from loader import config


class TurkishSuffix:
    def __init__(self, _word, _type=None):
        self._word = _word
        self._old_word = _word
        self._type = _type
        self._suffix = None
        if _type is not None:
            self.set_suffix(_type)

    def set_suffix(self, _type):
        self._word = self._old_word
        index = int(config.rule_set[config.types.index(_type)][0])
        division = int(config.rule_set[config.types.index(_type)][1])
        first = config.rule_set[config.types.index(_type)][2].replace("-", "")
        last = config.rule_set[config.types.index(_type)][3].replace("-", "")
        for i, letter in enumerate(self._old_word[::-1]):
            if letter in config.hards:
                if first[0] in "cd":
                    first = first.replace(first[0], config.hards[config.softs.index(first[0])])
                elif ";" in config.rule_set[config.types.index(_type)]:
                    if config.hards.index(letter) < 4:
                        self._word = self._old_word[:-1] + config.softs[config.hards.index(letter)]
            if letter in config.vowels:
                if i < 1:
                    if ":" in config.rule_set[config.types.index(_type)]:
                        if self._word.lower() in config.exceptions[config.types.index(_type)]:
                            first = first.replace("+", "y")
                        else:
                            first = first.replace("+", "n")
                    else:
                        first = first.replace("+", "y")
                first = first.replace("+", "")
                self._suffix = first + config.suffixes[index + config.vowels.index(letter)
                                                              // 2 % division] + last
                break

    def get_suffix(self):
        return self._suffix

    def get_word(self, special=False, type=None):
        if type is not None:
            self.set_suffix(type)
        if special is True:
            return self._old_word + "'" + self._suffix
        return self._word + self._suffix

    def get_old_word(self):
        return self._old_word



