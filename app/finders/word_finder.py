import itertools


def _get_combinations(letters_string):
    result = []
    for i in range(2, len(letters_string) + 1):
        for combination in itertools.combinations(letters_string, i):
            result.append(''.join(combination))
    return result


class WordFinder(object):
    def __init__(self, anagram_finder):
        self._anagram_finder = anagram_finder

    def get_words(self, letters_string):
        words = set()
        for combination in _get_combinations(letters_string):
            words.update(self._anagram_finder.get_anagrams(combination))
        return list(words)
