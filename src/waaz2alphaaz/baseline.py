"""
Zero-shot baseline evaluation.

Tests two models out-of-the-box on the aligned dataset (no fine-tuning):
  1. facebook/mms-1b-all  (target_lang="arb")
  2. openai/whisper-large-v3  (language="ar")

Computes WER and CER. Results are logged to wiki/artifacts/.
"""

from pathlib import Path


def run_baseline(dataset_dir: str | Path, output_dir: str | Path) -> dict:
    """Run both zero-shot models on the dataset, return WER/CER results dict."""
    raise NotImplementedError("Phase 2 — not yet implemented")
