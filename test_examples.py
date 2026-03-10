#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test examples for Ragale Analyzer
Contains sample Ragale poems for testing
"""

from ragale_analyzer import RagaleAnalyzer, KannadaSyllableCounter


# Example 1: Valid Ragale (from classical literature)
EXAMPLE_VALID_1 = """
ಕರಣಕ್ಕೆ ಕೈಕೊಂಡು ಹರಿವಂದು ನಂಬಿದೆನೆ
ಮರಣವನ್ನು ನೆಗೆಳದ ದೈವದನ್ನು ಪೇಳಿದೆನೆ
ಕರುಣಾಕರ ಪರಮೇಶ್ವರ ಕಾಪಾಡುದೆನ್ನ ಬನ್ನಿಸಿದು
ತರುಣದಲಿ ನಿರ್ವಿಕಾರ ಹೃದಯದಲಿ ತೊಂಡಿಸಿದಿರಬೆಂದು
"""

# Example 2: Valid Ragale - Devotional
EXAMPLE_VALID_2 = """
ಭಕ್ತಿಯಿಂದ ಭಗವಂತನ ಪಾದವ ಪೂಜಿಸಿದನು
ಮುಕ್ತಿಗಾಗಿ ಮನದೊಳಗೆ ಪ್ರಾರ್ಥಿಸಿದನು
ಶಕ್ತಿಯುತ ಮಹಾದೇವನ ನಾಮವ ಸ್ಮರಿಸಿದನು ಅವನು
ಭಕ್ತಿಯೆಂಬ ಮಾರ್ಗದಲ್ಲಿ ನಡೆದನು ನಿತ್ಯವು ನಿರಂತರವು
"""

# Example 3: Invalid - Wrong syllable count
EXAMPLE_INVALID_SYLLABLES = """
ಕರಣಕ್ಕೆ ಕೈಕೊಂಡು ಹರಿ
ಮರಣವನ್ನು ನೆಗೆಳದ ದೈವ
ಕರುಣಾಕರ ಪರಮೇಶ್ವರ ಕಾಪಾಡುದು
ತರುಣದಲಿ ನಿರ್ವಿಕಾರ ಹೃದಯ
"""

# Example 4: Invalid - No rhyme
EXAMPLE_INVALID_RHYME = """
ಕರಣಕ್ಕೆ ಕೈಕೊಂಡು ಹರಿವಂದು ನಂಬಿದನು
ಮರಣವನ್ನು ನೆಗೆಳದ ದೈವದನ್ನು ಪೇಳುವೆನು
ಕರುಣಾಕರ ಪರಮೇಶ್ವರ ಕಾಪಾಡುದೆನ್ನ ಬನ್ನಿಸಿದ
ತರುಣದಲಿ ನಿರ್ವಿಕಾರ ಹೃದಯದಲಿ ತೊಂಡಿಸಿದಿರುವನು
"""

# Example 5: Simple test for syllable counting
SYLLABLE_TEST_WORDS = {
    'ಕರಣ': 3,      # ka-ra-ṇa
    'ಪ್ರೇಮ': 2,    # prē-ma
    'ಅರಮನೆ': 4,    # a-ra-ma-ne
    'ಕರುಣಾಮಯ': 5,  # ka-ru-ṇā-ma-ya
    'ಹೃದಯ': 3,     # hṛ-da-ya
    'ಭಕ್ತಿ': 2,   # bhak-ti
    'ಸ್ಮರಣೆ': 3,   # sma-ra-ṇe
    'ಮಂಗಳ': 3,     # maṅ-ga-ḷa
    'ನಿತ್ಯ': 2,    # nit-ya
}


def test_syllable_counting():
    """Test syllable counting accuracy"""
    print("=" * 70)
    print("TESTING SYLLABLE COUNTING")
    print("=" * 70)
    print()
    
    counter = KannadaSyllableCounter()
    
    passed = 0
    failed = 0
    
    for word, expected in SYLLABLE_TEST_WORDS.items():
        actual = counter.count_syllables(word)
        status = "✓" if actual == expected else "✗"
        
        print(f"{status} '{word}': Expected {expected}, Got {actual}")
        
        if actual == expected:
            passed += 1
        else:
            failed += 1
    
    print()
    print(f"Results: {passed} passed, {failed} failed")
    print()


def test_poem_analysis(poem: str, description: str, should_be_valid: bool):
    """Test analysis of a complete poem"""
    print("=" * 70)
    print(f"TESTING: {description}")
    print("=" * 70)
    print()
    
    analyzer = RagaleAnalyzer(strict_mode=True)
    result = analyzer.analyze_poem(poem)
    report = analyzer.format_report(result, poem)
    
    print(report)
    
    # Verify result matches expectation
    if result.is_valid == should_be_valid:
        print(f"✓ Test PASSED - Result as expected (valid={should_be_valid})")
    else:
        print(f"✗ Test FAILED - Expected valid={should_be_valid}, got valid={result.is_valid}")
    
    print()


def run_all_tests():
    """Run all test cases"""
    print("\n")
    print("*" * 70)
    print("RAGALE ANALYZER - RUNNING TEST SUITE")
    print("*" * 70)
    print("\n")
    
    # Test 1: Syllable counting
    test_syllable_counting()
    
    # Test 2: Valid Ragale examples
    test_poem_analysis(EXAMPLE_VALID_1, "Valid Ragale - Classical Example", should_be_valid=True)
    test_poem_analysis(EXAMPLE_VALID_2, "Valid Ragale - Devotional", should_be_valid=True)
    
    # Test 3: Invalid examples
    test_poem_analysis(EXAMPLE_INVALID_SYLLABLES, "Invalid - Wrong Syllable Count", should_be_valid=False)
    test_poem_analysis(EXAMPLE_INVALID_RHYME, "Invalid - No Rhyme Scheme", should_be_valid=False)
    
    print("*" * 70)
    print("TEST SUITE COMPLETED")
    print("*" * 70)


if __name__ == "__main__":
    run_all_tests()
