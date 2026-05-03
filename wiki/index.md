# Wiki Index

> Summary: Top-level catalog of all knowledge pages, organized by category.

Last updated: 2026-05-02

---

## Entities
- [OpenAI Whisper](entities/whisper.md) — Encoder-decoder multilingual ASR model; primary fine-tuning candidate for Lisan-ud-Dawat transcription
- [Meta MMS Model](entities/mms_model.md) — 1,100+ language ASR model with adapter fine-tuning; best choice for very low data scenarios
- [wav2vec 2.0 / XLSR](entities/wav2vec.md) — Self-supervised speech model; CTC fine-tuning backbone underlying MMS
- [Dawoodi Bohra Community](entities/dawoodi_bohra_community.md) — The ~1–2 million strong Shia Ismaili community and sole native-speaker group of Lisan-ud-Dawat

## Concepts
- [Lisan-ud-Dawat](concepts/lisan_ud_dawat.md) — The liturgical and vernacular language of the Dawoodi Bohra community; a Gujarati-Arabic-Persian contact language
- [Lisan-ud-Dawat Script](concepts/lisan_ud_dawat_script.md) — The modified Perso-Arabic writing system with Indic phoneme extensions used for Lisan-ud-Dawat
- [ASR for Low-Resource Languages](concepts/asr_for_low_resource_languages.md) — Overview of approaches and tradeoffs for building speech recognition systems with scarce training data

## Processes
- [Environment Setup](processes/setup_environment.md) — Cross-platform setup using setup.py: venv, PyTorch wheel selection, ffmpeg, verification
- [Fine-tuning ASR for a New Language](processes/fine_tuning_asr_for_new_language.md) — End-to-end pipeline for adapting a pre-trained multilingual model to Lisan-ud-Dawat
- [Data Collection for a New Language](processes/data_collection_for_new_language.md) — How to collect, record, and annotate an audio corpus when none exists

## Artifacts
- [Transcription Tool Options](artifacts/transcription_tool_options.md) — Structured comparison of all viable ASR approaches with recommendation for waaz2alphaaz MVP

## References
- [Lisan-ud-Dawat Resources](references/lisan_ud_dawat_resources.md) — Academic papers, community publications, and digital resources for Lisan-ud-Dawat
- [ASR Papers and Tools](references/asr_papers_and_tools.md) — Key papers, HuggingFace models, datasets, and tools for low-resource ASR development

## Glossary
- [Acronyms](glossary/acronyms.md)
- [Terms](glossary/terms.md)
