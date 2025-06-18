#!/usr/bin/env Rscript

library(ggplot2)
library(dplyr)
library(tidyverse)
library(readr)

combined_csv_fp <- "result-experiment_misc-20250618231759.csv"

df_kb <- read_csv(combined_csv_fp) |>
  mutate(
    name = factor(
      name,
      levels = c("thesis_abstract", "matariki_light_pollution"),
      labels = c("Thesis Abstract", "Matariki Light Pollution")
    ),
    gen_duration = formatC(gen_duration, format = "f", digits = 2),
    eval_mem_reserved = formatC(
      eval_mem_reserved / 1024^3,
      format = "f", digits = 2
    ),
  ) |>
  rename(
    val_memory = eval_mem_reserved,
    val_speed = gen_duration
  ) |>
  pivot_longer(
    cols = c("val_memory", "val_speed"),
    names_to = c(".value", "kind"),
    names_sep = "_"
  )

df_plot <- df_kb |> filter(cfg_weight == 0.6)
# df_plot <- df_kb |> filter(exaggeration == 0.6)
# df_plot <- df_kb |> filter(name == "Thesis Abstract")
# df_plot <- df_kb |> filter(name == "Matariki Light Pollution")

plt <- ggplot(df_plot, aes(x = temperature, y = val)) +
  geom_point(aes(color = kind, shape = kind)) +
  geom_line(aes(group = kind, color = kind)) +
  labs(
    x = "Temperature",
    y = "Speed (Seconds)/Memory (GiB)"
  ) +
  theme(
    legend.position = "bottom",
    strip.background = element_rect(
      color = "darkgray", fill = "white", linewidth = 1.0, linetype = "solid"
    ),
    axis.text.x = element_text(size = 12),
    axis.text.y = element_text(size = 8),
    axis.title.x = element_text(size = 12),
    axis.title.y = element_text(size = 12),
    legend.title = element_blank()
  ) +
  facet_grid(name ~ exaggeration, scales = "free")

ggsave(
  create.dir = TRUE,
  plot = plt,
  paste0("pdfs/gen-speed-mem-feature.pdf"),
  height = 10,
  width = 14
)

# vim: sw=2:
