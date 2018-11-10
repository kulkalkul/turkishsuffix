from config_loader import config

import collections

Settings = config["settings"]
Exceptions = config["exceptions"]


class TurkishSuffix:
    def __init__(self):
        self.__rule_set = dict(zip(Settings.types, Settings.rule_set))

    def suffix(self, word, suffix_type):
        index, division, first, last, *options = self.__rule_set[suffix_type]
        index, division = int(index), int(division)

        vowel_from_backwards = (letter for letter in word[::-1] if letter in Settings.vowels)
        last_vowel = vowel_from_backwards.__next__()

        vowel_harmony = index + Settings.vowels.index(last_vowel) // 2 % division
        vowel = Settings.suffix_vowels[vowel_harmony]

        return vowel
