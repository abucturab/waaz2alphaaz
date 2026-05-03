"""
Text extraction from multiple document formats.

Supported inputs: .txt, .docx, .pdf (text-based or scanned), .jpg, .png, .tiff
Output: plain Arabic-script text with diacritics stripped.
"""

from pathlib import Path


def extract_text(source_path: str | Path) -> str:
    """Extract text from a document file, strip diacritics, return plain string."""
    raise NotImplementedError("Phase 1 — not yet implemented")


def extract_all(input_dir: str | Path, output_dir: str | Path) -> None:
    """Extract text from all files in input_dir, write .txt files to output_dir."""
    raise NotImplementedError("Phase 1 — not yet implemented")
