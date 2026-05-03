# Transcription Tool Options for Lisan-ud-Dawat

> Summary: A structured comparison of all viable ASR approaches for building a Lisan-ud-Dawat transcription tool, with data requirements, accuracy estimates, effort levels, and a recommended two-stage MVP strategy.

## Purpose

This artifact documents the technical options available for building an automatic speech recognition (ASR) / transcription system for Lisan-ud-Dawat — a low-resource language with an Arabic-derived script and a Gujarati phonological substrate. It is the primary decision-making reference for the waaz2alphaaz project.

## Options Comparison

| Approach | Data Needed | Expected WER | Effort | Best For |
|---|---|---|---|---|
| Whisper large-v3 zero-shot (Arabic) | 0 hours | 60–85% | Minimal | Demo, transcript bootstrapping |
| MMS zero-shot (Arabic code) | 0 hours | 55–80% | Minimal | Baseline evaluation |
| MMS adapter fine-tune (30 min) | 0.5h | 35–60% | Low | Very early stage MVP |
| MMS adapter fine-tune (5h) | 5h | 20–40% | Low–Medium | First usable model |
| Whisper medium LoRA fine-tune (5h) | 5h | 25–45% | Medium | Good balance of speed/quality |
| Whisper large-v3 LoRA fine-tune (10h) | 10h | 15–35% | Medium | Production MVP |
| Whisper large-v3 full fine-tune (50h) | 50h | 8–25% | Medium–High | Mature production system |
| IndicWav2Vec fine-tune | 5–30h | 15–30% | Medium | Leverages Indic phonological pre-training |
| wav2vec2 XLSR CTC fine-tune | 10–50h | 20–35% | Medium | Established pipeline, large community |
| Whisper + forced alignment (existing texts) | 0 labeled | Bootstrap only | Medium | Generating training data |
| Google USM API | 5–20h (cloud) | High | Low (costly) | Production if budget allows |
| Custom ASR from scratch | 200h+ | High | Very High | Not viable for this project stage |

## Approach Profiles

### Whisper large-v3 (OpenAI)
- **Architecture**: Encoder-decoder Transformer, 1.5B parameters
- **Arabic support**: Native (99 languages including Arabic `ar`)
- **Fine-tuning**: Full fine-tune or LoRA via HuggingFace PEFT
- **Key advantage**: Highest accuracy ceiling; encoder-decoder handles code-switching better than CTC
- **Key limitation**: Needs LoRA or large GPU for practical fine-tuning; outputs no diacritics by default
- **License**: MIT (open source, commercial use permitted)
- See: [OpenAI Whisper](../entities/whisper.md)

### Meta MMS (Massively Multilingual Speech)
- **Architecture**: wav2vec 2.0 + language-specific adapters, 300M–1B parameters
- **Coverage**: 1,107 languages including Arabic and Gujarati
- **Fine-tuning**: Adapter-only — extremely data-efficient (30–60 min viable)
- **Key advantage**: Training domain is religious/liturgical audio — directly matches Lisan-ud-Dawat waaz domain; lowest data requirement
- **Key limitation**: CC-BY-NC license (non-commercial only); no built-in diacritics
- See: [Meta MMS Model](../entities/mms_model.md)

### wav2vec2 / XLSR (Meta)
- **Architecture**: Encoder-only + CTC head
- **Coverage**: XLSR-53 (53 langs), XLSR-128 (128 langs)
- **Fine-tuning**: Standard CTC fine-tuning; freeze feature extractor, train transformer + head
- **Key advantage**: Self-supervised pre-training; low hallucination risk; easy KenLM integration
- **Key limitation**: Older architecture; weaker zero-shot than Whisper; needs language model for best results
- **License**: Apache 2.0
- See: [wav2vec 2.0 / XLSR](../entities/wav2vec.md)

### IndicWav2Vec (AI4Bharat)
- **Architecture**: wav2vec 2.0 pre-trained on 40 Indic languages
- **Key advantage**: Pre-training covers Gujarati and other languages phonologically close to Lisan-ud-Dawat's Indic substrate — likely better representations for Gujarati-derived phonemes than Arabic-focused models
- **Key limitation**: Less coverage of Arabic phonemes (the other half of Lisan-ud-Dawat)
- **Potential strategy**: Combine IndicWav2Vec features with Arabic language model

## Recommended Strategy: Two-Stage MVP

### Stage 1 — Immediate (Data: 0.5–2 hours)

**MMS Adapter Fine-tuning**

Why:
1. Most data-efficient model available — usable results with 30–60 minutes of labeled audio
2. Training domain (religious audio) matches the Dawoodi Bohra waaz corpus
3. Arabic phonological coverage from 1,100+ language pre-training
4. Adapter-only training runs on an 8GB consumer GPU or Google Colab T4
5. Non-commercial research license acceptable for community project

Action:
- Collect a 1–2 hour recording session with 5+ community speakers reading prepared sentences
- Annotate using Label Studio with Whisper zero-shot pre-annotation
- Train MMS adapter (`facebook/mms-300m`); estimate 2–4 hours on Colab T4
- Use output to bootstrap transcription of larger audio collection

Expected outcome: WER ~30–50% — unusable as standalone product but viable as a transcription assistant (generates a draft for a human to correct)

### Stage 2 — Production MVP (Data: 10–50 hours)

**Whisper large-v3 LoRA Fine-tuning**

Why:
1. Highest accuracy ceiling of any open-source approach
2. Encoder-decoder architecture is more robust to code-switching and diacritics than CTC
3. Built-in timestamp support useful for the waaz2alphaaz application
4. Arabic transfer: Whisper large-v3 has already seen Arabic script, phonemes, and vocabulary
5. MIT license permits any downstream use

Action:
- Use Stage 1 MMS model to generate draft transcripts for 20–50 hours of audio
- Human-correct drafts (faster than transcribing from scratch)
- Fine-tune Whisper large-v3 with LoRA using HuggingFace `peft` library
- Target GPU: 24GB VRAM (A10G/A100 on cloud) or use gradient checkpointing on 16GB

Expected outcome: WER 15–30% with 10–20 hours of data; WER <20% with 50+ hours

## Related Projects (Analogues)

| Language | Script | Data Used | Model | WER Achieved |
|---|---|---|---|---|
| Moroccan Darija | Arabic | ~50h | Whisper medium FT | ~28% |
| Sindhi | Arabic-derived | ~30h | wav2vec2 XLSR FT | ~12% CER |
| Uyghur | Arabic-derived | ~20h | XLSR FT | ~25% WER |
| Pashto | Arabic-extended | ~45h | wav2vec2 | ~18–25% WER |
| Faroese | Latin | ~50h | Whisper FT | ~15% WER |

Lisan-ud-Dawat is most analogous to **Sindhi** and **Pashto**: Arabic-script, South Asian linguistic context, additional characters beyond standard Arabic. Both achieved strong results with 20–50 hours of labeled audio.

## Open Questions

1. **Data access**: Can community approval be obtained for waaz recordings as training data? This is the critical dependency.
2. **Script encoding**: What Unicode encoding does the community currently use for digital Lisan-ud-Dawat text? Any custom fonts in use?
3. **Diacritics policy**: Should the ASR output include tashkeel/harakat? Requires diacritized transcripts if yes.
4. **Domain scope**: Waaz only, or also conversational speech? Impacts data collection strategy.
5. **Deployment target**: Local app, web API, mobile? Affects model size choice.

## Status

Draft — pending project scope definition and community engagement.

## Cross-references

- [ASR for Low-Resource Languages](../concepts/asr_for_low_resource_languages.md)
- [OpenAI Whisper](../entities/whisper.md)
- [Meta MMS Model](../entities/mms_model.md)
- [wav2vec 2.0 / XLSR](../entities/wav2vec.md)
- [Fine-tuning ASR for a New Language](../processes/fine_tuning_asr_for_new_language.md)
- [Data Collection for a New Language](../processes/data_collection_for_new_language.md)
- [Lisan-ud-Dawat](../concepts/lisan_ud_dawat.md)
- [ASR Papers and Tools Reference](../references/asr_papers_and_tools.md)
