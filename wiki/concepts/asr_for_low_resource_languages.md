# ASR for Low-Resource Languages

> Summary: An overview of the problem space and available approaches for building automatic speech recognition systems when training data is scarce or nonexistent for a target language.

## What It Is

Automatic Speech Recognition (ASR) for low-resource languages addresses the challenge of building transcription systems when a language has little or no existing labeled audio data, pre-trained acoustic models, or language models. The vast majority of the world's ~7,000 spoken languages fall into this category — including Lisan-ud-Dawat, the liturgical and everyday language of the Dawoodi Bohra community.

A "low-resource" language typically has:
- Fewer than 100 hours of transcribed audio (often fewer than 10 hours or none)
- No existing phoneme dictionary or pronunciation lexicon
- Little or no text corpus for language modeling
- Possibly an uncommon or modified writing script

## Why It Matters in This Domain

Lisan-ud-Dawat is spoken by a globally dispersed but culturally tight-knit community. There is virtually no publicly available ASR training data for this language. Building a transcription tool requires either:
1. Adapting a pre-trained multilingual model via transfer learning with limited collected data, or
2. Using zero/few-shot methods that leverage phonetic or linguistic similarity to supported languages (Arabic, Urdu, Gujarati), or
3. A combination of the above.

The writing system (a variant of Arabic script, sometimes called Lisani script) adds an additional layer: text normalization, diacritics, and right-to-left rendering must all be handled correctly.

## Key Principles

- **Transfer learning is central.** Modern large-scale pre-trained models (Whisper, MMS, wav2vec 2.0/XLSR) encode generalizable acoustic representations that can be fine-tuned with small datasets.
- **More data is always better, but diminishing returns set in.** For fine-tuning, 1–10 hours of transcribed audio can produce a usable model; 10–100 hours produces a good one.
- **Language proximity matters for zero-shot.** The closer the target language is (phonetically, lexically) to a language the base model knows, the better the zero-shot baseline will be. Lisan-ud-Dawat shares phonetics with Arabic and Gujarati.
- **Text pipeline is as important as acoustic model.** Even a good acoustic model will produce garbled output if the text normalization, tokenizer, or rendering pipeline is broken.
- **Iterative data collection beats waiting for perfection.** Bootstrap with a small dataset, deploy, collect corrections, retrain.
- **Community involvement is essential.** Native speakers are irreplaceable for transcription annotation and quality evaluation.

## Common Misunderstandings

- **"We need thousands of hours of data."** Not true for fine-tuning modern pre-trained models. 1–10 hours of quality transcribed audio can yield a working MVP.
- **"Whisper already supports Arabic, so it works."** Whisper's Arabic is Modern Standard Arabic and some dialects. Lisan-ud-Dawat is a distinct language with Gujarati/Indic substrate — zero-shot Arabic Whisper will produce partially intelligible but substantially incorrect output.
- **"We need to train from scratch."** Almost never the right choice for low-resource languages. Pre-trained models carry acoustic priors worth hundreds of thousands of GPU-hours.
- **"One model fits all tasks."** A model tuned for conversational speech will perform differently on recitations, religious texts, or fast speech. Task-specific fine-tuning matters.

## Examples

Comparable projects that have successfully built ASR for low-resource languages:
- **Sindhi ASR**: Fine-tuned Whisper and wav2vec 2.0 on ~10–30 hours of data; achieved word error rates (WER) of 20–40% depending on dialect.
- **Uyghur ASR**: Fine-tuned XLSR on ~50 hours; WER ~25%.
- **Gronings (Dutch dialect)**: Fine-tuned Whisper-small on ~5 hours; WER ~30%.
- **Faroese**: Fine-tuned Whisper on ~50 hours Common Voice data; WER dropped from ~80% (zero-shot) to ~15%.
- **Dialectal Arabic (Egyptian, Moroccan, etc.)**: MMS and Whisper both handle these with moderate zero-shot performance; fine-tuning improves significantly.

## Approaches at a Glance

| Approach | Data Needed | Accuracy Potential | Effort |
|---|---|---|---|
| Zero-shot (related language) | 0 hours | Low–Medium | Very low |
| Prompt engineering / language ID tricks | 0 hours | Low–Medium | Low |
| Fine-tune Whisper | 1–100 hours | Medium–High | Medium |
| Fine-tune MMS | 1–50 hours | Medium–High | Medium |
| Fine-tune XLSR/wav2vec 2.0 | 5–100 hours | Medium–High | Medium–High |
| Train from scratch (hybrid HMM/DNN or end-to-end) | 500+ hours | High | Very high |

For Lisan-ud-Dawat, the recommended path is **fine-tuning a multilingual pre-trained model** (Whisper or MMS), starting from a zero-shot Arabic/Urdu baseline.

## Cross-references

- [OpenAI Whisper](../entities/whisper.md)
- [Meta MMS Model](../entities/mms_model.md)
- [wav2vec 2.0 / XLSR](../entities/wav2vec.md)
- [Fine-tuning ASR for a New Language](../processes/fine_tuning_asr_for_new_language.md)
- [Data Collection for a New Language](../processes/data_collection_for_new_language.md)
- [Transcription Tool Options](../artifacts/transcription_tool_options.md)
