import gc
import glob
import os
import re
import string
from datetime import datetime
from pathlib import Path

import pandas as pd
import torch


def analyze_text(text):
    """
    Analyze text to calculate number of sentences, words, and average word length.

    Args:
        text (str): The text to analyze

    Returns:
        dict: Dictionary containing analysis results
    """
    if not text or not text.strip():
        return {"sentences": 0, "words": 0, "average_word_length": 0}

    # Count sentences (split by sentence-ending punctuation)
    sentence_endings = re.compile(r"[.!?]+")
    sentences = sentence_endings.split(text.strip())
    # Filter out empty sentences
    sentences = [s.strip() for s in sentences if s.strip()]
    sentence_count = len(sentences)

    # Count words and calculate total character length
    # Remove punctuation and convert to lowercase
    translator = str.maketrans("", "", string.punctuation)
    clean_text = text.translate(translator).lower()
    words = clean_text.split()

    word_count = len(words)

    # Calculate average word length
    if word_count > 0:
        total_chars = sum(len(word) for word in words)
        avg_word_length = total_chars / word_count
    else:
        avg_word_length = 0

    return {
        "sentences": sentence_count,
        "words": word_count,
        "avg_words": round(avg_word_length, 2),
    }


def persist_progress(df, progress_path):
    """Save the progress of experiment for resumption."""
    Path(progress_path).parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(progress_path, index=False)


def save_partial_metric(
    experiment_name,
    name,
    exaggeration,
    cfg_weight,
    temperature,
    metric,
    result_dir,
):
    metrics = [metric]
    df = pd.DataFrame(metrics)
    result_dir = os.path.join(result_dir, experiment_name)
    os.makedirs(result_dir, exist_ok=True)
    file_name = (
        f"{result_dir}/partial-{name}-{exaggeration}-{cfg_weight}-{temperature}.csv"
    )
    df.to_csv(file_name, index=False)


def _dump_cuda_mem_snapshot(experiment_name, model_id, algo, result_dir):
    mem_fp = f"{result_dir}/{experiment_name}/mem-snapshot-{algo}-{model_id.split('/')[1]}.pickle"
    torch.cuda.memory._dump_snapshot(mem_fp)


def combine_metrics(experiment_name, result_dir):
    dfs = []
    iters = glob.iglob(f"{result_dir}/{experiment_name}/partial-*.csv")
    for it in iters:
        df = pd.read_csv(it)
        dfs.append(df)
    combined = pd.concat(dfs)
    ts_str = datetime.now().strftime("%Y%m%d%H%M%S")
    file_name = f"{result_dir}/{experiment_name}/result-{experiment_name}-{ts_str}.csv"
    Path(file_name).parent.mkdir(parents=True, exist_ok=True)
    combined.to_csv(file_name, index=False)


def cleanup(model):
    del model
    torch.cuda.empty_cache()
    gc.collect()


def _reset_peak_memory_stats():
    return torch.cuda.reset_peak_memory_stats()


def get_memory_metrics():
    return torch.cuda.max_memory_allocated(), torch.cuda.max_memory_reserved()
