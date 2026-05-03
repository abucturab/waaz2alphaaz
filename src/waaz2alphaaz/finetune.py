"""
MMS adapter fine-tuning for Lisan-ud-Dawat.

Base model : facebook/mms-300m
Approach   : adapter-only (backbone frozen, ~2M adapter params trained)
Data       : HuggingFace dataset from data/dataset/
Output     : model checkpoint saved to models/mms-lisan-v1/
"""

from pathlib import Path


def train(
    dataset_dir: str | Path,
    output_dir: str | Path,
    num_epochs: int = 30,
    batch_size: int = 8,
    learning_rate: float = 3e-4,
) -> None:
    """Fine-tune MMS adapter on the Lisan-ud-Dawat dataset."""
    raise NotImplementedError("Phase 3 — not yet implemented")
