"""
Forced alignment: sync a known transcript to its audio using WhisperX.

Takes a processed WAV file + corrected transcript text and produces
time-stamped, segmented audio clips paired with their transcripts.
Output is saved in HuggingFace dataset format.
"""

from pathlib import Path


def align(audio_path: str | Path, transcript_path: str | Path, output_dir: str | Path) -> None:
    """Align transcript to audio, segment, and write output clips + metadata."""
    raise NotImplementedError("Phase 1 — not yet implemented")


def build_dataset(aligned_dir: str | Path, dataset_dir: str | Path) -> None:
    """Convert aligned clips into a HuggingFace dataset saved to dataset_dir."""
    raise NotImplementedError("Phase 1 — not yet implemented")
