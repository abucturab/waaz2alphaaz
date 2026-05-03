# OpenAI Whisper

> Summary: A large-scale multilingual speech recognition model from OpenAI, trained on 680,000 hours of diverse web audio, widely used as a base model for fine-tuning on low-resource languages.

## Overview

Whisper is an encoder-decoder transformer model released by OpenAI in September 2022 (v1) and updated through 2023–2024 (v2, v3, large-v3-turbo). It was trained on 680,000 hours of multilingual and multitask supervised data from the web, making it highly robust across accents, noise conditions, and domains.

Whisper performs multiple tasks: transcription (speech-to-text), translation (to English), language identification, and voice activity detection. It is available in multiple sizes, from `tiny` (39M parameters) to `large-v3` (1.5B parameters).

Whisper v3 large supports **99 languages** officially. The model was trained on a highly uneven distribution — English has the most data, followed by major European languages, then Chinese, Japanese, Korean, Arabic, Hindi, Urdu, and others.

## Key Properties

- **Architecture**: Encoder-decoder Transformer (similar to T5). Audio is converted to log-Mel spectrograms, encoded, then decoded autoregressively to text tokens.
- **Model sizes**: `tiny` (39M), `base` (74M), `small` (244M), `medium` (769M), `large-v2` (1.5B), `large-v3` (1.5B, improved), `large-v3-turbo` (~800M, distilled).
- **Input**: 30-second audio chunks, 16kHz, mono. Longer audio is handled via windowing.
- **Languages supported**: 99 in v3. Arabic (`ar`), Hindi (`hi`), Urdu (`ur`) are included. Lisan-ud-Dawat is NOT included.
- **Zero-shot Arabic performance**: Competitive with state-of-the-art on MSA; degrades for dialectal or minority Arabic-family languages.
- **License**: MIT (open source, fine-tuning permitted).
- **Training data**: ~680K hours web-scraped; quality is variable. Weakly supervised — transcripts are crawled, not manually annotated.
- **HuggingFace integration**: Available via `openai-whisper` package and `transformers` library (`WhisperForConditionalGeneration`).

## Interfaces & Dependencies

- **Python packages**: `openai-whisper` (official), `transformers` (HuggingFace), `faster-whisper` (CTranslate2-based, much faster inference).
- **Fine-tuning**: Supported via HuggingFace `Seq2SeqTrainer`. The encoder can be frozen (fine-tune decoder only) for very small datasets; full fine-tuning for larger datasets.
- **Language tokens**: Whisper uses a `<|language|>` token to condition on language. For a new language, you either re-use the closest token (e.g., `<|ar|>`) or add a new token and fine-tune.
- **Hardware**: `large-v3` requires ~10GB VRAM for inference; fine-tuning requires 24GB+ VRAM (use gradient checkpointing and LoRA to fit in 16GB).

## Known Behaviors & Gotchas

- **Hallucination on silence/noise**: Whisper is prone to hallucinating plausible-sounding text when audio is quiet or noisy. This is a known limitation, especially with `large` models.
- **Repetition loops**: Can get stuck repeating a phrase. Mitigation: use `logprob_threshold` and `no_speech_threshold` parameters.
- **30-second chunking artifacts**: Transcription quality degrades at chunk boundaries. Tools like `stable-ts` and `whisperx` improve timestamp alignment and chunking.
- **Arabic-script output**: Whisper outputs Arabic text with no short vowels (tashkeel/diacritics) by default. For Lisan-ud-Dawat, which may require diacritics to disambiguate words, this is a gap.
- **Right-to-left text**: Whisper outputs raw Unicode; RTL rendering must be handled by the downstream application.
- **Fine-tuning catastrophic forgetting**: Fine-tuning on a narrow dataset can cause the model to "forget" other languages. Use LoRA or freeze the encoder to mitigate.
- **`faster-whisper`**: CTranslate2-based implementation is 2–4x faster and uses less VRAM than the original; recommended for production deployment.
- **`whisper.cpp`**: C++ implementation, runs on CPU (including Apple Silicon via Metal), important for on-device deployment.

## Fine-tuning for a New Language

1. Prepare audio-transcript pairs (16kHz, mono WAV + plain text).
2. Build a `WhisperProcessor` with your language's tokenizer (either reuse Arabic or add custom tokens).
3. Use `WhisperForConditionalGeneration` with the `<|language|>` token set.
4. Fine-tune with `Seq2SeqTrainer` or a custom loop; batch size ~16, learning rate ~1e-5.
5. Evaluate with WER (Word Error Rate) and CER (Character Error Rate).

**Minimum viable data**: ~1 hour for a proof-of-concept; 5–10 hours for an MVP; 50+ hours for production quality.

**LoRA fine-tuning**: Libraries like `peft` from HuggingFace enable parameter-efficient fine-tuning with as little as 2–4GB VRAM using LoRA adapters.

## Current Status

- Latest stable: `large-v3-turbo` (late 2024). Whisper v3 large remains the highest-accuracy option.
- Actively maintained by OpenAI; HuggingFace integration well-maintained.
- Community fine-tuning is widespread — many fine-tunes for minority languages on HuggingFace Hub (search `whisper` + language name).
- Strong candidate for Lisan-ud-Dawat MVP: start zero-shot with `<|ar|>` language token, then fine-tune with collected data.

## Cross-references

- [ASR for Low-Resource Languages](../concepts/asr_for_low_resource_languages.md)
- [Meta MMS Model](mms_model.md)
- [wav2vec 2.0 / XLSR](wav2vec.md)
- [Fine-tuning ASR for a New Language](../processes/fine_tuning_asr_for_new_language.md)
- [Transcription Tool Options](../artifacts/transcription_tool_options.md)
- [Whisper Fine-tuning Guide (HuggingFace)](../references/whisper_finetuning_huggingface.md)
