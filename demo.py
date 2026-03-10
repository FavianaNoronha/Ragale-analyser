#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Quick demo of the Ragale Analyzer
"""

from ragale_analyzer import RagaleAnalyzer, KannadaSyllableCounter

print("=" * 70)
print("RAGALE ANALYZER - QUICK DEMO")
print("=" * 70)
print()

# Demo 1: Syllable counting
print("DEMO 1: Syllable Counting")
print("-" * 70)

counter = KannadaSyllableCounter()

test_words = {
    'ಕರಣ': 3,
    'ಪ್ರೇಮ': 2,
    'ಭಕ್ತಿ': 2,
    'ಕರಣಕ್ಕೆ ಕೈಕೊಂಡು': 6,  # Two words
}

for word, expected in test_words.items():
    actual = counter.count_syllables(word)
    status = "✓" if actual == expected else "✗"
    print(f"{status} '{word}' -> {actual} syllables (expected {expected})")

print()
print()

# Demo 2: Analyzing a simple Ragale (valid example)
print("DEMO 2: Analyzing a Valid Ragale Poem")
print("-" * 70)

# A simple valid-ish Ragale
valid_poem = """
ನಮ್ಮ ದೇಶದ ಮಹಿಮೆಯು ಜಗದಿ ಪ್ರಸಿದ್ಧವು
ಸಮ್ಮಣೆಯು ಬಂದಿಹುದು ಎಲ್ಲಾ ದಿಕ್ಕಿನಿಂದ
ಸಂಸ್ಕೃತಿಯು ಸಂಪ್ರದಾಯವು ನಮ್ಮದೆ ಹಳೆಯದಾಗಿದೆ
ಹೆಮ್ಮೆಯಿಂದ ನಾವು ಹೇಳುವೆವು ಭಾರತೀಯರು ಎಂದೆಂದು
"""

analyzer = RagaleAnalyzer(strict_mode=False)  # Flexible mode
result = analyzer.analyze_poem(valid_poem.strip())

print(f"Status: {'✓ VALID' if result.is_valid else '✗ INVALID'}")
print(f"Syllable counts: {result.syllable_counts}")
print(f"Expected: {result.expected_counts}")
print(f"Rhyme pattern: {result.rhyme_analysis.get('pattern', 'N/A')}")
print()

if result.errors:
    print("Errors:")
    for error in result.errors:
        print(f"  - {error}")

if result.warnings:
    print("Warnings:")
    for warning in result.warnings:
        print(f"  - {warning}")

print()
print()

# Demo 3: Detailed report
print("DEMO 3: Full Analysis Report")
print("-" * 70)

report = analyzer.format_report(result, valid_poem)
print(report)

print()
print("=" * 70)
print("Try running: python3 ragale_analyzer.py")
print("for interactive mode!")
print("=" * 70)
