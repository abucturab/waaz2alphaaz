# Data Collection for a New Language

> Summary: How to systematically collect, record, and annotate audio training data for a new language that has no existing ASR corpus, with guidance specific to community-based languages like Lisan-ud-Dawat.

## When to Use This

Use this process when:
- No publicly available labeled audio data exists for your target language
- You need to build a training corpus from scratch using community resources
- You have access to native speakers willing to contribute recordings or transcriptions

This is a prerequisite for [Fine-tuning ASR for a New Language](fine_tuning_asr_for_new_language.md).

## Prerequisites

- At least a small group of native speakers willing to participate
- A text corpus to read from (religious texts, written materials, news, literature)
- Recording equipment (smartphones with a quiet room are acceptable for a start)
- Annotation tools (see Step 5 below)
- A basic understanding of the script used (for Lisan-ud-Dawat: Arabic-derived script)
- Storage: ~1 hour of audio at 16kHz mono ≈ 115MB uncompressed WAV

## Data Quality vs. Quantity Trade-off

For ASR fine-tuning, **quality beats quantity**. Ten hours of accurately transcribed audio will outperform 100 hours with 20% transcription errors. Key quality factors:
- Accurate transcription (what was actually said)
- Consistent normalization (same spelling conventions throughout)
- Clean audio (minimal background noise, clipping, reverb)
- Speaker diversity (multiple speakers, genders, ages if possible)

## Steps

### Phase 1: Text Corpus Preparation (Weeks 1–2)

1. **Gather existing written materials**
   - Religious texts in Lisan-ud-Dawat (sermons, duas, khutbas, waaz transcripts)
   - Published books, newsletters, or community documents
   - Subtitles or transcripts from any existing recordings
   - Aim for 10,000–100,000 words of diverse text

2. **Normalize the text corpus**
   - Agree on spelling conventions for common words (especially variant spellings)
   - Decide on diacritics policy: include tashkeel or not (affects vocabulary size and annotation difficulty)
   - Define punctuation conventions
   - Create a style guide document for annotators — this is critical for consistency

3. **Prepare prompt texts for recording**
   - Select 500–2000 sentences of varying length (5–20 words each)
   - Prefer phonetically diverse sentences (cover all phonemes in the language)
   - Include domain-relevant vocabulary (religious terms, community-specific words)
   - Tool: use `phonetically_balanced_corpus` selection (research technique; can be approximated manually)

### Phase 2: Recording Setup (Week 2–3)

4. **Choose a recording method**

   **Option A: Browser-based recording tool (recommended for community scale)**
   - [Mozilla Common Voice](https://commonvoice.mozilla.org/) — open platform for community recording, but requires language addition (can self-host)
   - [VoxBox](https://github.com/ftyers/commonvoice-utils) or similar self-hosted tools
   - Custom web app with Web Audio API (relatively simple to build)
   
   **Option B: Dedicated recording app**
   - [Korvai](https://github.com/CoEDL/korvai) — linguistic field recording app
   - [ELAR](https://elar.soas.ac.uk/) tools — for endangered language documentation
   
   **Option C: In-person recording sessions**
   - Use Audacity (free, open source) for supervised recording sessions
   - Script: read prompts from screen, record each as a separate file
   - Advantage: quality control; disadvantage: requires in-person coordination

5. **Recording guidelines for participants**
   - Record in a quiet room (no fans, traffic, background TV)
   - Hold phone/microphone 15–30cm from mouth
   - Speak naturally and clearly — not exaggeratedly slow
   - Read each prompt once, then stop (do not re-read unless clearly failed)
   - Format: 16kHz or 44.1kHz, mono or stereo (resample later), WAV or MP3 (WAV preferred)
   - Target: 5–30 seconds per clip

6. **Minimum viable recording cohort**
   - Ideally: 10+ speakers (mix of gender, age, dialect variation)
   - Acceptable for MVP: 3–5 speakers
   - Each speaker records 30–120 minutes of prompts
   - Total target: 5–10 hours for a first training run

### Phase 3: Transcription and Annotation (Ongoing)

7. **Annotation approach**

   **Option A: Controlled recording (easiest to annotate)**
   - Record speakers reading pre-written prompts
   - Transcript is already known — just verify accuracy
   - Annotator listens and corrects any deviations from prompt
   
   **Option B: Existing recordings (harder)**
   - Use sermons, waaz recordings, lectures
   - Requires full transcription from scratch
   - Use a forced-alignment tool (Whisper, WebMAUS, MFA) to get initial alignment, then correct manually

8. **Annotation tools**
   
   **[Label Studio](https://labelstud.io/)** — recommended primary tool
   - Free, open source, self-hostable
   - Has an audio + text annotation template
   - Supports team collaboration
   - Exports to JSON, CSV, HuggingFace dataset format
   
   **[Audacity](https://www.audacityteam.org/)** with label tracks
   - Good for segmenting long recordings into labeled clips
   - Export: `File > Export > Export Labels`
   
   **[ELAN](https://archive.mpi.nl/tla/elan)**
   - Professional linguistic annotation tool
   - Supports multi-tier annotation, alignment, gloss
   - Steeper learning curve but powerful for complex annotation schemes
   
   **[WebMAUS / BAS](https://clarin.phonetik.uni-muenchen.de/BASWebServices/)** — forced aligner
   - Useful for automatically aligning a transcript to audio (when you have both)
   - Supports Arabic; may partially work for Lisan-ud-Dawat <!-- unverified: Arabic model in WebMAUS may not handle Lisan-ud-Dawat phonemes -->

9. **Quality assurance**
   - Each clip should be reviewed by at least one other annotator (double annotation)
   - Use inter-annotator agreement (IAA) metric: target >95% character-level agreement
   - Flag and re-annotate any clip below agreement threshold
   - Reject clips with significant background noise, clipping, or unclear speech

### Phase 4: Data Pipeline and Format

10. **Organize files**
    ```
    data/
    ├── audio/
    │   ├── speaker_001/
    │   │   ├── clip_001.wav
    │   │   ├── clip_002.wav
    │   │   └── ...
    │   └── speaker_002/
    ├── transcripts/
    │   ├── speaker_001.tsv   # clip_id | transcript | duration | split
    │   └── speaker_002.tsv
    └── metadata.json         # speaker demographics, recording conditions, date
    ```

11. **Create a HuggingFace Dataset** for easy integration with training pipelines
    ```python
    from datasets import Dataset, Audio
    import pandas as pd
    df = pd.read_csv("all_transcripts.tsv", sep="\t")
    dataset = Dataset.from_dict({
        "audio": df["audio_path"].tolist(),
        "sentence": df["transcript"].tolist(),
        "speaker_id": df["speaker_id"].tolist(),
    })
    dataset = dataset.cast_column("audio", Audio(sampling_rate=16000))
    dataset.save_to_disk("lisan_asr_dataset")
    ```

12. **Run basic statistics**
    - Total hours of audio
    - Hours per speaker
    - Vocabulary size (unique words)
    - Average clip duration
    - Distribution of clip lengths

### Phase 5: Iterative Expansion

13. **Deploy a first model and collect corrections** (after initial training)
    - Build a simple transcription tool with the initial model
    - Have native speakers use it and correct errors
    - Collect corrected transcriptions as new training data — this is the most efficient data collection method (active learning / correction loop)

14. **Target data milestones**
    - **30 minutes**: Sanity-check fine-tuning (validate the pipeline works)
    - **1–2 hours**: First usable model (WER ~50–60%, usable for assisted transcription)
    - **5–10 hours**: MVP quality (WER ~30–40%, useful for community transcription)
    - **20–50 hours**: Production quality (WER ~15–25%)
    - **100+ hours**: High quality, multiple domains (WER <15%)

## Common Failure Modes

- **Inconsistent transcription conventions**: Different annotators spell the same word differently. Fix: create and enforce a style guide before starting.
- **Single-speaker bias**: Model learns one person's accent. Fix: prioritize speaker diversity even with fewer total hours.
- **Domain mismatch**: All data is formal recitation but use case includes conversation. Fix: collect domain-diverse data from the start.
- **Poor audio quality**: Recordings made in noisy environments degrade training significantly. Fix: strict recording guidelines and audio quality check in the pipeline.
- **Low participation**: Community members don't engage with recording tool. Fix: in-person recording sessions at community events (mosques, jamaat gatherings).
- **Script inconsistency**: Ambiguous words transcribed with/without diacritics inconsistently. Fix: strip all diacritics for the first training run; add them back later.

## Outputs

- A structured audio corpus (WAV files + TSV/JSON transcripts)
- A HuggingFace dataset ready for fine-tuning
- A transcription style guide for the language
- Speaker metadata (for train/test split stratification)
- Statistics report (total hours, speakers, vocabulary size)

## Cross-references

- [ASR for Low-Resource Languages](../concepts/asr_for_low_resource_languages.md)
- [Fine-tuning ASR for a New Language](fine_tuning_asr_for_new_language.md)
- [Transcription Tool Options](../artifacts/transcription_tool_options.md)
- [Mozilla Common Voice Reference](../references/mozilla_common_voice.md)
- [Label Studio Reference](../references/label_studio.md)
