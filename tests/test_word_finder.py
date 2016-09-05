from unittest.mock import Mock, call

from app.anagram_finder import AnagramFinder
from app.word_finder import WordFinder


def test_when_letters_string_is_empty_then_word_finder_calls_anagram_finder_with_empty_string(monkeypatch):
    monkeypatch.setattr(AnagramFinder, 'get_anagrams', Mock(return_value=[]))
    word_finder = WordFinder(AnagramFinder([]))
    assert [] == word_finder.get_words('')


def test_when_letters_string_is_abc_then_word_finder_calls_anagram_finder_with_all_combinations_of_abc(monkeypatch):
    results_of_get_anagrams = [['cab'], ['ab', 'ba'], [], []]
    monkeypatch.setattr(AnagramFinder, 'get_anagrams', Mock(side_effect=results_of_get_anagrams))
    word_finder = WordFinder(AnagramFinder([]))
    assert ['cab', 'ab', 'ba'] == word_finder.get_words('abc')
    expected_calls = ['abc', 'ab', 'ac', 'bc']
    AnagramFinder.get_anagrams.has_calls(expected_calls)
    assert 4 == AnagramFinder.get_anagrams.call_count
