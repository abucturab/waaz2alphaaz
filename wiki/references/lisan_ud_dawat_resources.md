# Lisan-ud-Dawat Resources

> Summary: An annotated catalog of academic papers, corpora, NLP tools, online resources, and community publications relevant to Lisan-ud-Dawat and the Dawoodi Bohra community.

## Location

Resources are distributed across academic databases, community websites, and internal organizational archives. No single consolidated corpus or resource portal exists as of the last known survey.

## Academic & Linguistic Resources

### 1. Wikipedia — Lisan al-Dawat
- **URL**: https://en.wikipedia.org/wiki/Lisan_al-Dawat
- **What it contains**: Overview article covering definition, script, history, and community context. Useful as an entry point but thin on linguistic detail.
- **Quality**: Moderate; citations present but article is not comprehensive.

### 2. Ethnologue
- **URL**: https://www.ethnologue.com
- **What it contains**: Ethnologue's language database. <!-- unverified: LuD may or may not have an ISO 639-3 code entry; search "Lisan al-Dawat" or "Dawoodi Bohra" -->
- **Notes**: As of last check, LuD may not have a standalone ISO 639-3 entry. It may be listed under Gujarati varieties or not at all. **Needs verification.**

### 3. Glottolog
- **URL**: https://glottolog.org
- **What it contains**: Linguistic genealogy database. <!-- unverified: LuD classification status unknown -->
- **Notes**: Glottolog classifies endangered and minority languages. LuD's status there is uncertain — **needs investigation**.

### 4. "The Bohras" — scholarly works on the community
- Several academic books cover Dawoodi Bohra history and sociology; some include linguistic notes:
  - *The Bohras* by Jonah Blank (2001) — journalistic/sociological account; some description of LuD
  - Works by Farhad Daftary on Ismaili history (*The Ismailis: Their History and Doctrines*) — historical context but limited linguistic focus
  - Celia Kerslake and others in the field of Islamic linguistic studies <!-- unverified: specific papers on LuD are rare -->

### 5. Journal of Semitic Studies / Journal of the American Oriental Society
- **Relevance**: Occasional papers on Fatimid Arabic and Ismaili religious texts may touch on LuD precursors
- **Status**: No dedicated LuD linguistics paper has been confirmed in these journals — **needs investigation**

### 6. PhD Dissertations
- Some doctoral work on Bohra communities touches on language use:
  - Dissertations in South Asian Studies, Islamic Studies, or Sociolinguistics departments at universities in India, UK, or USA <!-- unverified: specific titles unknown — needs ProQuest/DART-Europe search -->
- **Gap**: No dissertation focused specifically on LuD phonology, morphology, or computational processing has been identified.

## NLP & Computational Resources

### 7. No Dedicated LuD NLP Corpus (as of 2026)
There is **no publicly available LuD text or audio corpus** for NLP/ASR purposes. This is the central resource gap for this project.

### 8. Arabic NLP Tools (Partial Applicability)
LuD's script and a large portion of its vocabulary are Arabic-derived. Arabic NLP tools that may have partial utility:
- **Farasa** (QCRI): Arabic segmenter and POS tagger — https://farasa.qcri.org/
- **CAMeL Tools** (NYU Abu Dhabi): Arabic morphological analysis — https://github.com/CAMeL-Lab/camel_tools
- **Madamira / CALIMA**: Arabic morphological disambiguators
- **OpenNMT Arabic models**: Machine translation models

**Limitation**: These tools are built for Modern Standard Arabic or dialectal Arabic. They will handle Arabic-vocabulary words in LuD but will fail on Gujarati-grammar portions, inflected forms, and LuD-specific constructions.

### 9. Gujarati NLP Tools (Partial Applicability)
LuD's grammar is Gujarati-based. Gujarati NLP tools:
- **iNLTK**: https://inltk.readthedocs.io — includes Gujarati language model
- **IndicNLP Library** (AI4Bharat): https://indicnlp.ai4bharat.org — covers Gujarati
- **IndicTrans** (AI4Bharat): Machine translation for Indian languages including Gujarati

**Limitation**: These tools use Gujarati in the Devanagari or native Gujarati script, not in Perso-Arabic script. Script conversion would be required, and mixed-language content is not handled.

### 10. Whisper (OpenAI) — Generic ASR
- **URL**: https://github.com/openai/whisper
- **Relevance**: OpenAI's Whisper has been trained on Arabic and can produce partial transcriptions of Arabic-heavy speech. For LuD waaz content, Whisper will perform reasonably on Arabic vocabulary items but poorly on Gujarati-grammar sections and LuD-specific words.
- **Use case for this project**: May serve as a baseline/first-pass model; fine-tuning on LuD audio would be required.

### 11. MMS (Meta Massively Multilingual Speech)
- **URL**: https://github.com/facebookresearch/fairseq/tree/main/examples/mms
- **Relevance**: Meta's MMS project covers thousands of languages including many low-resource ones. <!-- unverified: LuD coverage is uncertain — needs verification -->
- **Notes**: If LuD is not covered, MMS's base models may still offer a starting point for fine-tuning.

### 12. wav2vec2 / HuBERT
- **Relevance**: Self-supervised speech models that can be fine-tuned with small amounts of labeled audio. Given LuD's resource scarcity, these architectures are the most viable path to a working ASR system.
- **Key papers**: wav2vec 2.0 (Baevski et al., 2020); HuBERT (Hsu et al., 2021)

## Community Digital Resources

### 13. Dawat-e-Hadiyah Official Website
- **URL**: https://www.fatimidawat.com <!-- unverified: URL may vary; search "Dawat-e-Hadiyah" -->
- **What it contains**: Official communications, event announcements, and some published waaz transcripts in LuD. These transcripts, if accessible, are among the only structured LuD text data available.
- **Access**: Some content is publicly accessible; some requires community membership login.

### 14. Al-Jamea-tus-Saifiyah
- **URL**: https://www.aljamea.com <!-- unverified -->
- **What it contains**: The Bohra religious university's publications; some academic-style materials in LuD. Primary source for LuD literary and religious texts.
- **Access**: Primarily community-internal.

### 15. Waaz Audio Recordings (Community Platforms)
- The Dawoodi Bohra community distributes waaz audio through:
  - Official Dawat apps and websites
  - YouTube channels (partial — some are community-restricted)
  - Telegram groups and WhatsApp communities within the Bohra network
- **For ASR training**: These recordings are the primary data source for the waaz2alphaaz project, but access requires community relationships.

### 16. Published Waaz Transcripts (Physical/PDF)
- The Da'wa has published printed transcripts of key waaz, particularly Ashara Mubaraka waaz, in the LuD script. These are distributed at Ashara gatherings.
- **Digital availability**: Some are scanned and circulated in PDF form within the community.
- **For NLP**: These constitute the best available ground-truth transcription data, but are not in a machine-readable format and would require OCR or manual transcription.

### 17. Marsiya and Qasida Collections
- Published books of Bohra religious poetry (elegies and panegyrics) in LuD. These include fully vocalized text.
- **Linguistic value**: Poetry is highly structured and often fully diacriticized — excellent for building grapheme-to-phoneme (G2P) models.

## Script and Font Resources

### 18. Arabic Unicode Block
- **URL**: https://unicode.org/charts/PDF/U0600.pdf
- **Relevance**: Core Unicode reference for Arabic script characters used in LuD.

### 19. Arabic Extended-A Block (U+08A0–U+08FF)
- **URL**: https://unicode.org/charts/PDF/U08A0.pdf
- **Relevance**: Extended Arabic characters that may be needed for LuD's Indo-Aryan phoneme representations.

### 20. Noto Naskh Arabic Font
- **URL**: https://fonts.google.com/noto/specimen/Noto+Naskh+Arabic
- **Relevance**: Open-source font with broad Arabic Unicode coverage, suitable for rendering LuD text.

## Gaps and Needs

The following resources do not exist (as of this writing) and would significantly advance LuD NLP work:

1. **A romanized (Latin-script) transcription standard for LuD** — none confirmed to exist
2. **A phoneme inventory / pronunciation dictionary** — no published LuD phoneme dictionary found
3. **A labeled speech corpus** — no LuD ASR training corpus exists publicly
4. **A morphological analyzer** — none exists; would require building from scratch given the mixed-language grammar
5. **An ISO 639-3 registration** — LuD's official linguistic status is unclear

## When to Consult

- When choosing a base model for fine-tuning ASR (sections 10–12)
- When looking for text data for language modeling (sections 13–17)
- When resolving Unicode/rendering issues (sections 18–20)
- When seeking academic background on the language or community (sections 1–6)
- When assessing the state of the art in LuD computational linguistics (sections 7–12)

## Cross-references

- [Lisan-ud-Dawat](../concepts/lisan_ud_dawat.md)
- [Lisan-ud-Dawat Script](../concepts/lisan_ud_dawat_script.md)
- [Dawoodi Bohra Community](../entities/dawoodi_bohra_community.md)
