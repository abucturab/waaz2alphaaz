# ASR Papers and Tools Reference

> Summary: Annotated bibliography of key papers, HuggingFace resources, datasets, and tools for building low-resource ASR systems, with a focus on Arabic-script and Indic languages.

## Location

Distributed across arXiv, ACL Anthology, HuggingFace Hub, and GitHub. All links below were valid as of the last review date.

## Foundational Papers

### Core ASR Models

| Paper | Authors | Year | Key Contribution | URL |
|---|---|---|---|---|
| Whisper | Radford et al. | 2022 | 680K-hour multilingual ASR; 99 languages | https://arxiv.org/abs/2212.04356 |
| MMS | Pratap et al. | 2023 | ASR for 1,107 languages; adapter fine-tuning | https://arxiv.org/abs/2305.13516 |
| wav2vec 2.0 | Baevski et al. | 2020 | Self-supervised speech representations; CTC fine-tuning | https://arxiv.org/abs/2006.11477 |
| XLSR-53 | Conneau et al. | 2020 | Cross-lingual speech representations, 53 languages | https://arxiv.org/abs/2006.13979 |
| Google USM | Zhang et al. | 2023 | 2B-param model, 300+ languages (not open source) | https://arxiv.org/abs/2303.01037 |
| WhisperX | Bain et al. | 2023 | Whisper + word-level forced alignment | https://arxiv.org/abs/2303.00747 |

### Fine-tuning Techniques

| Paper | Authors | Year | Key Contribution | URL |
|---|---|---|---|---|
| LoRA | Hu et al. | 2022 | Low-rank adapter fine-tuning; applies to Whisper | https://arxiv.org/abs/2106.09685 |
| Lightweight Adapter Tuning | Le et al. | 2021 | Language adapters for multilingual speech | https://aclanthology.org/2021.acl-short.103/ |
| SpecAugment | Park et al. | 2019 | Data augmentation for ASR (time/frequency masking) | https://arxiv.org/abs/1904.08779 |

### Indic Language ASR (Relevant for Lisan-ud-Dawat's Gujarati substrate)

| Paper / Project | Authors | Year | Key Contribution |
|---|---|---|---|
| IndicWav2Vec | AI4Bharat | 2022 | wav2vec 2.0 pre-trained on 40 Indic languages including Gujarati |
| IndicSUPERB | AI4Bharat | 2023 | Benchmark for 26 Indic languages |
| Indic TTS | AI4Bharat | 2022 | TTS for Indic languages — text normalization techniques applicable to LuD |

**AI4Bharat GitHub**: https://github.com/AI4Bharat

## HuggingFace Models

### Arabic and Arabic-script Models

| Model | HuggingFace ID | Notes |
|---|---|---|
| Whisper large-v3 | `openai/whisper-large-v3` | Best general-purpose starting point for LuD |
| Whisper large-v3-turbo | `openai/whisper-large-v3-turbo` | Distilled; faster inference, slightly lower accuracy |
| MMS 300M (all langs) | `facebook/mms-300m` | Best for very low data; adapter fine-tuning |
| MMS 1B (all langs) | `facebook/mms-1b-all` | Higher capacity MMS |
| XLSR-53 | `facebook/wav2vec2-large-xlsr-53` | Good Arabic baseline; 53 languages |
| Arabic Whisper | `openai/whisper-large-v3` with `language="ar"` | Zero-shot Arabic baseline for LuD |
| Arabic XLSR fine-tune | `jonatasgrosman/wav2vec2-large-xlsr-53-arabic` | Community Arabic XLSR |
| Quranic Arabic Whisper | `tarteel-ai/whisper-base-ar-quran` | Fine-tuned on ~2,000h Quran recitation; religious domain |
| Urdu Whisper | `kmarle/whisper-medium-urdu` | Arabic-script, South Asian language — useful reference |
| Moroccan Darija | `AbderrahmanSkiredj/whisper-darija` | Dialectal Arabic Whisper fine-tune |

## Key Datasets

| Dataset | URL | Language | Hours | Notes |
|---|---|---|---|---|
| Mozilla Common Voice | https://commonvoice.mozilla.org | 100+ languages | Varies | Community-sourced; can add new languages |
| OpenSLR Pashto | https://openslr.org/54/ | Pashto | ~45h | Arabic-extended script; good LuD analogue |
| OpenSLR Urdu | https://openslr.org/79/ | Urdu | ~100h | Arabic-derived Nastaliq; useful for transfer |
| MGB-2 (Egyptian Arabic) | Unavailable publicly | Egyptian Arabic | ~1,200h | Dialectal Arabic benchmark |
| FLEURS | https://huggingface.co/datasets/google/fleurs | 102 languages | ~10h each | Includes Arabic and Gujarati |
| VoxPopuli | https://github.com/facebookresearch/voxpopuli | 23 EU languages | Varies | Parliamentary speech |

## Tools

### Audio Processing

| Tool | URL | Purpose |
|---|---|---|
| ffmpeg | https://ffmpeg.org | Audio conversion, resampling, format normalization |
| torchaudio | https://pytorch.org/audio | Python audio loading and resampling |
| pydub | https://github.com/jiaaro/pydub | Audio slicing and level normalization |
| Silero VAD | https://github.com/snakers4/silero-vad | Voice Activity Detection for audio chunking |
| pyannote-audio | https://github.com/pyannote/pyannote-audio | Speaker diarization; useful for multi-speaker waaz |

### Annotation and Data Collection

| Tool | URL | Purpose |
|---|---|---|
| Label Studio | https://labelstud.io | Audio transcription annotation; RTL support |
| Mozilla Common Voice | https://commonvoice.mozilla.org | Crowd-sourced recording platform |
| Audacity | https://www.audacityteam.org | Audio editing and segmentation |
| ELAN | https://archive.mpi.nl/tla/elan | Professional linguistic annotation |
| WhisperX | https://github.com/m-bain/whisperX | Whisper + forced word alignment |
| WebMAUS / BAS | https://clarin.phonetik.uni-muenchen.de/BASWebServices/ | Forced alignment (Arabic support) |

### Arabic / Indic Text Processing

| Tool | URL | Purpose |
|---|---|---|
| PyArabic | https://github.com/linuxscout/pyarabic | Arabic text normalization, diacritic stripping |
| CAMeL Tools | https://github.com/CAMeL-Lab/camel_tools | Arabic morphology, diacritization |
| arabic_reshaper | https://github.com/mpcabd/python-arabic-reshaper | Arabic text reshaping for display |
| python-bidi | https://github.com/MeirKriheli/python-bidi | Bidirectional text algorithm for RTL |
| IndicNLP Library | https://indicnlp.ai4bharat.org | Gujarati and other Indic language NLP |
| mishkal | https://github.com/linuxscout/mishkal | Arabic diacritizer (adds harakat) |

### Training and Fine-tuning

| Tool | URL | Purpose |
|---|---|---|
| HuggingFace Transformers | https://github.com/huggingface/transformers | Model loading, training, inference |
| HuggingFace PEFT | https://github.com/huggingface/peft | LoRA and adapter fine-tuning |
| HuggingFace Accelerate | https://github.com/huggingface/accelerate | Distributed training |
| KenLM | https://github.com/kpu/kenlm | n-gram language model for CTC beam search |
| pyctcdecode | https://github.com/kensho-technologies/pyctcdecode | CTC beam search decoder with KenLM |
| SpeechBrain | https://speechbrain.github.io | All-in-one speech toolkit |

## Key Tutorials

| Title | URL | Relevance |
|---|---|---|
| Fine-Tune Whisper For Multilingual ASR | https://huggingface.co/blog/fine-tune-whisper | Complete Whisper fine-tuning walkthrough |
| Fine-tuning MMS Adapter for Multi-Lingual ASR | https://huggingface.co/blog/mms_adapters | MMS adapter approach (most relevant for early-stage LuD) |
| Fine-Tune XLSR-Wav2Vec2 for low-resource ASR | https://huggingface.co/blog/fine-tune-xlsr-wav2vec2 | XLSR CTC fine-tuning walkthrough |
| Tarteel AI (Quranic ASR) | https://tarteel.ai | End-to-end example of religious domain ASR |

## When to Consult

- Choosing a base model → [Transcription Tool Options](../artifacts/transcription_tool_options.md)
- Setting up fine-tuning code → tutorials section above
- Handling Arabic text → PyArabic / CAMeL Tools
- Collecting and annotating data → Label Studio / Common Voice
- Finding a pre-trained starting checkpoint → HuggingFace models section

## Cross-references

- [ASR for Low-Resource Languages](../concepts/asr_for_low_resource_languages.md)
- [OpenAI Whisper](../entities/whisper.md)
- [Meta MMS Model](../entities/mms_model.md)
- [wav2vec 2.0 / XLSR](../entities/wav2vec.md)
- [Fine-tuning ASR for a New Language](../processes/fine_tuning_asr_for_new_language.md)
- [Data Collection for a New Language](../processes/data_collection_for_new_language.md)
- [Lisan-ud-Dawat Resources](lisan_ud_dawat_resources.md)
