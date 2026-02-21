"""Custom language (Alphaaz) conversion: map transcribed text to custom vocabulary."""

from pathlib import Path
from typing import Dict, Optional

import yaml


def load_alphaaz_config(config_path: Optional[Path] = None) -> dict:
    """Load Alphaaz mapping config from YAML."""
    if config_path is None:
        config_path = Path(__file__).resolve().parent.parent / "config" / "alphaaz.yaml"
    if not config_path.exists():
        return {"mappings": {}, "passthrough_unknown": True}
    with open(config_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {"mappings": {}, "passthrough_unknown": True}


def build_phrase_map(mappings: Dict[str, str]) -> list[tuple[str, str]]:
    """Build sorted list of (phrase, replacement) for longest-match replacement."""
    items = [(k.strip().lower(), v) for k, v in (mappings or {}).items() if k]
    items.sort(key=lambda x: -len(x[0]))
    return items


def apply_alphaaz(text: str, config_path: Optional[Path] = None) -> str:
    """
    Convert transcribed text to custom language using Alphaaz mappings.
    Uses longest-match replacement (case-insensitive on source).
    """
    config = load_alphaaz_config(config_path)
    mappings = config.get("mappings", {})
    passthrough = config.get("passthrough_unknown", True)

    phrase_list = build_phrase_map(mappings)
    if not phrase_list:
        return text

    result: list[str] = []
    remainder = text
    while remainder:
        remainder_lower = remainder.lower()
        matched = False
        for phrase, replacement in phrase_list:
            if remainder_lower.startswith(phrase):
                result.append(replacement)
                remainder = remainder[len(phrase) :].lstrip()
                matched = True
                break
        if not matched:
            # Advance by one character (or word for cleaner output)
            idx = 1
            for i, c in enumerate(remainder):
                if c.isspace() or i == len(remainder) - 1:
                    idx = i + 1
                    break
            result.append(remainder[:idx] if passthrough else "?")
            remainder = remainder[idx:]

    return "".join(result)
