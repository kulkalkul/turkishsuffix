import collections

from config_loader import config

Settings = config["settings"]
Exceptions = config["exceptions"]

# SuffixWord = collections.namedtuple("SuffixWord", ("word", "rule_set"))


class TurkishSuffix:
    def __init__(self):
        self.__rule_set = dict(zip(Settings.types, Settings.rule_set))
        self.__buffer_exceptions = dict(zip(Exceptions.buffer_exception_types, Exceptions.buffer_exception))

    def suffix(self, word, suffix_type):
        index, division, first, last, *options = self.__rule_set[suffix_type]
        index, division, first, last = int(index), int(division), first.replace("-", ""), last.replace("-", "")

        last_vowel = self.__vowel_from_backwards(word)
        vowel = self.__vowel_harmony(index, division, last_vowel)
        first, consonant = self.__hards_and_softs(word, first, last_vowel, options)
        first = self.__buffer_letter(word, suffix_type, first, last_vowel, options)

        return word[:-1] + consonant + first + vowel + last

    def __vowel_harmony(self, index, division, last_vowel):
        vowel_harmony = index + Settings.vowels.index(last_vowel) // 2 % division
        return Settings.suffix_vowels[vowel_harmony]

    def __vowel_from_backwards(self, word):
        vowel_from_backwards = (letter for letter in word[::-1] if letter in Settings.vowels)
        return vowel_from_backwards.__next__()

    def __hards_and_softs(self, word, first, vowel, options):
        last_letter = word[-1]
        if vowel is word[-1]:
            return first, last_letter
        if last_letter not in Settings.hards:
            return first, last_letter
        if first in Settings.softs[:2]:
            return Settings.hards[Settings.softs.index(first)], last_letter
        elif ";" in options:
            return first, Settings.softs[Settings.hards.index(last_letter)]

    def __buffer_letter(self, word, suffix_type, first, vowel, options):
        if vowel is not word[-1]:
            return first.replace("+", "")
        if ":" not in options:
            return first.replace("+", "n")
        elif word.lower() in self.__buffer_exceptions[suffix_type]:
            return first.replace("+", "y")
        else:
            return first.replace("+", "n")


turkishSuffix = TurkishSuffix()

# print(turkishSuffix.suffix("bora", "ilgi"))
