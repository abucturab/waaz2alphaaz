"""
CLI entry point: audio file → Arabic-script transcript (no diacritics).

Usage:
    python -m waaz2alphaaz <audio_file>
    waaz2alphaaz <audio_file>          # if installed via pip
"""

import sys
from pathlib import Path


def transcribe(audio_path: str | Path) -> str:
    """Load fine-tuned model, preprocess audio, run inference, return transcript."""
    raise NotImplementedError("Phase 4 — not yet implemented")


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: waaz2alphaaz <audio_file>")
        sys.exit(1)

    audio_path = Path(sys.argv[1])
    if not audio_path.exists():
        print(f"Error: file not found — {audio_path}")
        sys.exit(1)

    transcript = transcribe(audio_path)
    print(transcript)


if __name__ == "__main__":
    main()
