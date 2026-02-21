"""CLI entry point for waaz2alphaaz."""

import argparse
from pathlib import Path

from . import __version__
from .alphaaz import apply_alphaaz
from .transcriber import transcribe
from .writer import write_document

Format = str  # "docx" | "txt" | "md"


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Transcribe voice clips and output documents in custom language (Alphaaz)."
    )
    parser.add_argument("input", type=Path, help="Path to voice clip (WAV, MP3, M4A, FLAC, OGG)")
    parser.add_argument("-o", "--output", type=Path, default=Path("transcript.docx"), help="Output file path")
    parser.add_argument(
        "--format",
        choices=("docx", "txt", "md"),
        default="docx",
        help="Output format (default: docx)",
    )
    parser.add_argument(
        "--language",
        default="en",
        help="Input speech language code (default: en)",
    )
    parser.add_argument(
        "--no-custom",
        action="store_true",
        help="Skip custom language mapping; output raw transcription",
    )
    parser.add_argument(
        "--config",
        type=Path,
        default=None,
        help="Path to Alphaaz config YAML (default: config/alphaaz.yaml)",
    )
    parser.add_argument(
        "--local",
        action="store_true",
        help="Use local Whisper for transcription (pip install openai-whisper)",
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")

    args = parser.parse_args()

    if not args.input.exists():
        parser.error(f"Input file not found: {args.input}")

    text = transcribe(args.input, language=args.language, use_google=not args.local)
    if not text.strip():
        print("No speech detected or transcription returned empty.")
        text = "(No transcription)"

    if not args.no_custom:
        text = apply_alphaaz(text, config_path=args.config)

    write_document(text, args.output, format=args.format, title="Transcription")
    print(f"Wrote {args.output}")


if __name__ == "__main__":
    main()
