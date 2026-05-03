# Lisan-ud-Dawat Script

> Summary: Lisan-ud-Dawat uses a modified Perso-Arabic script written right-to-left, adapted to represent Indo-Aryan phonemes absent in Arabic, with a rich diacritic system critical for correct pronunciation.

## What It Is

The Lisan-ud-Dawat writing system is a variant of the Perso-Arabic script — the same family used for Arabic, Persian, Urdu, and Sindhi — but with community-specific adaptations to encode sounds from the Gujarati phonological inventory. Within the Bohra community it is sometimes called simply the **Dawat script** or referred to as the **Lisan-ud-Dawat script**.

Because the language has an Indo-Aryan grammatical base but an Arabic-derived script, significant orthographic conventions have developed over centuries to bridge the gap between Arabic phonology (which the script was designed for) and Gujarati phonology (which the language also requires).

## Script Family and Directionality

| Property | Value |
|---|---|
| Script family | Perso-Arabic (abjad) |
| Directionality | Right-to-left (RTL) |
| Typology | Consonantal alphabet (abjad) — vowels optionally marked |
| Unicode block | Arabic (U+0600–U+06FF) and Arabic Presentation Forms |
| Similar scripts | Urdu Nastaliq, Arabic Naskh, Sindhi script |

## Core Characters

The base alphabet draws from the standard 28 Arabic letters, augmented by the 4 Persian additions (پ چ ژ گ), giving a foundation of 32 characters — the same as the Urdu alphabet. However, LuD uses a **Naskh** style (the standard printed Arabic style) more often than the **Nastaliq** style used for Urdu. <!-- unverified: style usage may vary by publication and era -->

## Adaptations for Gujarati Sounds

This is the most distinctive feature of the LuD script. Gujarati has several phonemes that do not exist in Arabic or Persian, requiring special orthographic solutions:

### Aspirated Consonants
Gujarati distinguishes aspirated from unaspirated stops (e.g., /p/ vs /pʰ/, /b/ vs /bʱ/). Arabic has no aspiration contrast. LuD conventionally marks aspiration by following the consonant with a **هَ** (*ha* with fatha) or by a diacritic convention. <!-- unverified: exact convention may vary by text and era -->

| Gujarati sound | Approximate LuD representation |
|---|---|
| پھ /pʰ/ | پھ (pa + ha) |
| بھ /bʱ/ | بھ (ba + ha) |
| تھ /tʰ/ | تھ (ta + ha) |
| دھ /dʱ/ | دھ (da + ha) |
| کھ /kʰ/ | کھ (ka + ha) |
| گھ /ɡʱ/ | گھ (ga + ha) |

### Retroflex Consonants
Retroflex consonants (/ʈ/, /ɖ/, /ɳ/, /ɽ/) are characteristic of Indo-Aryan languages. LuD script represents these using:
- Standard Arabic ط (emphatic T) and ض (emphatic D) may be repurposed or distinguished by context
- A subscript dot or nuqta under ن for retroflex nasal /ɳ/ — similar to Urdu's conventions
- ڑ (ra with subscript dot) for the retroflex flap /ɽ/ — borrowed from Urdu orthographic convention <!-- unverified: LuD-specific conventions may differ from Urdu -->

### The Nuqta System
LuD shares with Urdu and Sindhi the use of a **nuqta** (subscript dot) to create new characters from base Arabic letters. This is used to distinguish:
- Arabic /q/ (ق) from a Gujarati-influenced /k/ realization
- Various dental vs. retroflex pairs

## Diacritics

LuD texts — especially religious texts and the *waaz* transcripts — typically include a full set of diacritical marks (*tashkeel* / *harakat*) that Arabic calligraphy uses to mark short vowels. This is significant because:

1. **Short vowels are phonemic** in LuD (inherited from Arabic vocabulary)
2. **Correct recitation** of religious texts depends on diacritics
3. **Disambiguation**: Without diacritics, many words would be ambiguous (root consonants are shared among multiple words)

The diacritics used include:

| Diacritic | Arabic name | Function |
|---|---|---|
| َ (fatha) | Fat-ha | Short /a/ vowel |
| ِ (kasra) | Kasra | Short /i/ vowel |
| ُ (damma) | Damma | Short /u/ vowel |
| ً (tanwin fath) | Tanwin | Nunation — /an/ ending |
| ْ (sukun) | Sukun | No vowel (consonant cluster marker) |
| ّ (shadda) | Shadda | Gemination (consonant doubling) |
| ٰ (superscript alef) | Alef khanjariyya | Long /aː/ (rare) |
| ۡ (Quranic pause mark) | Sajda/waqf marks | Recitation pause (in Quranic quotations) |

**Critical for ASR/TTS systems**: LuD texts are often *fully vocalized* (all diacritics present) in religious documents, especially waaz transcripts published by the Da'wa. This is an advantage — it reduces grapheme-to-phoneme ambiguity — but also a computational challenge because diacritic recognition must be accurate.

## Ligatures and Presentation Forms

Like all Arabic-script languages, LuD text uses **contextual ligature forms** — characters change shape depending on whether they appear at the start, middle, end, or isolated position in a word. Standard Arabic OpenType fonts handle most of this automatically, but:

- Some LuD-specific character combinations may not be covered by all Arabic fonts
- Historically printed LuD texts (pre-digital) may use calligraphic forms requiring OCR-specific training
- The **lam-alif** ligature (لا) is mandatory in standard Arabic and applies in LuD as well

## Special Characters and Extensions

Some LuD texts include characters or marks not standard in Arabic:

- **Quranic annotation marks** (e.g., *maddah* for long /aː/, *hamza* variants) are common because the waaz genre heavily quotes the Quran
- **Persian-style tanvin** forms for Persianate grammatical endings
- Community-specific abbreviations for common phrases (e.g., *sallallahu alayhi wa sallam*, *alayhi al-salam*)

## Keyboard and Digital Input

LuD does not have a dedicated Unicode keyboard layout. Writers typically use:

- **Arabic keyboard layouts** (Windows Arabic, macOS Arabic) — covers most base characters
- **Urdu keyboard layouts** — better for aspirated and retroflex characters (Phonetic Urdu layout)
- Custom community software or input methods <!-- unverified: specific tools unknown -->

The Dawat-e-Hadiyah (the Bohra religious organization's official body) has digitized significant amounts of LuD text, but the tools and formats used internally are not publicly documented. <!-- unverified -->

## Orthographic Variation Across Eras

**Medieval/early manuscripts**: Handwritten Naskh; may use older Arabic orthographic conventions; minimal or no diacritics.

**19th–early 20th century printed texts**: Lithograph printing common in Gujarat; dense diacritics; calligraphic conventions.

**Modern printed texts (post-1970s)**: Typeset using Arabic typefaces; diacritics present in religious texts.

**Digital era (1990s–present)**: Mix of formats — some use Unicode Arabic correctly, some use legacy encodings, some are scanned PDFs of older prints. This heterogeneity is a major challenge for any digital corpus work.

## OCR Challenges

Optical Character Recognition (OCR) for LuD is extremely challenging because:
1. Diacritics sit above/below base characters and must be associated correctly
2. LuD uses characters from Arabic, Persian, and Indo-Aryan extensions — no single OCR model covers all
3. Older texts use calligraphic forms that differ significantly from modern typeset
4. No publicly available LuD-specific OCR model exists as of the last known survey <!-- unverified -->

## Common Misunderstandings

- **"You can just use an Arabic font"**: Standard Arabic fonts do not always include the aspirated/retroflex extensions used in LuD.
- **"Diacritics are optional like in modern Arabic"**: In LuD religious texts, diacritics are considered mandatory for accurate recitation — they are not decorative or optional.
- **"The script is the same as Urdu Nastaliq"**: LuD predominantly uses Naskh style; Nastaliq is Urdu's predominant calligraphic style. They are different typographic forms.

## Examples

A sample word showing diacritics in a LuD religious context:

> **اَلْحَمْدُ لِلّٰهِ** — "Al-hamdu lillah" (Praise be to God)

This Quranic phrase, also used in LuD, carries full diacritics in printed LuD texts. Every vowel and consonant cluster marker is explicit.

A word with a Gujarati aspirated stop:

> **پھول** — "phool" (flower) — the پھ represents the aspirated /pʰ/ sound absent in Arabic

## Cross-references

- [Lisan-ud-Dawat](lisan_ud_dawat.md)
- [Dawoodi Bohra Community](../entities/dawoodi_bohra_community.md)
- [Lisan-ud-Dawat Resources](../references/lisan_ud_dawat_resources.md)
