# Quick Start Guide - Ragale Analyzer

## Installation

No installation needed! Just Python 3.6+

```bash
cd /workspaces/Ragale-analyser
```

## 3 Ways to Use the Analyzer

### Method 1: Interactive Mode (Easiest)

```bash
python3 ragale_analyzer.py
```

Then paste your 4-line Ragale poem when prompted:

```
Enter your Ragale poem (4 lines, press Enter twice when done):

ಕರಣಕ್ಕೆ ಕೈಕೊಂಡು ಹರಿವಂದು ನಂಬಿದೆನೆ
ಮರಣವನ್ನು ನೆಗೆಳದ ದೈವದನ್ನು ಪೇಳಿದೆನೆ
ಕರುಣಾಕರ ಪರಮೇಶ್ವರ ಕಾಪಾಡುದೆನ್ನ ಬನ್ನಿಸಿದು
ತರುಣದಲಿ ನಿರ್ವಿಕಾರ ಹೃದಯದಲಿ ತೊಂಡಿಸಿದಿರಬೆಂದು

[Press Enter]
```

You'll get a detailed analysis report!

### Method 2: Analyze a File

Create a text file with your poem:

```bash
cat > my_ragale.txt << 'EOF'
ಭಕ್ತಿಯಿಂದ ಭಗವಂತನ ಪಾದವ ಪೂಜಿಸಿದನು
ಮುಕ್ತಿಗಾಗಿ ಮನದೊಳಗೆ ಪ್ರಾರ್ಥಿಸಿದನು
ಶಕ್ತಿಯುತ ಮಹಾದೇವನ ನಾಮವ ಸ್ಮರಿಸಿದನು ಅವನು
ಭಕ್ತಿಯೆಂಬ ಮಾರ್ಗದಲ್ಲಿ ನಡೆದನು ನಿತ್ಯವು ನಿರಂತರವು
EOF
```

Then analyze it:

```bash
python3 ragale_analyzer.py my_ragale.txt
```

### Method 3: Python API (For Developers)

Create a Python script:

```python
from ragale_analyzer import RagaleAnalyzer

# Your poem
poem = """
ನಮ್ಮ ದೇಶದ ಮಹಿಮೆಯು ಜಗದಿ ಪ್ರಸಿದ್ಧವು
ಸಮ್ಮಣೆಯು ಬಂದಿಹುದು ಎಲ್ಲಾ ದಿಕ್ಕಿನಿಂದ
ಸಂಸ್ಕೃತಿಯು ಸಂಪ್ರದಾಯವು ನಮ್ಮದೆ ಹಳೆಯದಾಗಿದೆ
ಹೆಮ್ಮೆಯಿಂದ ನಾವು ಹೇಳುವೆವು ಭಾರತೀಯರು ಎಂದೆಂದು
"""

# Create analyzer
analyzer = RagaleAnalyzer(strict_mode=True)

# Analyze
result = analyzer.analyze_poem(poem)

# Check if valid
if result.is_valid:
    print("✓ Valid Ragale!")
else:
    print("✗ Not valid Ragale")
    for error in result.errors:
        print(f"  Error: {error}")

# Print full report
report = analyzer.format_report(result, poem)
print(report)
```

## Try the Demo

Quick demonstration:

```bash
python3 demo.py
```

This shows:
- Syllable counting examples
- Analysis of sample poems
- Full report generation

## Run Tests

See the analyzer in action with multiple test cases:

```bash
python3 test_examples.py
```

Tests include:
- Syllable counting accuracy
- Valid Ragale examples
- Invalid examples (wrong syllable count, no rhyme)

## Understanding the Output

### Valid Ragale Output

```
Status: ✓ VALID RAGALE

SYLLABLE COUNT ANALYSIS:
Line 1: 12 syllables (expected 12) ✓
Line 2: 12 syllables (expected 12) ✓
Line 3: 16 syllables (expected 16) ✓
Line 4: 16 syllables (expected 16) ✓

RHYME SCHEME ANALYSIS:
Pattern: AABB
Lines 1-2 rhyme: ✓ Yes (endings: 'ನು' vs 'ನು')
Lines 3-4 rhyme: ✓ Yes (endings: 'ದು' vs 'ದು')
```

### Invalid Ragale Output

```
Status: ✗ NOT VALID RAGALE

ERRORS:
✗ Line 1: Expected 12 syllables, found 10 (-2)
✗ Lines 1 and 2 do not rhyme (endings: ನು vs ದೆ)

SUGGESTIONS:
💡 Check syllable counting, especially:
💡   - Conjunct consonants (should not add extra syllables)
💡   - Ottu/gunita (double consonants)
💡 Ensure lines 1-2 end with same sound
```

## Tips for Success

### 1. Count Syllables Carefully

Remember:
- `ಪ್ರೇಮ` = 2 syllables (ಪ್ರೇ + ಮ), not 3
- `ಭಕ್ತಿ` = 2 syllables (ಭಕ್ + ತಿ), not 3
- `ಕರುಣಾಮಯ` = 5 syllables (ಕ + ರು + ಣಾ + ಮ + ಯ)

Conjunct consonants (ಕ್ರ, ಪ್ರ, etc.) don't add syllables!

### 2. Match Rhymes

Lines 1-2 must end with the same sound:
```
Line 1: ...ನು
Line 2: ...ನು  ✓ Good!
```

Lines 3-4 must end with the same sound:
```
Line 3: ...ದು
Line 4: ...ದು  ✓ Good!
```

### 3. Follow the Pattern

Standard Ragale:
- Line 1: 12 syllables
- Line 2: 12 syllables
- Line 3: 16 syllables
- Line 4: 16 syllables

### 4. Use Flexible Mode for Learning

If you're practicing and want some tolerance:

```python
analyzer = RagaleAnalyzer(strict_mode=False)  # Allows ±1 syllable
```

## Common Mistakes

❌ **Wrong**: Using different endings for paired lines
```
Line 1: ...ನು
Line 2: ...ದೆ  ← Different ending!
```

❌ **Wrong**: Miscounting conjunct consonants
```
ಪ್ರೇಮ = 3?  ← No! It's 2 syllables
```

❌ **Wrong**: Not having exactly 4 lines
```
Only 3 lines... ← Need exactly 4
```

✅ **Right**: Proper structure
```
Line 1: 12 syllables, ends with ನು
Line 2: 12 syllables, ends with ನು ✓
Line 3: 16 syllables, ends with ದು
Line 4: 16 syllables, ends with ದು ✓
```

## Sample Poems

See [sample_poems.txt](sample_poems.txt) for ready-to-test examples!

## Learn More

- **[Ragale_Rules.md](Ragale_Rules.md)** - Deep dive into Ragale prosody
- **[README_ANALYZER.md](README_ANALYZER.md)** - Complete API documentation
- **[README.md](README.md)** - Project overview

## Need Help?

1. Read [Ragale_Rules.md](Ragale_Rules.md) for detailed rules
2. Try the examples in [sample_poems.txt](sample_poems.txt)
3. Run `python3 demo.py` to see it in action
4. Use debug mode to see syllable breakdown:

```python
from ragale_analyzer import KannadaSyllableCounter

counter = KannadaSyllableCounter()
counter.debug = True  # Shows detailed analysis
count = counter.count_syllables("ಪ್ರೇಮ")
```

## Ready to Start?

```bash
# Try it now!
python3 ragale_analyzer.py
```

Happy composing! 🎭📝

---

**ಓಂ ಶ್ರೀ ಗುರುಭ್ಯೋ ನಮಃ**
