import pytest
from lib.grammar_stats import *

"""
Given a string starting with capital letter and ending with valid punctuation
return true
"""

def test_string_with_capital_letter_and_valid_punctuation():
    sentence = GrammarStats()
    result = sentence.check("Hello world!")
    assert result == True

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

"""
Given a valid sentence 
percentage_ good returns 100
"""

def test_valid_sentence_returns_100():
    sentence = GrammarStats()
    sentence.check("Hello world!")
    result = sentence.percentage_good()
    assert result == 100

"""
Given a valid sentence and none valid sentence
percentage_ good returns 50
"""

def test_valid_sentence_returns_50():
    sentence = GrammarStats()
    sentence.check("Hello world!")
    sentence.check("Hello world")
    result = sentence.percentage_good()
    assert result == 50

"""
Given no valid sentences
percentage_ good returns 0
"""

def test_no_valid_sentences_returns_0():
    sentence = GrammarStats()
    sentence.check("Hello world")
    sentence.check("Hello world")
    sentence.check("Hello world")
    result = sentence.percentage_good()
    assert result == 0

"""
Given one valid sentence and two no valid sentences
percentage_ good returns 33
"""

def test_1_valid_sentence_and_two_invalid_returns_33():
    sentence = GrammarStats()
    sentence.check("Hello world!")
    sentence.check("Hello world")
    sentence.check("Hello world")
    result = sentence.percentage_good()
    assert result == 33