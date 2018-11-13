import collections

from .config_loader import config

Settings = config["settings"]
Exceptions = config["exceptions"]


SuffixWord = collections.namedtuple("SuffixWord", ("word", "suffix_type", "apostrophe", "possessive", "new_word",
                                                   "suffix", "suffixed"))


def lower_turkish(string):
    new_string = [Settings.lowercase_i[Settings.uppercase_i.index(letter)] if letter in Settings.uppercase_i
                  else letter.lower() for (i, letter) in enumerate(string)]
    return "".join(new_string)


class TurkishSuffix:
    def __init__(self):
        self.__rule_set = dict(zip(Settings.types, Settings.rule_set))
        self.__possessive_rule_set = dict(zip(Settings.possessive_types, Settings.possessive_rule_set))
        self.__buffer_exceptions = dict({key: Exceptions.buffer_exception for key in Exceptions.buffer_exception_types})

    def suffix(self, word, suffix_type, apostrophe=False, possessive=None):
        if suffix_type not in self.__rule_set:
            raise KeyError("'{}' Hint: There is no suffix type with that name.".format(suffix_type))
        index, division, first, last, *options = self.__rule_set[suffix_type]
        index, division = int(index), int(division)

        last_vowel = self.__vowel_from_backwards(word)
        vowel = self.__vowel_harmony(word, index, division, last_vowel)
        word, first, last, vowel, last_vowel = self.__possessive(word, suffix_type, index, division, first, last,
                                                                 possessive, last_vowel, vowel)

        first, last = first.replace("-", ""), last.replace("-", "")
        first, consonant = self.__hards_and_softs(word, first, last_vowel, options, possessive)
        first = self.__buffer_letter(word, suffix_type, first, last_vowel, options, possessive)

        if apostrophe:
            apostrophe = "'"
            new_word = word
        else:
            apostrophe = ""
            new_word = word[:-1] + consonant

        suffix = first + vowel + last
        suffixed = new_word + apostrophe + suffix
        return SuffixWord(word, suffix_type, apostrophe, possessive, new_word, suffix, suffixed)

    def __possessive(self, word, suffix_type, index, division, first, last, possessive, last_vowel, vowel):
        possessive_vowel = ""
        if suffix_type is not "iyelik":
            return word, first, last, vowel, last_vowel
        if not possessive:
            raise TypeError("suffix() missing 1 required positional argument: 'possessive'\n"
                            "Hint: You can not use possessive suffix without defining possessive state.")
        if possessive not in self.__possessive_rule_set:
            raise KeyError("'{}' Hint: There is no possessive state with that name.".format(possessive))
        possessive_first, possessive_last, *possessive_options = self.__possessive_rule_set[possessive]
        if ";" in possessive_options:
            plural = self.suffix(word, "çokluk")
            possessive_first = possessive_first + plural.suffix
            last_vowel = self.__vowel_from_backwards(plural.suffixed)
            vowel = self.__vowel_harmony(plural.suffixed, index, division, last_vowel)
        if ":" not in possessive_options and "," not in possessive_options and last_vowel is word[-1]:
            if lower_turkish(word) not in self.__buffer_exceptions[suffix_type]:
                vowel = ""
        elif ":" in possessive_options and last_vowel is not word[-1]:
            possessive_vowel = vowel
        elif ":" in possessive_options and lower_turkish(word) in self.__buffer_exceptions[suffix_type]:
            possessive_vowel = vowel
        possessive_first = possessive_vowel + possessive_first
        return word, possessive_first, possessive_last, vowel, last_vowel

    def __vowel_harmony(self, word, index, division, last_vowel):
        major = self.__major_vowel(word)
        vowel_harmony = index + Settings.vowels.index(last_vowel) // 2 % division + major
        return Settings.suffix_vowels[vowel_harmony]

    def __major_vowel(self, word):
        return lower_turkish(word) in Exceptions.major_vowel_exception

    def __vowel_from_backwards(self, word):
        vowel_from_backwards = (letter for letter in word[::-1] if letter in Settings.vowels)
        return vowel_from_backwards.__next__()

    def __hards_and_softs(self, word, first, vowel, options, possessive):
        last_letter = word[-1]
        if vowel is word[-1]:
            return first, last_letter
        elif possessive == "3ç":
            return first, last_letter
        elif last_letter not in Settings.hards:
            return first, last_letter
        elif first in Settings.softs[:2]:
            return Settings.hards[Settings.softs.index(first)], last_letter
        elif ";" in options and last_letter in Settings.hards[:4]:
            return first, Settings.softs[Settings.hards.index(last_letter)]
        return first, last_letter

    def __buffer_letter(self, word, suffix_type, first, vowel, options, possessive):
        if vowel is not word[-1]:
            return first.replace("+", "")
        elif suffix_type in self.__buffer_exceptions and lower_turkish(word) in self.__buffer_exceptions[suffix_type]:
            if possessive == "1ç" or possessive == "2ç":
                return "y" + first
            if first:
                return first.replace("+", "y")
            return first + "y"
        if "," in options:
            return first.replace("+", "s")
        elif ":" not in options:
            return first.replace("+", "y")
        return first.replace("+", "n")


turkishSuffix = TurkishSuffix()
