<<<<<<< HEAD
# Ragale Analyser (ರಾಗಳೆ ವೈಶ್ಲೇಷಕ)

A tool to analyse classical Kannada Ragale (ರಾಗಳೆ) poetry — validating matra counts, yati (caesura), rhyme (prāsa), and identifying Ragale types.

---

## 📜 What is Ragale?

**Ragale** is a classical Kannada metrical (chandas) form based on **matras (ಮಾತ್ರೆ)** — the unit of syllabic weight — rather than syllable count or rhyme. It is one of the most flexible and widely used meters in classical and Bhakti Kannada poetry, used by poets like Basavanna, Akka Mahadevi, Allama Prabhu, and Harihara.

---

## ⚖️ Matra (ಮಾತ್ರೆ) — The Core Unit

The entire Ragale system revolves around **matra count**:

| Syllable Type | Matra Value |
|---|---|
| Short vowel (hrasva svara: ಉತ್ತರ, ಇ, ಉ, ಋ) | **1 matra** |
| Long vowel (dīrgha svara: ಆ, ಈ, ಓ, ಏ, ಐ, ಔ) | **2 matras** |
| Consonant with short vowel | **1 matra** |
| Consonant with long vowel | **2 matras** |
| Anusvara (ಂ) / Visarga (ಃ) following a syllable | **+1 matra** (position-sensitive) |
| Conjunct consonants (ottakshara) at start of a foot | **1 matra** |

---

## 📐 Fundamental Structural Rules

1. **Fixed matra count per line (pāda)**: Every line must have exactly the prescribed number of matras for that Ragale type.
2. **Uniformity**: All lines in a stanza follow the same matra count — no exceptions.
3. **No mandatory rhyme**: Ragale does NOT require end-rhyme. Focus is on matra rhythm.
4. **Stanza size**: Usually **4 lines (catushpadi)** per stanza.
5. **Yati (ಯತಿ) / Caesura**: Many Ragale types have a prescribed internal pause within a line, splitting the line into two halves.

---

## 🏷️ Types of Ragale & Their Rules

### 🔹 Lalita Ragale (ಲಲಿತ ರಾಗಲೇ)
- **Matras per line**: 8
- **Yati**: After 4th matra (split: 4 + 4)
- **Lines per stanza**: 4
- Lightest and simplest Ragale — ideal for lyrical, gentle emotions.

### 🔹 Lata Ragale (ಲತಾ ರಾಗಲೇ)
- **Matras per line**: 10
- **Yati**: After 5th matra (split: 5 + 5)
- **Lines per stanza**: 4
- Slightly more elaborate, used for flowing narrative.

### 🔹 Mandanila Ragale (ಮಂದಾನಿಲ ರಾಗಲೇ)
- **Matras per line**: 12
- **Yati**: After 6th matra (split: 6 + 6)
- **Lines per stanza**: 4
- Medium weight; used for philosophical and devotional themes.

### 🔹 Utsāha Ragale (ಉತ್ಸಾಹ ರಾಗಲೇ)
- **Matras per line**: 16
- **Yati**: After 8th matra (split: 8 + 8)
- **Lines per stanza**: 4
- Heaviest standard Ragale; used for heroic, elevated, or deeply spiritual content.

### 📊 Summary Table

| Type | Matras/Line | Yati Split | Lines/Stanza |
|---|---|---|---|
| Lalita | 8 | 4 + 4 | 4 |
| Lata | 10 | 5 + 5 | 4 |
| Mandanila | 12 | 6 + 6 | 4 |
| Utsāha | 16 | 8 + 8 | 4 |

---

## 🔁 Rhyme in Ragale — Special Notes

Although **end-rhyme is NOT a strict rule**, Ragale poems may incorporate:

- **Prāsa (ಪ್ರಾಸ)**: Alliteration at the **second letter** of each line — a common ornamental device.
- **Anuprāsa**: Repetition of consonant sounds for euphony.
- **Internal rhythm**: Controlled by the yati and matra pattern.

### For a Rhyme Analyser, check:
1. **End-syllable matching** across lines (optional but present in many works).
2. **Second-letter consonant alliteration (dvitīyākshara prāsa)** — very common in classical Kannada.
3. **Matra-count correctness** — the primary validator.

---

## 🧮 Analysis Algorithm

How to analyse a Kannada line for Ragale compliance:

```
1. Tokenize the line into syllables (akshara)
2. For each syllable:
   a. Identify the vowel component (hrasva = 1, dīrgha = 2)
   b. Check for anusvara/visarga → +1 if present
3. Sum all matra values
4. Check if sum == expected matras for the Ragale type
5. Check yati: verify matra count at the split point
6. (Optional) Check prāsa: compare 2nd consonant of each line
```

---

## 📝 Example — Lalita Ragale (8 matras per line)

```
ಒಂದು ಮಾತು ಬರೆದನು
ಮಾನವನು ಮನಸಲ್ಲಿ
ಹೃದಯದಲ್ಲಿ ಹುರಿದು
ಬಾಳಿಗೂ ಬೆಳಕಾಗಿ
```

Each line maintains 8 matras with a yati after the 4th matra.

---

## 🛠️ Features (Planned / Implemented)

- [ ] Kannada Unicode syllable tokenizer (handling matras, ottakshara, anusvara, visarga)
- [ ] Matra counter per syllable
- [ ] Line matra validator (checks against all 4 Ragale types)
- [ ] Yati checker (validates the internal pause position)
- [ ] Prāsa / Rhyme detector (dvitīyākshara prāsa and end-rhyme)
- [ ] Ragale type identifier (auto-detect which type based on matra count)
- [ ] Full poem analyser (validates all lines in a stanza)

---

## 📚 References

- Kannada Sahitya Vishwakosha, Government of Karnataka
- *Kannada Chandassu* by C. K. Nagaraja Rao
- Classical works on Kannada prosody (chandassu)

---

## 🤝 Contributing

Contributions are welcome! Please open an issue or pull request for any improvements, bug fixes, or new features.

---

## 📄 License

This project is open source. See [LICENSE](LICENSE) for details.
=======
# Ragale Analyzer

## Overview

**Ragale Analyzer** is a Python-based tool for validating Kannada poems against traditional Ragale meter rules. It provides comprehensive analysis of syllable counts, rhyme schemes, and adherence to classical Kannada prosody (chandas).

Ragale is one of the most important metrical forms in Kannada poetry, characterized by its 12-12-16-16 syllable pattern and specific rhyme schemes. This tool helps poets, students, and literature enthusiasts validate their compositions.

## Features

- ✅ **Accurate Syllable Counting**: Follows traditional Kannada prosody rules
- ✅ **Rhyme Scheme Analysis**: Validates Prāsa patterns (AABB, AAAA, AABA, ABAB)
- ✅ **Meter Validation**: Checks standard 12-12-16-16 pattern and variations
- ✅ **Detailed Feedback**: Provides errors, warnings, and suggestions
- ✅ **Multiple Modes**: Strict and flexible validation
- ✅ **No Dependencies**: Pure Python, no external packages needed

## Quick Start

### 1. View Ragale Rules

Learn about Ragale prosody in detail:
```bash
cat Ragale_Rules.md
```

See [Ragale_Rules.md](Ragale_Rules.md) for comprehensive documentation on:
- Syllable counting rules (Akṣara Gaṇane)
- Rhyme schemes (Prāsa)
- Rhythm patterns (Gati)
- Caesura placement (Yati)
- And much more!

### 2. Run the Analyzer

**Interactive mode:**
```bash
python3 ragale_analyzer.py
```

**Analyze a file:**
```bash
python3 ragale_analyzer.py my_poem.txt
```

**Run demo:**
```bash
python3 demo.py
```

**Run tests:**
```bash
python3 test_examples.py
```

### 3. Use in Your Code

```python
from ragale_analyzer import RagaleAnalyzer

poem = """
ಕರಣಕ್ಕೆ ಕೈಕೊಂಡು ಹರಿವಂದು ನಂಬಿದೆನೆ
ಮರಣವನ್ನು ನೆಗೆಳದ ದೈವದನ್ನು ಪೇಳಿದೆನೆ
ಕರುಣಾಕರ ಪರಮೇಶ್ವರ ಕಾಪಾಡುದೆನ್ನ ಬನ್ನಿಸಿದು
ತರುಣದಲಿ ನಿರ್ವಿಕಾರ ಹೃದಯದಲಿ ತೊಂಡಿಸಿದಿರಬೆಂದು
"""

analyzer = RagaleAnalyzer(strict_mode=True)
result = analyzer.analyze_poem(poem)

print(f"Valid: {result.is_valid}")
print(f"Syllables: {result.syllable_counts}")
print(f"Rhyme pattern: {result.rhyme_analysis['pattern']}")

# Generate full report
report = analyzer.format_report(result, poem)
print(report)
```

## Project Structure

```
Ragale-analyser/
├── README.md                   # This file - project overview
├── Ragale_Rules.md            # Detailed Ragale prosody rules (read this first!)
├── README_ANALYZER.md         # Analyzer API documentation
├── ragale_analyzer.py         # Main analyzer code
├── test_examples.py           # Test suite with examples
├── demo.py                    # Quick demonstration script
└── sample_poems.txt           # Sample Ragale poems for testing
```

## What is Ragale?

Ragale (ರಗಳೆ) is a classical Kannada meter characterized by:

1. **Four-line stanzas** (padya)
2. **Syllable pattern**: 12-12-16-16
	 - Lines 1-2: 12 syllables each
	 - Lines 3-4: 16 syllables each
3. **Rhyme scheme**: Lines 1-2 rhyme, Lines 3-4 rhyme (AABB pattern typically)
4. **Yati (Caesura)**:
	 - 12-syllable lines: pause after 6th syllable (6+6)
	 - 16-syllable lines: pause after 8th syllable (8+8)
5. **Gati (Rhythm)**: Balance of laghu (light) and guru (heavy) syllables

### Example Ragale:

```
ಕರಣಕ್ಕೆ ಕೈಕೊಂಡು || ಹರಿವಂದು ನಂಬಿದೆನೆ     (12 syllables)
ಮರಣವನ್ನು ನೆಗೆಳದ || ದೈವದನ್ನು ಪೇಳಿದೆನೆ     (12 syllables)
ಕರುಣಾಕರ ಪರಮೇಶ್ವರ || ಕಾಪಾಡುದೆನ್ನ ಬನ್ನಿಸಿದು    (16 syllables)
ತರುಣದಲಿ ನಿರ್ವಿಕಾರ || ಹೃದಯದಲಿ ತೊಂಡಿಸಿದಿರಬೆಂದು  (16 syllables)
```

**Rhyme**: Lines 1-2 end with "ನೆ", Lines 3-4 end with "ದು" ✓

## How the Analyzer Works

### Syllable Counting

The analyzer counts syllables according to Kannada prosody rules:

- **Independent vowels** (ಅ, ಆ, ಇ, etc.) = 1 syllable
- **Consonant + vowel** = 1 syllable
- **Conjunct consonants** (ಕ್ರ, ಪ್ರ, etc.) =part of one syllable
- **Virama/Halant** (್) = does not add syllable
- **Anusvara** (ಂ) and **Visarga** (ಃ) = part of previous syllable

Example:
- `ಪ್ರೇಮ` = 2 syllables (ಪ್ರೇ + ಮ)
- `ಭಕ್ತಿ` = 2 syllables (ಭಕ್ + ತಿ)
- `ಕರುಣಾಮಯ` = 5 syllables (ಕ + ರು + ಣಾ + ಮ + ಯ)

### Rhyme Detection

The analyzer checks if lines rhyme by comparing their ending sounds:

- Lines 1-2 must have same ending (2-3 characters)
- Lines 3-4 must have same ending
- Supports patterns: AABB (standard), AAAA, AABA, ABAB

### Validation Modes

**Strict Mode** (`strict_mode=True`):
- Exact syllable count required
- All rules must be followed

**Flexible Mode** (`strict_mode=False`):
- Allows ±1 syllable variation
- More forgiving for modern compositions

## Sample Output

```
======================================================================
RAGALE ANALYSIS REPORT
======================================================================

Status: ✓ VALID RAGALE

POEM:
----------------------------------------------------------------------
1. ಕರಣಕ್ಕೆ ಕೈಕೊಂಡು ಹರಿವಂದು ನಂಬಿದೆನೆ
2. ಮರಣವನ್ನು ನೆಗೆಳದ ದೈವದನ್ನು ಪೇಳಿದೆನೆ
3. ಕರುಣಾಕರ ಪರಮೇಶ್ವರ ಕಾಪಾಡುದೆನ್ನ ಬನ್ನಿಸಿದು
4. ತರುಣದಲಿ ನಿರ್ವಿಕಾರ ಹೃದಯದಲಿ ತೊಂಡಿಸಿದಿರಬೆಂದು

SYLLABLE COUNT ANALYSIS:
----------------------------------------------------------------------
Line 1: 12 syllables (expected 12) ✓
Line 2: 12 syllables (expected 12) ✓
Line 3: 16 syllables (expected 16) ✓
Line 4: 16 syllables (expected 16) ✓

RHYME SCHEME ANALYSIS:
----------------------------------------------------------------------
Pattern: AABB
Expected patterns: AABB, AAAA, AABA, ABAB
Lines 1-2 rhyme: ✓ Yes (endings: 'ನೆ' vs 'ನೆ')
Lines 3-4 rhyme: ✓ Yes (endings: 'ದು' vs 'ದು')

======================================================================
```

## Documentation

- **[Ragale_Rules.md](Ragale_Rules.md)** - Complete guide to Ragale prosody
	- History and types of Ragale
	- 8 detailed rules with examples
	- Practice exercises
	- Composition guidelines
  
- **[README_ANALYZER.md](README_ANALYZER.md)** - Analyzer usage guide
	- API reference
	- Configuration options
	- Troubleshooting
	- Advanced usage

- **[sample_poems.txt](sample_poems.txt)** - Example poems for testing

## Use Cases

- **Poets**: Validate your Ragale compositions before publication
- **Students**: Learn Ragale meter and practice composition
- **Scholars**: Analyze classical Kannada literature
- **Educators**: Teaching tool for Kannada prosody classes
- **Applications**: Integrate into Kannada poetry tools and apps

## Requirements

- Python 3.6 or higher
- No external dependencies!

## Contributing

Contributions welcome! Areas for improvement:

- More accurate syllable counting edge cases
- Gati (laghu-guru) pattern analysis
- Support for more Ragale variations
- Web interface
- More test examples from classical literature

## Cultural Significance

Ragale has been a cornerstone of Kannada poetry since the 12th century. Notable works:

- **Ragaḷēgaḷa Paṅkti** - Harihara (who perfected the form)
- **Girija Kalyāṇa** - Harihara
- **Jaimini Bhārata** - Lakshmisha
- Countless devotional and narrative poems

This analyzer helps preserve and promote this rich literary tradition.

## License

This project is provided for educational and cultural preservation purposes.

---

**ಓಂ ಶ್ರೀ ಗುರುಭ್ಯೋ ನಮಃ**

*May this tool help preserve and promote the beautiful tradition of Kannada Ragale poetry.*
# Ragale-analyser
>>>>>>> c559b18 (Add Ragle analyser files and updated README)
