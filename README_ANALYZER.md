# Ragale Analyzer - Usage Guide

## Overview

The Ragale Analyzer is a Python tool that validates Kannada poems against traditional Ragale meter rules. It checks syllable counts, rhyme schemes, and provides detailed feedback on conformance to Ragale prosody.

## Features

- ✅ **Syllable Counting**: Accurate syllable counting following Kannada prosody rules
- ✅ **Rhyme Analysis**: Validates rhyme schemes (Prāsa) - AABB, AAAA, AABA patterns
- ✅ **Meter Validation**: Checks standard 12-12-16-16 syllable pattern
- ✅ **Yati Analysis**: Guidance on caesura placement
- ✅ **Detailed Reports**: Comprehensive analysis with errors, warnings, and suggestions
- ✅ **Multiple Modes**: Strict mode and flexible mode (±1 syllable tolerance)

## Installation

No external dependencies required! Uses only Python standard library.

```bash
# Make the script executable
chmod +x ragale_analyzer.py

# Or run with Python
python3 ragale_analyzer.py
```

## Usage

### Method 1: Interactive Mode

Run the analyzer without arguments for interactive input:

```bash
python3 ragale_analyzer.py
```

Then enter your 4-line Ragale poem when prompted.

### Method 2: File Input

Save your poem in a text file and pass it as an argument:

```bash
python3 ragale_analyzer.py my_poem.txt
```

### Method 3: Python API

Use the analyzer in your Python code:

```python
from ragale_analyzer import RagaleAnalyzer

# Your poem text
poem = """
ಕರಣಕ್ಕೆ ಕೈಕೊಂಡು ಹರಿವಂದು ನಂಬಿದೆನೆ
ಮರಣವನ್ನು ನೆಗೆಳದ ದೈವದನ್ನು ಪೇಳಿದೆನೆ
ಕರುಣಾಕರ ಪರಮೇಶ್ವರ ಕಾಪಾಡುದೆನ್ನ ಬನ್ನಿಸಿದು
ತರುಣದಲಿ ನಿರ್ವಿಕಾರ ಹೃದಯದಲಿ ತೊಂಡಿಸಿದಿರಬೆಂದು
"""

# Create analyzer (strict_mode=True for exact validation)
analyzer = RagaleAnalyzer(strict_mode=True)

# Analyze the poem
result = analyzer.analyze_poem(poem)

# Generate formatted report
report = analyzer.format_report(result, poem)
print(report)

# Access individual results
print(f"Valid: {result.is_valid}")
print(f"Syllable counts: {result.syllable_counts}")
print(f"Rhyme pattern: {result.rhyme_analysis['pattern']}")
```

## Understanding the Output

### Sample Output

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

### Status Indicators

- ✓ = Pass/Valid
- ✗ = Fail/Invalid
- ⚠ = Warning
- 💡 = Suggestion

## Syllable Counting Rules

The analyzer follows traditional Kannada prosody rules:

1. **Independent vowels** (ಅ, ಆ, ಇ, etc.) = 1 syllable each
2. **Consonant + vowel** = 1 syllable
3. **Conjunct consonants** (ಕ್ರ, ಪ್ರ, etc.) = count as one with following vowel
4. **Virama/Halant** (್) = combines with previous syllable
5. **Anusvara** (ಂ) and **Visarga** (ಃ) = part of previous syllable

### Examples:

- `ಪ್ರೇಮ` = 2 syllables (ಪ್ರೇ + ಮ)
- `ಅರಮನೆ` = 4 syllables (ಅ + ರ + ಮ + ನೆ)
- `ಕರುಣಾಮಯ` = 5 syllables (ಕ + ರು + ಣಾ + ಮ + ಯ)
- `ಭಕ್ತಿ` = 2 syllables (ಭಕ್ + ತಿ)

## Running Tests

Test the analyzer with example poems:

```bash
python3 test_examples.py
```

This will:
1. Test syllable counting accuracy
2. Validate correct Ragale examples
3. Verify detection of invalid poems
4. Show detailed analysis reports

## Configuration Options

### Strict Mode vs. Flexible Mode

```python
# Strict mode - exact syllable count required
analyzer = RagaleAnalyzer(strict_mode=True)

# Flexible mode - allows ±1 syllable variation
analyzer = RagaleAnalyzer(strict_mode=False)
```

### Ragale Pattern Types

The analyzer supports different Ragale patterns:

```python
# Standard Ragale (12-12-16-16) - default
result = analyzer.analyze_poem(poem, expected_pattern='sadhaarana')

# Equal 12-syllable lines (12-12-12-12)
result = analyzer.analyze_poem(poem, expected_pattern='sama_12')

# Equal 14-syllable lines (14-14-14-14)
result = analyzer.analyze_poem(poem, expected_pattern='sama_14')

# Equal 16-syllable lines (16-16-16-16)
result = analyzer.analyze_poem(poem, expected_pattern='sama_16')
```

## API Reference

### RagaleAnalyzer Class

#### Methods:

- `analyze_poem(text, expected_pattern='sadhaarana')` - Analyze a poem
- `format_report(result, poem_text)` - Generate formatted report
- `parse_lines(text)` - Split poem into lines

### AnalysisResult Dataclass

Properties:
- `is_valid`: Boolean - Overall validation result
- `syllable_counts`: List[int] - Actual syllable counts for each line
- `expected_counts`: List[int] - Expected syllable counts
- `rhyme_analysis`: Dict - Rhyme scheme analysis
- `yati_analysis`: Dict - Yati/caesura analysis
- `errors`: List[str] - Validation errors
- `warnings`: List[str] - Non-critical warnings
- `suggestions`: List[str] - Improvement suggestions

### KannadaSyllableCounter Class

#### Methods:

- `count_syllables(text)` - Count syllables in text
- `get_syllable_list(text)` - Get list of individual syllables
- `extract_kannada_text(text)` - Clean and extract Kannada text

### RhymeAnalyzer Class

#### Methods:

- `check_rhyme(line1, line2)` - Check if two lines rhyme
- `get_rhyme_pattern(lines)` - Get pattern like 'AABB'
- `analyze_rhyme_scheme(lines)` - Comprehensive rhyme analysis

## Troubleshooting

### Common Issues:

**Issue**: Syllable count seems wrong
- **Solution**: Check for conjunct consonants, virama, and anusvara - they don't add syllables

**Issue**: Rhyme not detected
- **Solution**: Ensure last 2-3 characters match exactly, including vowel signs

**Issue**: "Expected 4 lines" error
- **Solution**: Ensure poem has exactly 4 non-empty lines

### Debug Mode:

Enable debug output for syllable counting:

```python
counter = KannadaSyllableCounter()
counter.debug = True
count = counter.count_syllables("ಕರಣಕ್ಕೆ")
# Will print detailed syllable analysis
```

## Examples

See `test_examples.py` for complete working examples of:
- Valid Ragale poems
- Invalid poems with various issues
- Syllable counting tests
- API usage patterns

## Contributing

To improve the analyzer:

1. Add more test examples in `test_examples.py`
2. Improve syllable counting accuracy
3. Enhance Yati (caesura) detection
4. Add Gati (laghu-guru) pattern analysis
5. Support more Ragale variations

## References

- See `Ragale_Rules.md` for detailed Ragale prosody rules
- Classical texts: Chandōmbudhi, Kavi Rahasya
- Kannada Unicode specification

## License

This tool is provided for educational and cultural preservation purposes.

---

**ಓಂ ಶ್ರೀ ಗುರುಭ್ಯೋ ನಮಃ**
