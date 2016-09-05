from app.anagram_finder import AnagramFinder


def test_when_anagram_finder_has_no_words_then_get_anagrams_returns_nothing():
    words = []
    anagram_finder = AnagramFinder()
    anagram_finder.add_words(words)
    assert [] == anagram_finder.get_anagrams('house')