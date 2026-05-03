"""
Audio preprocessing: convert any audio format to 16kHz mono WAV.
"""

from pathlib import Path


def normalize_audio(input_path: str | Path, output_path: str | Path) -> None:
    """Convert audio to 16kHz mono WAV and normalize loudness."""
    raise NotImplementedError("Phase 1 — not yet implemented")


def normalize_all(input_dir: str | Path, output_dir: str | Path) -> None:
    """Normalize all audio files in input_dir, write WAVs to output_dir."""
    raise NotImplementedError("Phase 1 — not yet implemented")
