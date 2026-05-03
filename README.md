# waaz2alphaaz

ASR (speech-to-text) transcription tool for **Lisan-ud-Dawat** — the liturgical and community language of the Dawoodi Bohra community.

Converts audio (duas, madeh/nasheeds, speech) into Arabic-script text. The audio is an amalgam of Classical Arabic, Lisan-ud-Dawat, and Urdu — all transcribed to standard Arabic Unicode without diacritics.

---

## Project Status

**Phase 0 — Complete:** Repository structure, dependencies  
**Phase 1 — Pending:** Data pipeline (OCR → audio preprocessing → forced alignment)  
**Phase 2 — Pending:** Baseline evaluation (zero-shot MMS + Whisper)  
**Phase 3 — Pending:** Fine-tuning (MMS adapter)  
**Phase 4 — Pending:** CLI application  
**Phase 5 — Pending:** Web app (Streamlit/Gradio)  

---

## Repository Structure

```
waaz2alphaaz/
├── data/
│   ├── raw/
│   │   ├── audio/              # original recordings (any format)
│   │   └── text_sources/       # PDF, Word, images, or .txt files
│   ├── processed/
│   │   ├── audio/              # 16kHz mono WAV (normalized)
│   │   ├── transcripts/        # extracted + human-corrected text
│   │   └── aligned/            # segmented audio + transcript pairs
│   └── dataset/                # HuggingFace dataset format
├── src/
│   └── waaz2alphaaz/
│       ├── ocr.py              # text extraction from any document format
│       ├── preprocess.py       # audio normalization
│       ├── align.py            # forced alignment (WhisperX)
│       ├── baseline.py         # zero-shot evaluation
│       ├── finetune.py         # MMS adapter fine-tuning
│       └── transcribe.py       # CLI entry point
├── notebooks/                  # exploratory notebooks (one per phase)
├── models/                     # fine-tuned model checkpoints (not committed)
└── wiki/                       # project knowledge base
```

---

## Setup

### Prerequisites

- Python 3.10+
- `ffmpeg` installed on your system:
  ```bash
  brew install ffmpeg        # macOS
  sudo apt install ffmpeg    # Ubuntu/Debian
  ```

### Install

```bash
git clone https://github.com/abucturab/waaz2alphaaz.git
cd waaz2alphaaz
python -m venv .venv
source .venv/bin/activate     # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

---

## Usage (Phase 4 — not yet implemented)

```bash
python -m waaz2alphaaz path/to/audio.wav
```

---

## Data Pipeline

```
data/raw/text_sources/   +   data/raw/audio/
         │                          │
         ▼                          ▼
     ocr.py                   preprocess.py
  (extract text)            (→ 16kHz mono WAV)
         │                          │
         └──────────┬───────────────┘
                    ▼
               align.py
         (WhisperX forced alignment)
                    │
                    ▼
            data/dataset/
      (HuggingFace dataset format)
```

Supported text source formats: `.txt`, `.docx`, `.pdf` (text-based or scanned), `.jpg`, `.png`

---

## Wiki

Project knowledge base lives in [`wiki/`](wiki/). Start with [`wiki/schema.md`](wiki/schema.md).

Covers: Lisan-ud-Dawat language, ASR for low-resource languages, model options, fine-tuning process, data collection.

---

## License

MIT
