# Fine-tuning ASR for a New Language

> Summary: Step-by-step process for adapting a pre-trained multilingual ASR model (Whisper or MMS/wav2vec) to transcribe a new, unsupported language using collected audio-transcript pairs.

## When to Use This

Use this process when:
- You have collected at least 30 minutes (ideally 1–10+ hours) of transcribed audio in the target language
- A zero-shot baseline from a multilingual model is insufficient for the use case
- You want to improve accuracy for a specific domain (e.g., religious recitation, conversational speech)

For Lisan-ud-Dawat, this process should be started once the first batch of transcribed audio (Step 1 of [Data Collection](data_collection_for_new_language.md)) is complete.

## Prerequisites

- Python 3.9+ environment with `transformers`, `datasets`, `torchaudio`, `evaluate`, `jiwer`, `accelerate`
- GPU with at least 16GB VRAM (for large models); 8GB acceptable for small/medium Whisper or MMS-300m with gradient checkpointing
- A dataset of audio files paired with transcriptions (see [Data Collection](data_collection_for_new_language.md))
- A chosen base model: Whisper large-v3, MMS-300m, or XLSR-300m (see [Transcription Tool Options](../artifacts/transcription_tool_options.md) for guidance)
- For Arabic-script languages: a normalized character vocabulary from the transcription corpus

## Steps

### Phase 1: Environment Setup

1. **Install dependencies**
   ```bash
   pip install transformers datasets torchaudio evaluate jiwer accelerate peft
   # For wav2vec/MMS CTC path:
   pip install pyctcdecode kenlm
   ```

2. **Verify GPU access**
   ```python
   import torch
   print(torch.cuda.is_available(), torch.cuda.get_device_properties(0).total_memory)
   ```

3. **Decide on model path** — see [Transcription Tool Options](../artifacts/transcription_tool_options.md):
   - Religious/liturgical domain → Start with MMS-300m or MMS-1b
   - General/conversational → Start with Whisper large-v3
   - Very limited compute → Start with Whisper small or medium

### Phase 2: Data Preparation

4. **Audit your dataset**
   - Check audio format: must be 16kHz, mono, WAV or FLAC
   - Resample if needed: `torchaudio.transforms.Resample(orig_freq, 16000)`
   - Remove clips shorter than 1 second or longer than 30 seconds
   - Check transcript encoding: UTF-8, correct Arabic/Lisani script

5. **Normalize transcriptions**
   - Remove punctuation that is not linguistically meaningful (optional: keep sentence boundaries)
   - Normalize Unicode: use `unicodedata.normalize('NFC', text)` for Arabic
   - Handle Arabic diacritics (tashkeel): decide whether to include or strip. **Recommendation**: strip for MVP to simplify vocabulary; add in later iterations.
   - Build character vocabulary: extract all unique characters from all transcripts
   - Ensure vocabulary includes: space ` `, silence marker `|`, `[UNK]`, `[PAD]`

6. **Split dataset**
   - 80% train / 10% validation / 10% test (adjust if data is very small)
   - For <1 hour total: 70% / 15% / 15%
   - Ensure test set has diverse speakers if possible

7. **Create HuggingFace Dataset**
   ```python
   from datasets import Dataset, Audio
   dataset = Dataset.from_dict({"audio": audio_paths, "sentence": transcripts})
   dataset = dataset.cast_column("audio", Audio(sampling_rate=16000))
   ```

### Phase 3: Model & Tokenizer Setup

#### Path A: Whisper Fine-tuning

8a. **Load processor and model**
    ```python
    from transformers import WhisperProcessor, WhisperForConditionalGeneration
    processor = WhisperProcessor.from_pretrained("openai/whisper-large-v3", language="arabic", task="transcribe")
    model = WhisperForConditionalGeneration.from_pretrained("openai/whisper-large-v3")
    # For new language token: either reuse "arabic" or add new token
    model.config.forced_decoder_ids = None
    model.config.suppress_tokens = []
    ```

8b. **LoRA setup** (recommended for <16GB VRAM or small datasets)
    ```python
    from peft import get_peft_model, LoraConfig, TaskType
    config = LoraConfig(task_type=TaskType.SEQ_2_SEQ_LM, r=32, lora_alpha=64,
                        target_modules=["q_proj","v_proj"], lora_dropout=0.05)
    model = get_peft_model(model, config)
    ```

#### Path B: MMS / wav2vec 2.0 Fine-tuning

8c. **Build custom tokenizer**
    ```python
    from transformers import Wav2Vec2CTCTokenizer, Wav2Vec2FeatureExtractor, Wav2Vec2Processor
    vocab_dict = {char: idx for idx, char in enumerate(sorted(vocab_set))}
    # Add special tokens
    vocab_dict["[UNK]"] = len(vocab_dict)
    vocab_dict["[PAD]"] = len(vocab_dict)
    # Save and load
    tokenizer = Wav2Vec2CTCTokenizer("vocab.json", unk_token="[UNK]", pad_token="[PAD]", word_delimiter_token="|")
    feature_extractor = Wav2Vec2FeatureExtractor(feature_size=1, sampling_rate=16000, padding_value=0.0, do_normalize=True)
    processor = Wav2Vec2Processor(feature_extractor=feature_extractor, tokenizer=tokenizer)
    ```

8d. **Load MMS model with new language adapter** <!-- unverified: exact API for adding new language adapter may differ from standard -->
    ```python
    from transformers import Wav2Vec2ForCTC
    model = Wav2Vec2ForCTC.from_pretrained("facebook/mms-300m",
        vocab_size=len(vocab_dict),
        ignore_mismatched_sizes=True)
    # Freeze the feature extractor
    model.freeze_feature_extractor()
    ```

### Phase 4: Training

9. **Configure training arguments**
   ```python
   from transformers import TrainingArguments
   training_args = TrainingArguments(
       output_dir="./lisan-asr",
       per_device_train_batch_size=8,        # Reduce if OOM
       gradient_accumulation_steps=2,
       learning_rate=3e-4,                    # Lower (1e-4) for Whisper
       warmup_steps=500,
       num_train_epochs=30,                   # More epochs for small datasets
       evaluation_strategy="steps",
       eval_steps=200,
       save_steps=200,
       logging_steps=50,
       load_best_model_at_end=True,
       metric_for_best_model="wer",
       fp16=True,                             # Use bf16 on Ampere GPUs
       gradient_checkpointing=True,
   )
   ```

10. **Define compute_metrics**
    ```python
    import evaluate
    wer_metric = evaluate.load("wer")
    def compute_metrics(pred):
        pred_ids = pred.predictions
        label_ids = pred.label_ids
        # Decode predictions and references
        pred_str = processor.batch_decode(pred_ids, skip_special_tokens=True)
        label_ids[label_ids == -100] = processor.tokenizer.pad_token_id
        label_str = processor.batch_decode(label_ids, skip_special_tokens=True)
        wer = wer_metric.compute(predictions=pred_str, references=label_str)
        return {"wer": wer}
    ```

11. **Train**
    ```python
    from transformers import Trainer
    trainer = Trainer(model=model, args=training_args,
                      train_dataset=train_dataset, eval_dataset=val_dataset,
                      tokenizer=processor.feature_extractor,
                      compute_metrics=compute_metrics)
    trainer.train()
    ```

12. **Monitor training**: Watch validation WER; stop if it plateaus or rises (overfitting). For small datasets (<5 hours), expect to train 20–50 epochs.

### Phase 5: Evaluation and Iteration

13. **Evaluate on test set**
    - Compute WER and CER on held-out test set
    - Listen to failed examples — identify systematic errors (missing words, wrong script, specific phoneme confusion)
    - Target WER thresholds: <40% is usable, <25% is good, <15% is excellent for a low-resource setting

14. **Error analysis**
    - Are errors clustered around specific phonemes or vocabulary? → More data for those patterns
    - Are errors consistent across speakers? → May indicate script normalization issues
    - Is the model confusing Arabic words with Lisan-ud-Dawat words? → Language model post-processing may help

15. **Optional: Add n-gram language model** (for MMS/wav2vec path)
    ```bash
    # Build KenLM n-gram LM from text corpus
    lmplz -o 5 <text_corpus.txt >lm.arpa
    build_binary lm.arpa lm.binary
    ```
    Then use `pyctcdecode` for beam search decoding with LM.

16. **Iterate**: Collect more data (see [Data Collection](data_collection_for_new_language.md)), retrain, evaluate. Even adding 30 minutes of targeted audio for known error patterns can improve WER significantly.

### Phase 6: Saving and Deployment

17. **Save model**
    ```python
    trainer.save_model("./lisan-asr-final")
    processor.save_pretrained("./lisan-asr-final")
    ```

18. **Push to HuggingFace Hub** (optional, for sharing)
    ```python
    trainer.push_to_hub("your-org/whisper-lisan-ud-dawat")
    ```

19. **Test inference pipeline**
    ```python
    from transformers import pipeline
    asr = pipeline("automatic-speech-recognition", model="./lisan-asr-final")
    result = asr("test_audio.wav")
    print(result["text"])
    ```

## Common Failure Modes

- **OOM (out of memory)**: Reduce batch size, enable gradient checkpointing, use LoRA, or switch to a smaller model variant.
- **WER not improving**: Check data quality — even a few mis-transcribed training examples can derail training. Audit samples manually.
- **Model outputs Arabic text instead of Lisan-ud-Dawat**: The language token or decoder forced output may be pulling toward Arabic. Check `forced_decoder_ids` configuration.
- **CTC loss is NaN**: Often caused by vocabulary mismatch — a character in a transcript that is not in the vocabulary. Re-audit vocabulary construction.
- **Overfitting (val WER rises while train WER falls)**: Add dropout, use LoRA with smaller rank, freeze more layers, or collect more data.
- **Whisper hallucination in silence**: Add `no_speech_threshold=0.6` and `logprob_threshold=-1.0` to generation config.

## Outputs

- A fine-tuned model checkpoint saved locally (and optionally on HuggingFace Hub)
- WER/CER metrics on the test set
- An inference pipeline ready for integration into the transcription tool
- An error analysis report guiding the next data collection round

## Cross-references

- [ASR for Low-Resource Languages](../concepts/asr_for_low_resource_languages.md)
- [Data Collection for a New Language](data_collection_for_new_language.md)
- [OpenAI Whisper](../entities/whisper.md)
- [Meta MMS Model](../entities/mms_model.md)
- [wav2vec 2.0 / XLSR](../entities/wav2vec.md)
- [Transcription Tool Options](../artifacts/transcription_tool_options.md)
