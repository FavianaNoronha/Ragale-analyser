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