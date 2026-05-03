# Meta MMS Model

> Summary: Meta's Massively Multilingual Speech model, covering 1,100+ languages for ASR and TTS, trained primarily on religious audio data, making it a strong candidate for liturgical low-resource language transcription.

## Overview

The Massively Multilingual Speech (MMS) project was released by Meta AI in May 2023. It addresses the language gap in ASR by training on audio from religious texts — specifically the Bible and other Christian scriptures read aloud in hundreds of languages — sourced from organizations like Faith Comes By Hearing.

MMS covers **1,107 languages** for ASR (speech-to-text), **1,162 languages** for TTS (text-to-speech), and **4,017 languages** for language identification. This makes it the broadest language coverage of any publicly available ASR system.

MMS ASR models are based on **wav2vec 2.0** architecture (CTC decoding), while the TTS uses VITS architecture.

## Key Properties

- **Architecture**: wav2vec 2.0 (300M parameter base) with CTC head for ASR. A single multilingual model handles all 1,100+ languages.
- **Language coverage**: 1,107 languages for ASR. Includes Arabic, Urdu, Hindi, Gujarati, and numerous minority languages. Lisan-ud-Dawat is NOT directly included, but closely related liturgical varieties may be present.
- **Training data source**: Religious audio recordings (Bible, New Testament, etc.) — this means the model is particularly well-suited to **formal, liturgical, or read speech** rather than spontaneous conversation.
- **Data per language**: MMS was trained with as little as 2–32 hours per language for the lowest-resource ones. This validates that such small datasets can yield usable models.
- **License**: CC-BY-NC 4.0 (non-commercial use; fine-tuning permitted for research/non-profit; commercial use requires Meta's permission).
- **HuggingFace**: Available as `facebook/mms-300m`, `facebook/mms-1b`, `facebook/mms-1b-all`, and language-specific variants.
- **Character-level output**: MMS outputs characters, not BPE tokens. This is advantageous for Arabic script since characters map more directly to phonemes.

## Interfaces & Dependencies

- **Python packages**: `transformers` (HuggingFace) — `Wav2Vec2ForCTC`, `Wav2Vec2CTCTokenizer`.
- **CTC decoding**: Can use greedy decoding or beam search with a language model (KenLM n-gram LM is common).
- **Fine-tuning**: Follow the standard wav2vec 2.0/CTC fine-tuning recipe (see [wav2vec entity page](wav2vec.md)).
- **Language adapter approach**: MMS uses language-specific adapter layers in the transformer. For fine-tuning a new language, you add a new adapter rather than retraining the full model — very parameter-efficient.

## Known Behaviors & Gotchas

- **Religious/formal domain bias**: Because training data is religious recordings, MMS performs best on formal, clearly enunciated speech. Spontaneous conversation, code-switching, or colloquial registers will degrade performance more than with Whisper.
- **Liturgical advantage**: For a project transcribing religious recitations, sermons, or Quran-adjacent texts in Lisan-ud-Dawat, MMS's training domain is a strong fit.
- **Language adapters**: The adapter mechanism means fine-tuning is computationally cheap — you only train a small set of adapter weights, leaving the large pre-trained backbone frozen. This is ideal for very small datasets.
- **Arabic script support**: MMS handles Arabic-script languages (Arabic, Urdu, etc.) with character-level CTC. Custom character sets can be added for Lisan-ud-Dawat specific glyphs or diacritics.
- **No built-in diacritization**: Like Whisper, MMS does not add diacritics (tashkeel) automatically.
- **Non-commercial license**: If this project is for community use only (non-commercial), CC-BY-NC is acceptable. If any commercial use is contemplated, check Meta's MMS license terms.
- **No native long-audio support**: MMS/wav2vec operates on segments; audio must be chunked. Use VAD (Voice Activity Detection, e.g., Silero VAD or pyannote) for chunking.

## MMS for Lisan-ud-Dawat — Specific Notes

The Dawoodi Bohra community's Lisan-ud-Dawat shares many phonemes with Arabic and has Indic (Gujarati) substrate. Two starting strategies:

1. **Zero-shot with Arabic MMS**: Use `facebook/mms-1b-all` with Arabic language code. Will likely produce partial Arabic text with incorrect words for Lisan-ud-Dawat-specific vocabulary.
2. **Fine-tune with new language adapter**: Add a Lisan-ud-Dawat adapter to MMS, train on collected audio. Can start working with as little as 1–5 hours of transcribed audio.

The language-adapter approach makes MMS uniquely efficient for this use case: the backbone stays frozen, only ~2M adapter parameters need to be trained.

## Current Status

- Released May 2023; stable. No major architecture updates since release.
- Actively used in research and low-resource language community projects.
- HuggingFace integration is mature; fine-tuning tutorials available.
- **Strong recommendation** for liturgical/religious speech domains in Lisan-ud-Dawat.

## Cross-references

- [ASR for Low-Resource Languages](../concepts/asr_for_low_resource_languages.md)
- [OpenAI Whisper](whisper.md)
- [wav2vec 2.0 / XLSR](wav2vec.md)
- [Fine-tuning ASR for a New Language](../processes/fine_tuning_asr_for_new_language.md)
- [Transcription Tool Options](../artifacts/transcription_tool_options.md)
- [Meta MMS Paper Reference](../references/meta_mms_paper.md)
