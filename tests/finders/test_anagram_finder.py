from app.finders.anagram_finder import AnagramFinder


def test_when_there_are_no_words_then_get_anagrams_returns_nothing():
    words = []
    anagram_finder = AnagramFinder(words)
    assert [] == anagram_finder.get_anagrams('ader')


def test_when_there_is_an_anagram_then_return_it():
    words = ['read']
    anagram_finder = AnagramFinder(words)
    assert ['read'] == anagram_finder.get_anagrams('ader')


def test_when_there_are_multiple_words_then_return_correct_anagram():
    words = ['read', 'cat']
    anagram_finder = AnagramFinder(words)
    assert ['read'] == anagram_finder.get_anagrams('ader')


def test_when_letters_are_not_sorted_then_sort_them_before_searching_for_anagrams():
    words = ['read']
    anagram_finder = AnagramFinder(words)
    assert ['read'] == anagram_finder.get_anagrams('dera')


def test_when_there_are_multiple_anagrams_then_return_them():
    words = ['read', 'dear', 'cat']
    anagram_finder = AnagramFinder(words)
    assert ['dear', 'read'] == anagram_finder.get_anagrams('reda')
