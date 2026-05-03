# Process: Environment Setup

> Summary: How to set up the waaz2alphaaz Python environment using setup.py on any platform.

Last updated: 2026-05-02

---

## Overview

`setup.py` is a cross-platform environment setup script. Run it once after cloning the repo. It creates a Python virtual environment and installs all dependencies with the correct PyTorch build for your hardware.

```bash
python setup.py
```

Supports: macOS (Intel + Apple Silicon), Linux, Windows.  
Requires: Python 3.10+, ffmpeg (see below).

---

## What it does (in order)

1. **Checks Python version** — exits if below 3.10
2. **Detects platform** — identifies OS and whether CUDA/Apple Silicon is present
3. **Creates `.venv`** — skips if already exists
4. **Upgrades pip** — inside the venv
5. **Installs PyTorch** — picks the correct index URL (see table below)
6. **Installs `requirements.txt`** — all remaining project dependencies
7. **Checks ffmpeg** — warns with install instructions if missing (does not exit)
8. **Verifies install** — imports `torch`, `transformers`, `datasets`, `easyocr` and prints versions

---

## PyTorch wheel selection

| Platform | Wheel | Notes |
|---|---|---|
| macOS (Apple Silicon) | PyPI default | Includes MPS (Metal) backend automatically |
| macOS (Intel) | PyPI default | CPU build |
| Linux / Windows — CUDA ≥ 12.4 | `cu124` | `download.pytorch.org/whl/cu124` |
| Linux / Windows — CUDA ≥ 12.1 | `cu121` | `download.pytorch.org/whl/cu121` |
| Linux / Windows — CUDA ≥ 11.8 | `cu118` | `download.pytorch.org/whl/cu118` |
| Linux / Windows — no GPU | `cpu` | `download.pytorch.org/whl/cpu` |

CUDA version is detected by trying `nvidia-smi` first, then `nvcc` as fallback.

---

## ffmpeg

ffmpeg is required by WhisperX (forced alignment) and pydub (audio format conversion). It is **not** installed by setup.py — it must be installed at the OS level.

Install instructions:

```bash
brew install ffmpeg               # macOS
sudo apt install ffmpeg           # Ubuntu/Debian
choco install ffmpeg              # Windows (Chocolatey)
# Or download from https://ffmpeg.org/download.html
```

If ffmpeg is not found, setup.py prints the appropriate install command and continues. You can install it later without re-running setup.py.

---

## Activating the environment

After setup completes, activate before running any project code:

```bash
source .venv/bin/activate     # macOS / Linux
.venv\Scripts\activate        # Windows
```

---

## Common failure modes

| Symptom | Likely cause | Fix |
|---|---|---|
| `Python 3.10+ required` | Wrong Python on PATH | Use `python3.10 setup.py` or install 3.10+ |
| `requirements.txt not found` | Run from wrong directory | `cd` to repo root first |
| `pip install` fails for `whisperx` | Missing system build tools | Install Xcode CLT (Mac) or Visual C++ (Windows) |
| ffmpeg warning printed | ffmpeg not installed | Follow printed instructions and re-run any ffmpeg-dependent steps later |
| `easyocr` import fails | Missing OpenCV | `pip install opencv-python` inside `.venv` |

---

## Re-running setup.py

Safe to re-run at any time. The venv creation step is skipped if `.venv` already exists; pip and packages are upgraded in place.

---

## Related

- [Fine-tuning ASR for a New Language](fine_tuning_asr_for_new_language.md)
- [Data Collection for a New Language](data_collection_for_new_language.md)
