import pytest
from lib.grammar_stats import *

"""
Given a string starting with capital letter and ending with valid punctuation
return true
"""

def test_string_with_capital_letter_and_valid_punctuation():
    sentence = GrammarStats()
    assert sentence.check("Hello world!") == True

"""
Given a string starting with capital letter and no ending with valid punctuation
return false
"""

def test_string_with_capital_letter_and_no_valid_punctuation():
    sentence = GrammarStats()
    assert sentence.check("Hello world") == False

"""
Given a string starting with lowercase letter and ending with valid punctuation
return false
"""

def test_string_with_no_capital_letter_and_valid_punctuation():
    sentence = GrammarStats()
    assert sentence.check("hello world!") == False

"""
Given an empty string
raise error
"""

def test_string_with_empty_string():
    sentence = GrammarStats()
    with pytest.raises(Exception) as e:
        sentence.check('')
    error_message = str(e.value)
    assert error_message == "Must provide a text for validity check"