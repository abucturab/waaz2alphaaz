# wav2vec 2.0 / XLSR

> Summary: Facebook AI's self-supervised speech representation learning framework, with multilingual XLSR variants that serve as the acoustic backbone for MMS and are widely used as fine-tuning bases for low-resource ASR.

## Overview

wav2vec 2.0 (Facebook/Meta AI, 2020) is a self-supervised learning framework for speech representations. It learns powerful acoustic features by training on unlabeled audio — masking portions of the latent speech representation and learning to distinguish the correct masked frame from distractors (contrastive learning over quantized representations). The result is a model that, even without any transcription labels, learns phonetically meaningful features.

**XLSR** (Cross-Lingual Speech Representations) extends wav2vec 2.0 to multilingual settings. XLSR-53 was trained on 53 languages; XLSR-128 on 128 languages; the MMS project (see [MMS entity](mms_model.md)) uses wav2vec 2.0 architecture scaled to 1,100+ languages.

For ASR fine-tuning, a CTC (Connectionist Temporal Classification) head is added on top of the encoder, and the model is trained on labeled audio-transcript pairs.

## Key Properties

- **Architecture**: CNN feature extractor + Transformer encoder + quantization module. No decoder — outputs are CTC logits over a character/token vocabulary.
- **Self-supervised pre-training**: Trained on unlabeled audio (LibriSpeech, CommonVoice, VoxPopuli, MLS, etc.). Pre-training creates general acoustic representations; fine-tuning adapts to a specific language and task.
- **CTC decoding**: Outputs sequence of character probabilities; decoded with greedy or beam-search (optionally with n-gram language model via KenLM or beam-search + LM).
- **Model sizes**:
  - `wav2vec2-base`: 95M parameters
  - `wav2vec2-large`: 317M parameters
  - `XLSR-53`: 317M parameters, pre-trained on 53 languages
  - `XLSR-128` / `mms-300m`: ~300M, 128–1100+ languages
  - `mms-1b`: ~1B parameters, full MMS coverage
- **Supported languages**: XLSR-53 covers 53 languages including Arabic (`ar`), Urdu (`ur`), Hindi (`hi`). XLSR-128 adds more. MMS covers 1,100+.
- **License**: Apache 2.0 (wav2vec 2.0 and XLSR variants); MMS uses CC-BY-NC 4.0.
- **HuggingFace**: `facebook/wav2vec2-large-xlsr-53`, `facebook/wav2vec2-xls-r-300m`, `facebook/mms-300m`, etc.

## Interfaces & Dependencies

- **Python packages**: `transformers`, `datasets`, `torchaudio`, `soundfile`.
- **Fine-tuning libraries**: HuggingFace `Trainer`, or custom PyTorch training loop.
- **CTC language model decoding**: `pyctcdecode` library + KenLM n-gram LM improves WER significantly post-hoc.
- **Audio requirements**: 16kHz, mono, float32 normalized. Use `torchaudio` or `librosa` for preprocessing.
- **Tokenizer**: For Arabic-script languages, use a character-level tokenizer. Build a custom vocabulary from your transcription corpus.

## Known Behaviors & Gotchas

- **CTC vs encoder-decoder**: wav2vec 2.0/CTC is a monotonic alignment model — it cannot reorder or insert words not in the audio. This is more constrained than Whisper's attention-based decoder, which means less hallucination but also less ability to "guess" unclear words.
- **No built-in language model**: Raw CTC output often has character-level errors. Adding a KenLM n-gram LM during beam search decoding can reduce WER by 5–15 percentage points.
- **Long audio**: Like MMS, wav2vec 2.0 needs to be chunked for audio longer than ~30 seconds. HuggingFace `pipeline("automatic-speech-recognition")` handles this automatically with `chunk_length_s` parameter.
- **Pre-training language proximity**: Fine-tuning XLSR-53 or XLSR-128 on Lisan-ud-Dawat benefits from the model having seen Arabic and Urdu during pre-training — the acoustic features for those languages are already encoded.
- **Arabic character normalization**: Arabic text has many Unicode variants for the same character (e.g., different forms of ‎ه, different alef variants). Normalize before building vocabulary and training.
- **Fine-tuning instability**: CTC fine-tuning can be unstable with very small datasets (<1 hour). Use low learning rates (1e-4 to 3e-4), warmup steps, and monitor CTC loss carefully.
- **GPU memory**: `large-xlsr` fine-tuning needs ~16GB VRAM. Use gradient checkpointing to reduce memory.

## Fine-tuning Recipe Summary

1. **Choose base model**: `facebook/wav2vec2-large-xlsr-53` or `facebook/mms-300m` (broader language coverage).
2. **Build vocabulary**: Extract all unique characters from transcription corpus; add `[PAD]`, `[UNK]`, `|` (word boundary), `<s>`, `</s>`.
3. **Create processor**: `Wav2Vec2Processor` with custom `Wav2Vec2CTCTokenizer`.
4. **Prepare dataset**: Resample to 16kHz, extract input values, tokenize transcripts.
5. **Configure training**: Freeze feature extractor for first N steps; use AdamW with warmup; CTC loss.
6. **Evaluate**: WER on held-out test set.
7. **Optional**: Add KenLM language model for beam search decoding.

**Minimum viable data**: ~1 hour for a proof-of-concept; 5–20 hours for a usable MVP. With MMS language adapters, even less may suffice.

## Comparison to Whisper for Low-Resource Use Cases

| Aspect | wav2vec 2.0 / XLSR | Whisper |
|---|---|---|
| Architecture | Encoder-only + CTC | Encoder-decoder |
| Hallucination risk | Low (CTC constraint) | Higher |
| Fine-tuning efficiency | High (freeze encoder) | Medium (LoRA needed for efficiency) |
| Language model integration | Easy (KenLM + pyctcdecode) | Harder (decoder already attends to context) |
| Long-form audio | Needs chunking | Built-in 30s window |
| Zero-shot performance | Weaker | Stronger |
| Training data domain | Self-supervised (diverse audio) | Weakly supervised (web audio) |

## Current Status

- Mature, stable framework. wav2vec 2.0 paper published 2020; XLSR-53 2021; XLSR-128 / MMS 2023.
- Widely used in academia and industry for low-resource ASR research.
- HuggingFace ecosystem is excellent — multiple tutorials, colab notebooks, and community fine-tunes available.
- Recommended as the **primary fine-tuning architecture** for Lisan-ud-Dawat given MMS's domain match and adapter efficiency.

## Cross-references

- [ASR for Low-Resource Languages](../concepts/asr_for_low_resource_languages.md)
- [Meta MMS Model](mms_model.md)
- [OpenAI Whisper](whisper.md)
- [Fine-tuning ASR for a New Language](../processes/fine_tuning_asr_for_new_language.md)
- [Transcription Tool Options](../artifacts/transcription_tool_options.md)
