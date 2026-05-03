#!/usr/bin/env python3
"""
waaz2alphaaz — cross-platform environment setup.

Creates a virtual environment and installs all dependencies with the
correct PyTorch build for your hardware (Apple Silicon, NVIDIA GPU, or CPU).

Usage:
    python setup.py

Supports: macOS (Intel + Apple Silicon), Linux, Windows
Requires: Python 3.10+
"""

import os
import platform
import subprocess
import sys
from pathlib import Path

# ── Constants ─────────────────────────────────────────────────────────────────

MIN_PYTHON = (3, 10)
VENV_DIR = Path(".venv")
REQUIREMENTS = Path("requirements.txt")

# PyTorch index URLs by CUDA version
TORCH_INDEX = {
    "cu124": "https://download.pytorch.org/whl/cu124",
    "cu121": "https://download.pytorch.org/whl/cu121",
    "cu118": "https://download.pytorch.org/whl/cu118",
    "cpu":   "https://download.pytorch.org/whl/cpu",
}

# ── Helpers ───────────────────────────────────────────────────────────────────

def step(msg: str) -> None:
    print(f"\n{'─' * 60}\n  {msg}\n{'─' * 60}")

def info(msg: str) -> None:
    print(f"  ✓ {msg}")

def warn(msg: str) -> None:
    print(f"  ⚠  {msg}")

def fail(msg: str) -> None:
    print(f"\n  ✗ {msg}\n")
    sys.exit(1)

def run(cmd: list, capture: bool = False) -> subprocess.CompletedProcess:
    print(f"    $ {' '.join(str(c) for c in cmd)}")
    return subprocess.run(
        cmd,
        check=True,
        capture_output=capture,
        text=True,
    )

# ── Platform detection ────────────────────────────────────────────────────────

def get_system() -> str:
    """Return 'mac', 'linux', or 'windows'."""
    s = platform.system()
    return {"Darwin": "mac", "Linux": "linux", "Windows": "windows"}.get(s, s.lower())

def is_apple_silicon() -> bool:
    return platform.system() == "Darwin" and platform.machine() == "arm64"

def detect_cuda_version() -> float | None:
    """
    Return CUDA version as a float (e.g. 12.1) or None if not available.
    Tries nvidia-smi first, then nvcc as fallback.
    """
    # Try nvidia-smi (available on any machine with NVIDIA drivers)
    try:
        result = subprocess.run(
            ["nvidia-smi"],
            capture_output=True, text=True, check=True,
        )
        for line in result.stdout.splitlines():
            if "CUDA Version:" in line:
                version_str = line.split("CUDA Version:")[1].strip().split()[0]
                return float(version_str)
    except (subprocess.CalledProcessError, FileNotFoundError, ValueError):
        pass

    # Fallback: nvcc
    try:
        result = subprocess.run(
            ["nvcc", "--version"],
            capture_output=True, text=True, check=True,
        )
        for line in result.stdout.splitlines():
            if "release" in line.lower():
                part = line.split("release")[1].strip().split(",")[0].strip()
                return float(part)
    except (subprocess.CalledProcessError, FileNotFoundError, ValueError):
        pass

    return None

def pick_torch_index(system: str) -> str | None:
    """
    Return the PyTorch --index-url for this machine, or None to use PyPI default.
    Mac uses PyPI default (includes MPS support for Apple Silicon automatically).
    """
    if system == "mac":
        return None  # PyPI default works for both Intel and Apple Silicon

    cuda = detect_cuda_version()

    if cuda is None:
        return TORCH_INDEX["cpu"]
    elif cuda >= 12.4:
        return TORCH_INDEX["cu124"]
    elif cuda >= 12.1:
        return TORCH_INDEX["cu121"]
    elif cuda >= 11.8:
        return TORCH_INDEX["cu118"]
    else:
        warn(f"CUDA {cuda} detected but no matching wheel — falling back to CPU build.")
        return TORCH_INDEX["cpu"]

# ── venv helpers ──────────────────────────────────────────────────────────────

def venv_python() -> Path:
    """Return path to the Python executable inside the venv."""
    if platform.system() == "Windows":
        return VENV_DIR / "Scripts" / "python.exe"
    return VENV_DIR / "bin" / "python"

def venv_pip() -> Path:
    if platform.system() == "Windows":
        return VENV_DIR / "Scripts" / "pip.exe"
    return VENV_DIR / "bin" / "pip"

def activate_hint() -> str:
    if platform.system() == "Windows":
        return r".venv\Scripts\activate"
    return "source .venv/bin/activate"

# ── ffmpeg check ──────────────────────────────────────────────────────────────

def check_ffmpeg() -> None:
    step("Checking system dependency: ffmpeg")
    try:
        result = subprocess.run(
            ["ffmpeg", "-version"],
            capture_output=True, text=True, check=True,
        )
        version_line = result.stdout.splitlines()[0] if result.stdout else "unknown"
        info(f"ffmpeg found — {version_line}")
    except FileNotFoundError:
        warn("ffmpeg not found. It is required for audio processing.")
        system = get_system()
        if system == "mac":
            print("     Install with:  brew install ffmpeg")
        elif system == "linux":
            print("     Install with:  sudo apt install ffmpeg")
        elif system == "windows":
            print("     Download from: https://ffmpeg.org/download.html")
            print("     Or via choco:  choco install ffmpeg")
        print("     Re-run setup.py after installing ffmpeg.\n")

# ── Main setup ────────────────────────────────────────────────────────────────

def main() -> None:
    print("\n  waaz2alphaaz — environment setup\n")

    # ── 1. Python version check ───────────────────────────────────────────────
    step("Checking Python version")
    current = sys.version_info[:2]
    if current < MIN_PYTHON:
        fail(
            f"Python {MIN_PYTHON[0]}.{MIN_PYTHON[1]}+ required. "
            f"You have {current[0]}.{current[1]}."
        )
    info(f"Python {current[0]}.{current[1]} ✓")

    # ── 2. Detect platform ────────────────────────────────────────────────────
    step("Detecting platform")
    system = get_system()
    cuda = detect_cuda_version()

    info(f"OS: {platform.system()} {platform.machine()}")

    if system == "mac" and is_apple_silicon():
        info("Apple Silicon detected — PyTorch will use MPS (Metal) backend")
    elif cuda:
        info(f"NVIDIA GPU detected — CUDA {cuda}")
    else:
        info("No GPU detected — using CPU build")

    torch_index = pick_torch_index(system)

    # ── 3. Create virtual environment ─────────────────────────────────────────
    step("Creating virtual environment (.venv)")
    if VENV_DIR.exists():
        info(".venv already exists — skipping creation")
    else:
        run([sys.executable, "-m", "venv", str(VENV_DIR)])
        info(".venv created")

    python = venv_python()
    pip = venv_pip()

    # ── 4. Upgrade pip ────────────────────────────────────────────────────────
    step("Upgrading pip")
    run([str(python), "-m", "pip", "install", "--upgrade", "pip"])

    # ── 5. Install PyTorch (platform-specific) ────────────────────────────────
    step("Installing PyTorch")
    torch_cmd = [str(pip), "install", "torch", "torchaudio"]
    if torch_index:
        torch_cmd += ["--index-url", torch_index]
    run(torch_cmd)

    # ── 6. Install remaining dependencies ────────────────────────────────────
    step("Installing project dependencies (requirements.txt)")
    if not REQUIREMENTS.exists():
        fail("requirements.txt not found. Are you running from the project root?")
    run([str(pip), "install", "-r", str(REQUIREMENTS)])

    # ── 7. Check ffmpeg ───────────────────────────────────────────────────────
    check_ffmpeg()

    # ── 8. Verify core imports ────────────────────────────────────────────────
    step("Verifying installation")
    verify_script = (
        "import torch, transformers, datasets, easyocr; "
        "print('torch:', torch.__version__); "
        "print('transformers:', transformers.__version__); "
        "print('MPS available:', torch.backends.mps.is_available()); "
        "print('CUDA available:', torch.cuda.is_available())"
    )
    run([str(python), "-c", verify_script])

    # ── Done ──────────────────────────────────────────────────────────────────
    print(f"""
{'═' * 60}
  Setup complete!

  Activate your environment:
    {activate_hint()}

  Then run the tool:
    python -m waaz2alphaaz <audio_file>
{'═' * 60}
""")


if __name__ == "__main__":
    main()
