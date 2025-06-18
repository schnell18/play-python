import logging
import os
import time
from datetime import datetime
from itertools import product
from pathlib import Path

import librosa
import pandas as pd
import torchaudio as ta
from chatterbox.tts import ChatterboxTTS

from common import (
    _reset_peak_memory_stats,
    analyze_text,
    cleanup,
    combine_metrics,
    get_memory_metrics,
    persist_progress,
    save_partial_metric,
)


def gen_experiment_items(tasks):
    dikts = []
    for name, spec in tasks.items():
        configs = spec["configs"]
        text = spec["text"]
        for config in configs:
            dikts.append(
                {
                    "name": name,
                    "text": text,
                    "exaggeration": config[0],
                    "cfg_weight": config[1],
                    "temperature": config[2],
                }
            )
    return pd.DataFrame(dikts)


def _setup_fn():
    return ChatterboxTTS.from_pretrained(device="cuda")


def do_expermient(
    experiment_name,
    tasks,
    result_dir="results",
    **kwargs,
):
    df_all = gen_experiment_items(tasks)
    progress_path = os.path.join(result_dir, experiment_name, "progress.csv")
    if Path(progress_path).exists():
        df_saved = pd.read_csv(progress_path)
        df_all = df_all.merge(
            df_saved,
            how="left",
            on=["name", "exaggeration", "cfg_weight", "temperature"],
        )
        # filter already processed repos, equivalent to SQL is null
        df_todo = df_all.query("status != status or status != 1")
    else:
        df_all["status"] = 0
        df_all["completion_time"] = ""
        df_todo = df_all
    print("*" * 72)
    print("Sub-task list:")
    print(df_all)
    cnt_todo, cnt_tot = len(df_todo), len(df_all)
    print(f"Todo:{cnt_todo}, Done: {cnt_tot - cnt_todo}, Total: {cnt_tot}")
    if cnt_todo == 0:
        print("Tasks completed!")
    print("*" * 72)
    if cnt_todo == 0:
        return

    df_todo = df_todo.sort_values(
        by=["name", "exaggeration", "cfg_weight", "temperature"],
        ascending=False,
    )
    for idx, row in df_todo.iterrows():
        name = row["name"]
        exaggeration = row["exaggeration"]
        cfg_weight = row["cfg_weight"]
        temperature = row["temperature"]
        text = row["text"]

        metric = _init_metrics(name, exaggeration, cfg_weight, temperature)
        print("*" * 72)
        print(
            f"Generating {name} w/ exag={exaggeration}, cfg_w={cfg_weight}, temp={temperature}"
        )
        print("*" * 72)

        _reset_peak_memory_stats()
        model = _setup_fn()
        allot, reserved = get_memory_metrics()
        metric["load_mem_allot"] = allot
        metric["load_mem_reserved"] = reserved
        # Evaluate the model
        metric = generate(
            name,
            text,
            model,
            exaggeration,
            cfg_weight,
            temperature,
            metric,
            result_dir,
        )
        metric["eval_mem_allot"], metric["eval_mem_reserved"] = get_memory_metrics()

        cleanup(model)
        save_partial_metric(
            experiment_name,
            name,
            exaggeration,
            cfg_weight,
            temperature,
            metric,
            result_dir,
        )
        df_all.loc[
            (df_all["name"] == name)
            & (df_all["temperature"] == temperature)
            & (df_all["cfg_weight"] == cfg_weight)
            & (df_all["temperature"] == temperature),
            ["status", "completion_time"],
        ] = 1, datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        persist_progress(df_all, progress_path)
    # combine metrics
    combine_metrics(experiment_name, result_dir)


def generate(
    name,
    text,
    model,
    exaggeration,
    cfg_weight,
    temperature,
    metric,
    result_dir,
):
    t1 = time.time()
    # If you want to synthesize with a different voice, specify the audio prompt
    reference_audio_path = "justin.wav"
    wav = model.generate(
        text,
        exaggeration=exaggeration,
        cfg_weight=cfg_weight,
        temperature=temperature,
        audio_prompt_path=reference_audio_path,
    )
    fp = os.path.join(
        result_dir, f"{name}-{exaggeration}-{cfg_weight}-{temperature}.wav"
    )
    ta.save(fp, wav, model.sr)
    t2 = time.time()
    metric["gen_duration"] = t2 - t1

    metric["audio_length"] = librosa.get_duration(path=fp)
    metric["file_size"] = os.path.getsize(fp)
    ret = analyze_text(text)
    metric.update(ret)
    return metric


def _init_metrics(name, exaggeration, cfg_weight, temperature):
    return {
        "name": name,
        "exaggeration": exaggeration,
        "cfg_weight": cfg_weight,
        "temperature": temperature,
        "load_mem_allot": 0,
        "load_mem_reserved": 0,
        "eval_mem_allot": 0,
        "eval_mem_reserved": 0,
        "gen_duration": 0,
        "audio_length": 0,
        "file_size": 0,
    }


########################################################################
#  Misc experiments
########################################################################


def experiment_misc(permutations):
    text = """
This week, Aotearoa New Zealand officially celebrates Matariki for the
fourth time, marked by the reappearance in the night sky of the star cluster
also known as the Pleiades. Yet, ironically, the accompanying celebrations
and the legislation that declares Matariki a public holiday miss the mark.
They fail to promote and protect the country's dark skies, which are crucial
to seeing the stars in this small constellation.
"""
    text_thesis_abstract = """Large Language Models have exhibited remarkable capabilities in
tasks such as natural language comprehension, content generation, and knowledge
retrieval. However, training and serving these models require substantial
computational resources, posing a significant barrier to AI application
development and research. To address these challenges, various model
compression techniques have been explored, with quantization emerging as a key
approach.
"""
    tasks = {
        "thesis_abstract": {
            "text": text_thesis_abstract,
            "configs": permutations,
        },
        "matariki_light_pollution": {
            "text": text,
            "configs": permutations,
        },
    }
    do_expermient(
        "experiment_misc",
        tasks,
        result_dir="/fdata/chatterbox/results",
    )


def main():
    logging.basicConfig(
        format="%(asctime)s %(levelname)s [%(name)s] %(message)s",
        level=logging.INFO,
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    exaggerations = [0.4, 0.5, 0.6, 0.7, 0.8]
    cfg_weights = [0.3, 0.5, 0.6]
    temperatures = [0.2, 0.5, 0.8, 1.0]
    permutations = list(product(exaggerations, cfg_weights, temperatures))
    experiment_misc(permutations)


if __name__ == "__main__":
    max_threads = str(min(8, os.cpu_count()))
    os.environ["OMP_NUM_THREADS"] = max_threads
    os.environ["OPENBLAS_NUM_THREADS"] = max_threads
    os.environ["MKL_NUM_THREADS"] = max_threads
    os.environ["VECLIB_MAXIMUM_THREADS"] = max_threads
    os.environ["NUMEXPR_NUM_THREADS"] = max_threads
    os.environ["NUMEXPR_MAX_THREADS"] = max_threads

    main()
