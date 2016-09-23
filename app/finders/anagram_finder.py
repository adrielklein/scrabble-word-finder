from collections import defaultdict

from werkzeug.utils import cached_property


class AnagramFinder(object):
    def __init__(self, words):
        self._words = words

    @cached_property
    def _alphagram_2_words(self):
        result = defaultdict(lambda: set())
        for word in self._words:
            alphagram = ''.join(sorted(word))
            result[alphagram].add(word)
        return result

    def get_anagrams(self, letter_string):
        alphagram = ''.join(sorted(letter_string))
        return sorted(list(self._alphagram_2_words[alphagram]))
