"""Transcribe audio files to text."""

from pathlib import Path
from typing import Optional

import speech_recognition as sr


def audio_to_wav(source_path: Path, wav_path: Optional[Path] = None) -> Path:
    """Convert supported audio to WAV for recognition. Requires pydub (and ffmpeg for non-WAV)."""
    try:
        from pydub import AudioSegment
    except ImportError:
        if source_path.suffix.lower() != ".wav":
            raise RuntimeError(
                "For non-WAV files install pydub and ffmpeg: pip install pydub"
            )
        return source_path

    suffix = source_path.suffix.lower()
    if suffix == ".wav":
        return source_path

    loaders = {
        ".mp3": "mp3",
        ".m4a": "m4a",
        ".flac": "flac",
        ".ogg": "ogg",
    }
    fmt = loaders.get(suffix)
    if not fmt:
        raise ValueError(f"Unsupported format: {suffix}. Use one of: .wav, .mp3, .m4a, .flac, .ogg")

    audio = AudioSegment.from_file(str(source_path), format=fmt)
    out = wav_path or source_path.with_suffix(".wav")
    audio.export(str(out), format="wav")
    return out


def transcribe(
    audio_path: Path,
    language: str = "en",
    use_google: bool = True,
) -> str:
    """
    Transcribe audio file to text.
    Prefers Google Speech Recognition (free, requires internet).
    Set use_google=False and install whisper for local transcription.
    """
    wav_path = audio_to_wav(audio_path)
    recognizer = sr.Recognizer()

    with sr.AudioFile(str(wav_path)) as source:
        audio = recognizer.record(source)

    if use_google:
        try:
            # Google uses codes like en-US, fa-IR
            lang_code = f"{language}-{language.upper()}" if len(language) == 2 else language
            return recognizer.recognize_google(audio, language=lang_code)
        except sr.UnknownValueError:
            return ""
        except sr.RequestError as e:
            raise RuntimeError(f"Speech recognition request failed: {e}") from e

    # Optional: Whisper local
    try:
        import whisper
        model = whisper.load_model("base")
        result = model.transcribe(str(audio_path), language=language if language != "en" else None)
        return (result.get("text") or "").strip()
    except ImportError:
        raise RuntimeError(
            "Local transcription requires openai-whisper. Install with: pip install openai-whisper"
        )
