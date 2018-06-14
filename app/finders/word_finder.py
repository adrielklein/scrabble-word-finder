import itertools
import re

def _get_combinations(letters_string):
    result = []
    for i in range(2, len(letters_string) + 1):
        for combination in itertools.combinations(letters_string, i):
            result.append(''.join(combination))
    return result

def _get_words(self, letters_string):
    result = set()
    words = self._anagram_finder._words
    for word in words:
        match = re.search(letters_string, word, re.IGNORECASE)
        if match:                      
            result.add(match.group())
    return result

class WordFinder(object):
    def __init__(self, anagram_finder):
        self._anagram_finder = anagram_finder

    def get_words(self, letters_string):
        words = set()
        for word in _get_words(self, letters_string):
            words.update([word])
        return sorted(words, key=lambda word: (-len(word), word))
