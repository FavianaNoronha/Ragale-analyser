#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Ragale Analyzer - Validates Kannada poems against Ragale meter rules
"""

import re
import unicodedata
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass


@dataclass
class AnalysisResult:
    """Stores analysis results for a Ragale stanza"""
    is_valid: bool
    syllable_counts: List[int]
    expected_counts: List[int]
    rhyme_analysis: Dict[str, any]
    yati_analysis: Dict[str, any]
    errors: List[str]
    warnings: List[str]
    suggestions: List[str]


class KannadaSyllableCounter:
    """Counts syllables in Kannada text according to prosody rules"""
    
    # Kannada Unicode ranges
    KANNADA_RANGE = (0x0C80, 0x0CFF)
    
    # Vowels (ಸ್ವರಗಳು)
    INDEPENDENT_VOWELS = set('ಅಆಇಈಉಊಋಎಏಐಒಓಔ')
    
    # Vowel signs (ಮಾತ್ರೆಗಳು)
    VOWEL_SIGNS = set('\u0CBE\u0CBF\u0CC0\u0CC1\u0CC2\u0CC3\u0CC6\u0CC7\u0CC8\u0CCA\u0CCB\u0CCC')
    
    # Virama/Halant (್)
    VIRAMA = '\u0CCD'
    
    # Anusvara (ಂ) and Visarga (ಃ)
    ANUSVARA = '\u0C82'
    VISARGA = '\u0C83'
    
    # Consonants base range
    CONSONANTS = set('ಕಖಗಘಙಚಛಜಝಞಟಠಡಢಣತಥದಧನಪಫಬಭಮಯರಲವಶಷಸಹಳೞ')
    
    def __init__(self):
        self.debug = False
    
    def is_kannada_char(self, char: str) -> bool:
        """Check if character is in Kannada Unicode range"""
        if not char:
            return False
        code = ord(char)
        return self.KANNADA_RANGE[0] <= code <= self.KANNADA_RANGE[1]
    
    def extract_kannada_text(self, text: str) -> str:
        """Extract only Kannada text, removing punctuation and spaces"""
        # Remove common punctuation but keep Kannada text
        text = re.sub(r'[,\.;:!?\(\)\[\]\{\}"\']+', '', text)
        return text.strip()
    
    def count_syllables(self, text: str) -> int:
        """
        Count syllables (aksharas) in Kannada text
        
        Rules:
        1. Each independent vowel = 1 syllable
        2. Each consonant + vowel (with or without sign) = 1 syllable
        3. Virama (halant) combines with previous syllable
        4. Anusvara and Visarga attach to previous syllable
        """
        if not text:
            return 0
        
        # Clean the text - remove punctuation but keep spaces for proper word separation
        text = re.sub(r'[,\.;:!?\(\)\[\]\{\}"\']+', '', text)
        text = text.strip()
        
        syllable_count = 0
        i = 0
        
        if self.debug:
            print(f"Analyzing: {text}")
            print(f"Length: {len(text)}")
        
        while i < len(text):
            char = text[i]
            
            # Skip spaces - they don't count as syllables
            if char.isspace():
                i += 1
                continue
            
            # Skip non-Kannada characters
            if not self.is_kannada_char(char):
                i += 1
                continue
            
            # Independent vowel = 1 syllable
            if char in self.INDEPENDENT_VOWELS:
                syllable_count += 1
                if self.debug:
                    print(f"  [{i}] {char} -> Independent vowel (count={syllable_count})")
                i += 1
                continue
            
            # Consonant - check what follows
            if char in self.CONSONANTS or self.is_consonant(char):
                # Look ahead for virama, vowel signs, etc.
                next_idx = i + 1
                has_virama = False
                
                # Check if followed by virama
                if next_idx < len(text) and text[next_idx] == self.VIRAMA:
                    # Check if it's a conjunct (virama followed by another consonant)
                    if next_idx + 1 < len(text) and (
                        text[next_idx + 1] in self.CONSONANTS or 
                        self.is_consonant(text[next_idx + 1])
                    ):
                        # This is a conjunct beginning - don't count yet
                        # The syllable will be counted with the final consonant
                        has_virama = True
                        if self.debug:
                            print(f"  [{i}] {char} -> Conjunct part (no count)")
                        i = next_idx + 1  # Skip to next consonant
                        continue
                    else:
                        # Virama at end or before non-consonant
                        # This consonant doesn't form a syllable
                        if self.debug:
                            print(f"  [{i}] {char} -> Halant (no count)")
                        i = next_idx + 1
                        continue
                
                # Count this syllable (consonant with implicit 'a' or vowel sign)
                syllable_count += 1
                if self.debug:
                    print(f"  [{i}] {char} -> Consonant syllable (count={syllable_count})")
                
                i += 1
                
                # Skip vowel sign if present (already counted with consonant)
                if i < len(text) and text[i] in self.VOWEL_SIGNS:
                    if self.debug:
                        print(f"  [{i}] {text[i]} -> Vowel sign (attached)")
                    i += 1
                
                # Skip anusvara/visarga (part of same syllable)
                if i < len(text) and text[i] in (self.ANUSVARA, self.VISARGA):
                    if self.debug:
                        print(f"  [{i}] {text[i]} -> Anusvara/Visarga (attached)")
                    i += 1
                
                continue
            
            # Other cases - treat as syllable
            syllable_count += 1
            if self.debug:
                print(f"  [{i}] {char} -> Other (count={syllable_count})")
            i += 1
        
        return syllable_count
    
    def is_consonant(self, char: str) -> bool:
        """Check if character is a Kannada consonant"""
        if char in self.CONSONANTS:
            return True
        # Check Unicode category
        if self.is_kannada_char(char):
            category = unicodedata.category(char)
            return category == 'Lo'  # Letter, other (includes consonants)
        return False
    
    def split_at_yati(self, text: str, position: int) -> Tuple[str, str]:
        """Split text at yati (caesura) position"""
        syllables = self.get_syllable_list(text)
        if position > len(syllables):
            return text, ""
        
        # This is simplified - would need more sophisticated splitting
        # For now, just split the text roughly
        return text[:len(text)//2], text[len(text)//2:]
    
    def get_syllable_list(self, text: str) -> List[str]:
        """Get list of individual syllables (for advanced analysis)"""
        # Simplified version - returns approximate syllable boundaries
        syllables = []
        text = self.extract_kannada_text(text)
        
        i = 0
        current_syllable = ""
        
        while i < len(text):
            char = text[i]
            
            if not self.is_kannada_char(char) or char.isspace():
                if current_syllable:
                    syllables.append(current_syllable)
                    current_syllable = ""
                i += 1
                continue
            
            current_syllable += char
            
            # Check if syllable is complete
            if i + 1 < len(text):
                next_char = text[i + 1]
                
                # If next is virama, continue
                if next_char == self.VIRAMA:
                    i += 1
                    continue
                
                # If next is vowel sign, anusvara, visarga - add and complete
                if next_char in self.VOWEL_SIGNS or next_char in (self.ANUSVARA, self.VISARGA):
                    current_syllable += next_char
                    syllables.append(current_syllable)
                    current_syllable = ""
                    i += 2
                    continue
                
                # Independent vowel or new consonant - current syllable complete
                if next_char in self.INDEPENDENT_VOWELS or self.is_consonant(next_char):
                    syllables.append(current_syllable)
                    current_syllable = ""
                    i += 1
                    continue
            
            i += 1
        
        if current_syllable:
            syllables.append(current_syllable)
        
        return syllables


class RhymeAnalyzer:
    """Analyzes rhyme schemes (Prāsa) in Ragale"""
    
    def __init__(self):
        self.syllable_counter = KannadaSyllableCounter()
    
    def get_ending_sound(self, text: str, num_chars: int = 2) -> str:
        """Extract ending sound from text (last few characters)"""
        text = self.syllable_counter.extract_kannada_text(text)
        if not text:
            return ""
        
        # Get last 2-3 characters for rhyme comparison
        ending = text[-num_chars:] if len(text) >= num_chars else text
        return ending
    
    def check_rhyme(self, line1: str, line2: str) -> bool:
        """Check if two lines rhyme (same ending sound)"""
        ending1 = self.get_ending_sound(line1)
        ending2 = self.get_ending_sound(line2)
        
        if not ending1 or not ending2:
            return False
        
        return ending1 == ending2
    
    def get_rhyme_pattern(self, lines: List[str]) -> str:
        """
        Get rhyme pattern for lines (e.g., AABB, ABAB)
        Returns pattern like 'AABB' for 4 lines
        """
        if not lines:
            return ""
        
        pattern = []
        rhyme_groups = {}
        current_label = ord('A')
        
        for line in lines:
            ending = self.get_ending_sound(line)
            
            # Find if this ending matches any existing group
            found = False
            for rhyme_ending, label in rhyme_groups.items():
                if rhyme_ending == ending:
                    pattern.append(label)
                    found = True
                    break
            
            if not found:
                # New rhyme group
                label = chr(current_label)
                rhyme_groups[ending] = label
                pattern.append(label)
                current_label += 1
        
        return ''.join(pattern)
    
    def analyze_rhyme_scheme(self, lines: List[str]) -> Dict[str, any]:
        """Comprehensive rhyme analysis"""
        if len(lines) != 4:
            return {
                'valid': False,
                'pattern': '',
                'error': f'Expected 4 lines, got {len(lines)}'
            }
        
        pattern = self.get_rhyme_pattern(lines)
        
        # Check standard Ragale patterns
        valid_patterns = ['AABB', 'AAAA', 'AABA', 'ABAB']
        is_valid = pattern in valid_patterns
        
        # Get ending sounds
        endings = [self.get_ending_sound(line) for line in lines]
        
        # Check specific pair rhymes
        pair1_rhymes = self.check_rhyme(lines[0], lines[1])
        pair2_rhymes = self.check_rhyme(lines[2], lines[3])
        
        return {
            'valid': is_valid,
            'pattern': pattern,
            'expected_patterns': valid_patterns,
            'pair1_rhymes': pair1_rhymes,  # Lines 1-2
            'pair2_rhymes': pair2_rhymes,  # Lines 3-4
            'endings': endings,
            'line1_line2_match': pair1_rhymes,
            'line3_line4_match': pair2_rhymes
        }


class RagaleAnalyzer:
    """Main Ragale analyzer combining all validation rules"""
    
    # Standard Ragale patterns
    STANDARD_PATTERNS = {
        'sadhaarana': [12, 12, 16, 16],  # Most common
        'sama_12': [12, 12, 12, 12],      # Equal lines - 12
        'sama_14': [14, 14, 14, 14],      # Equal lines - 14
        'sama_16': [16, 16, 16, 16],      # Equal lines - 16
    }
    
    def __init__(self, strict_mode: bool = True):
        """
        Initialize analyzer
        
        Args:
            strict_mode: If True, enforce strict Ragale rules. 
                        If False, allow some flexibility (±1 syllable)
        """
        self.syllable_counter = KannadaSyllableCounter()
        self.rhyme_analyzer = RhymeAnalyzer()
        self.strict_mode = strict_mode
        self.tolerance = 0 if strict_mode else 1
    
    def analyze_poem(self, text: str, expected_pattern: str = 'sadhaarana') -> AnalysisResult:
        """
        Analyze a Ragale stanza
        
        Args:
            text: The poem text (4 lines expected)
            expected_pattern: Type of Ragale pattern to check against
            
        Returns:
            AnalysisResult with detailed validation results
        """
        # Parse lines
        lines = self.parse_lines(text)
        
        # Get expected syllable counts
        expected_counts = self.STANDARD_PATTERNS.get(
            expected_pattern, 
            self.STANDARD_PATTERNS['sadhaarana']
        )
        
        errors = []
        warnings = []
        suggestions = []
        
        # Validate line count
        if len(lines) != 4:
            errors.append(f"Ragale must have exactly 4 lines. Found {len(lines)} lines.")
            return AnalysisResult(
                is_valid=False,
                syllable_counts=[],
                expected_counts=expected_counts,
                rhyme_analysis={},
                yati_analysis={},
                errors=errors,
                warnings=warnings,
                suggestions=["Ensure your stanza has exactly 4 lines"]
            )
        
        # Count syllables for each line
        syllable_counts = [self.syllable_counter.count_syllables(line) for line in lines]
        
        # Validate syllable counts
        syllable_valid = True
        for i, (actual, expected) in enumerate(zip(syllable_counts, expected_counts)):
            diff = abs(actual - expected)
            
            if diff > self.tolerance:
                syllable_valid = False
                errors.append(
                    f"Line {i+1}: Expected {expected} syllables, found {actual} "
                    f"({'+' if actual > expected else ''}{actual - expected})"
                )
            elif diff == 1 and not self.strict_mode:
                warnings.append(
                    f"Line {i+1}: {actual} syllables (expected {expected}, within tolerance)"
                )
        
        # Analyze rhyme scheme
        rhyme_analysis = self.rhyme_analyzer.analyze_rhyme_scheme(lines)
        
        if not rhyme_analysis['valid']:
            errors.append(
                f"Rhyme pattern '{rhyme_analysis['pattern']}' does not match "
                f"standard Ragale patterns: {', '.join(rhyme_analysis['expected_patterns'])}"
            )
        
        if not rhyme_analysis['pair1_rhymes']:
            errors.append(f"Lines 1 and 2 do not rhyme (endings: {rhyme_analysis['endings'][0]} vs {rhyme_analysis['endings'][1]})")
        
        if not rhyme_analysis['pair2_rhymes']:
            errors.append(f"Lines 3 and 4 do not rhyme (endings: {rhyme_analysis['endings'][2]} vs {rhyme_analysis['endings'][3]})")
        
        # Analyze Yati (caesura)
        yati_analysis = self.analyze_yati(lines, expected_counts)
        
        if not yati_analysis['valid']:
            warnings.extend(yati_analysis['warnings'])
        
        # Generate suggestions
        if syllable_counts != expected_counts:
            suggestions.append("Check syllable counting, especially:")
            suggestions.append("  - Conjunct consonants (should not add extra syllables)")
            suggestions.append("  - Ottu/gunita (double consonants)")
            suggestions.append("  - Anusvara (ಂ) and Visarga (ಃ) don't add syllables")
        
        if not rhyme_analysis['valid']:
            suggestions.append("Ensure lines 1-2 end with same sound, and lines 3-4 end with same sound")
            suggestions.append(f"Current endings: L1='{rhyme_analysis['endings'][0]}', L2='{rhyme_analysis['endings'][1]}', "
                             f"L3='{rhyme_analysis['endings'][2]}', L4='{rhyme_analysis['endings'][3]}'")
        
        # Overall validation
        is_valid = (
            len(errors) == 0 and
            syllable_valid and
            rhyme_analysis['valid']
        )
        
        return AnalysisResult(
            is_valid=is_valid,
            syllable_counts=syllable_counts,
            expected_counts=expected_counts,
            rhyme_analysis=rhyme_analysis,
            yati_analysis=yati_analysis,
            errors=errors,
            warnings=warnings,
            suggestions=suggestions
        )
    
    def parse_lines(self, text: str) -> List[str]:
        """Parse poem text into individual lines"""
        # Split by newlines and filter empty lines
        lines = [line.strip() for line in text.strip().split('\n') if line.strip()]
        return lines
    
    def analyze_yati(self, lines: List[str], expected_counts: List[int]) -> Dict[str, any]:
        """
        Analyze Yati (caesura) placement
        
        Yati should be at:
        - 6th syllable for 12-syllable lines
        - 8th syllable for 16-syllable lines
        """
        yati_positions = {
            12: 6,
            14: 7,
            16: 8
        }
        
        warnings = []
        valid = True
        
        for i, (line, expected_syllables) in enumerate(zip(lines, expected_counts)):
            expected_yati = yati_positions.get(expected_syllables)
            
            if expected_yati:
                # This is a heuristic - proper yati analysis needs word boundary detection
                syllables = self.syllable_counter.get_syllable_list(line)
                
                # Check if there's a natural word boundary near expected yati
                # This is simplified - proper implementation would check for spaces/word breaks
                if len(syllables) >= expected_yati:
                    warnings.append(
                        f"Line {i+1}: Check for natural pause (yati) around syllable {expected_yati}"
                    )
        
        return {
            'valid': True,  # Yati is guidance, not strict rule for validation
            'warnings': warnings
        }
    
    def format_report(self, result: AnalysisResult, poem_text: str) -> str:
        """Format analysis result as readable report"""
        lines = self.parse_lines(poem_text)
        
        report = []
        report.append("=" * 70)
        report.append("RAGALE ANALYSIS REPORT")
        report.append("=" * 70)
        report.append("")
        
        # Overall result
        status = "✓ VALID RAGALE" if result.is_valid else "✗ NOT VALID RAGALE"
        report.append(f"Status: {status}")
        report.append("")
        
        # Poem display with line numbers
        report.append("POEM:")
        report.append("-" * 70)
        for i, line in enumerate(lines, 1):
            report.append(f"{i}. {line}")
        report.append("")
        
        # Syllable analysis
        report.append("SYLLABLE COUNT ANALYSIS:")
        report.append("-" * 70)
        for i, (actual, expected) in enumerate(zip(result.syllable_counts, result.expected_counts), 1):
            status_symbol = "✓" if actual == expected else "✗"
            diff = actual - expected
            diff_str = f" ({'+' if diff > 0 else ''}{diff})" if diff != 0 else ""
            report.append(f"Line {i}: {actual} syllables (expected {expected}){diff_str} {status_symbol}")
        report.append("")
        
        # Rhyme analysis
        report.append("RHYME SCHEME ANALYSIS:")
        report.append("-" * 70)
        rhyme = result.rhyme_analysis
        if rhyme:
            report.append(f"Pattern: {rhyme.get('pattern', 'N/A')}")
            report.append(f"Expected patterns: {', '.join(rhyme.get('expected_patterns', []))}")
            report.append(f"Lines 1-2 rhyme: {'✓ Yes' if rhyme.get('pair1_rhymes') else '✗ No'} "
                         f"(endings: '{rhyme.get('endings', ['',''])[0]}' vs '{rhyme.get('endings', ['','',''])[1]}')")
            report.append(f"Lines 3-4 rhyme: {'✓ Yes' if rhyme.get('pair2_rhymes') else '✗ No'} "
                         f"(endings: '{rhyme.get('endings', ['','','',''])[2]}' vs '{rhyme.get('endings', ['','','',''])[3]}')")
        report.append("")
        
        # Errors
        if result.errors:
            report.append("ERRORS:")
            report.append("-" * 70)
            for error in result.errors:
                report.append(f"✗ {error}")
            report.append("")
        
        # Warnings
        if result.warnings:
            report.append("WARNINGS:")
            report.append("-" * 70)
            for warning in result.warnings:
                report.append(f"⚠ {warning}")
            report.append("")
        
        # Suggestions
        if result.suggestions:
            report.append("SUGGESTIONS:")
            report.append("-" * 70)
            for suggestion in result.suggestions:
                report.append(f"💡 {suggestion}")
            report.append("")
        
        report.append("=" * 70)
        
        return "\n".join(report)


def main():
    """Main function for command-line usage"""
    import sys
    
    print("=" * 70)
    print("RAGALE ANALYZER - Kannada Poetry Meter Validator")
    print("=" * 70)
    print()
    
    # Example usage
    if len(sys.argv) > 1:
        # Read from file
        filename = sys.argv[1]
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                poem = f.read()
        except FileNotFoundError:
            print(f"Error: File '{filename}' not found")
            sys.exit(1)
    else:
        # Interactive mode
        print("Enter your Ragale poem (4 lines, press Enter twice when done):")
        print()
        lines = []
        empty_count = 0
        
        while empty_count < 1:
            line = input()
            if line.strip():
                lines.append(line)
                empty_count = 0
            else:
                empty_count += 1
            
            if len(lines) == 4:
                break
        
        poem = '\n'.join(lines)
    
    if not poem.strip():
        print("No poem provided. Exiting.")
        sys.exit(1)
    
    # Analyze
    analyzer = RagaleAnalyzer(strict_mode=True)
    result = analyzer.analyze_poem(poem)
    
    # Print report
    report = analyzer.format_report(result, poem)
    print(report)
    
    # Exit code
    sys.exit(0 if result.is_valid else 1)


if __name__ == "__main__":
    main()
