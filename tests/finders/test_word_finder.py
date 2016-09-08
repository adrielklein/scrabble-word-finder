from unittest.mock import Mock, call

from app.finders.anagram_finder import AnagramFinder
from app.finders.word_finder import WordFinder


def test_when_letters_string_is_empty_then_word_finder_calls_anagram_finder_with_empty_string(monkeypatch):
    monkeypatch.setattr(AnagramFinder, 'get_anagrams', Mock(return_value=[]))
    word_finder = WordFinder(AnagramFinder([]))
    assert [] == word_finder.get_words('')


def test_when_letters_string_is_abc_then_word_finder_calls_anagram_finder_with_all_combinations_of_abc(monkeypatch):
    results_of_get_anagrams = [['cab'], ['ab', 'ba'], [], []]
    monkeypatch.setattr(AnagramFinder, 'get_anagrams', Mock(side_effect=results_of_get_anagrams))
    word_finder = WordFinder(AnagramFinder([]))
    assert ['cab', 'ab', 'ba'] == word_finder.get_words('abc')
    expected_calls = [call('ab'), call('ac'), call('bc'), call('abc')]
    AnagramFinder.get_anagrams.assert_has_calls(expected_calls)
    assert 4 == AnagramFinder.get_anagrams.call_count


def test_when_anagram_finder_gives_duplicates_then_only_choose_uniques(monkeypatch):
    results_of_get_anagrams = [['bib'], ['bib'], ['bib'], ['bib']]
    monkeypatch.setattr(AnagramFinder, 'get_anagrams', Mock(side_effect=results_of_get_anagrams))
    word_finder = WordFinder(AnagramFinder([]))
    assert ['bib'] == word_finder.get_words('ibb')
