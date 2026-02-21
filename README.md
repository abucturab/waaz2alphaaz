# waaz2alphaaz

Transcription software that accepts a voice clip, transcribes it, and outputs a document in a custom language (Alphaaz).

## Features

- **Voice clip input**: Supports common audio formats (WAV, MP3, M4A, FLAC, OGG).
- **Speech-to-text**: Transcribes speech using a local or optional cloud engine.
- **Custom language (Alphaaz)**: Maps transcribed text to a custom vocabulary/script so the output document uses your defined language.

## Setup

```bash
cd waaz2alphaaz
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Optional: OpenAI Whisper (recommended for accuracy)

Install [ffmpeg](https://ffmpeg.org/) for audio handling, then:

```bash
pip install openai-whisper
```

If you don't install Whisper, the app falls back to the built-in `speech_recognition` engine (requires an internet connection for Google Speech API or use of a local engine).

## Usage

### Transcribe a single file

```bash
python -m waaz2alphaaz transcribe path/to/voice_clip.mp3 -o output.docx
```

### Transcribe and output plain text (custom language)

```bash
python -m waaz2alphaaz transcribe path/to/voice_clip.wav -o transcript.txt --format txt
```

### Options

- `-o, --output`: Output file path (default: `transcript.docx`).
- `--format`: Output format: `docx`, `txt`, or `md`.
- `--language`: Input speech language code (e.g. `en`, `fa`). Default: `en`.
- `--no-custom`: Skip custom language mapping; output raw transcription.

## Custom language (Alphaaz)

Edit `waaz2alphaaz/config/alphaaz.yaml` to define how words or phrases from the transcription are mapped to your custom language. The transcribed text is then converted according to this mapping before writing the document.

Example mapping:

```yaml
# alphaaz.yaml
mappings:
  hello: "αλφα"
  world: "ααζ"
  thank you: "θανα"
```

## Project structure

```
waaz2alphaaz/
├── README.md
├── requirements.txt
├── pyproject.toml
├── config/
│   └── alphaaz.yaml      # Custom language mappings
└── waaz2alphaaz/
    ├── __init__.py
    ├── __main__.py       # CLI entry point
    ├── transcriber.py    # Transcription logic
    ├── alphaaz.py        # Custom language conversion
    └── writer.py         # Document output (DOCX, TXT, MD)
```

## License

MIT
