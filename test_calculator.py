from calculator import Calculator
import pytest


def test_positive_num():
    calc = Calculator()
    assert calc.is_positive(1) == True


def test_negative_num():
    calc = Calculator()
    assert calc.is_positive(-1) == False


def test_zero_num():
    calc = Calculator()
    assert calc.is_positive(0) == False


def test_word_with_vowels():
    calc = Calculator()
    assert calc.count_vowels("apple") == 2


def test_word_with_no_vowels():
    calc = Calculator()
    assert calc.count_vowels("sky") == 0


def test_empty_string():
    calc = Calculator()
    assert calc.count_vowels("") == 0


def test_word_with_uppercase_letters():
    calc = Calculator()
    assert calc.count_vowels("APPLE") == 2


def test_large_positive_num():
    calc = Calculator()
    assert calc.is_positive(1000000) == True


def test_word_with_all_vowels():
    calc = Calculator()
    assert calc.count_vowels("aeiou") == 5
