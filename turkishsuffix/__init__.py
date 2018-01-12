
class TurkishSuffix:
    def __init__(self):
        import configparser
        import json
        import pkg_resources
        path = pkg_resources.resource_filename(__name__, "config.ini")
        config = configparser.ConfigParser()
        config.read_file(open(path, "r", encoding="utf-8"))
        self.types = json.loads(config.get("Settings", "types"))
        self.vowels = json.loads(config.get("Settings", "vowels"))
        self.softs = json.loads(config.get("Settings", "softs"))
        self.hards = json.loads(config.get("Settings", "hards"))
        self.rule_set = json.loads(config.get("Settings", "rule_set"))
        self.suffixes = json.loads(config.get("Settings", "suffixes"))
        self.exceptions = []
        for i, exception in enumerate(self.types):
            try:
                self.exceptions.append(json.loads(config.get("Exceptions", exception)))
            except configparser.NoOptionError:
                self.exceptions.append(None)


turkishSuffix = TurkishSuffix()


class Suffix:
    def __init__(self, _word, _type=None):
        self._word = _word
        self._old_word = _word
        self._type = _type
        self._suffix = None
        if _type is not None:
            self.set_suffix(_type)

    def set_suffix(self, _type):
        self._word = self._old_word
        index = int(turkishSuffix.rule_set[turkishSuffix.types.index(_type)][0])
        division = int(turkishSuffix.rule_set[turkishSuffix.types.index(_type)][1])
        first = turkishSuffix.rule_set[turkishSuffix.types.index(_type)][2].replace("-", "")
        last = turkishSuffix.rule_set[turkishSuffix.types.index(_type)][3].replace("-", "")
        for i, letter in enumerate(self._old_word[::-1]):
            if letter in turkishSuffix.hards:
                if first[0] in "cd":
                    first = first.replace(first[0], turkishSuffix.hards[turkishSuffix.softs.index(first[0])])
                elif ";" in turkishSuffix.rule_set[turkishSuffix.types.index(_type)]:
                    if turkishSuffix.hards.index(letter) < 4:
                        self._word = self._old_word[:-1] + turkishSuffix.softs[turkishSuffix.hards.index(letter)]
            if letter in turkishSuffix.vowels:
                if i < 1:
                    if ":" in turkishSuffix.rule_set[turkishSuffix.types.index(_type)]:
                        if self._word.lower() in turkishSuffix.exceptions[turkishSuffix.types.index(_type)]:
                            first = first.replace("+", "y")
                        else:
                            first = first.replace("+", "n")
                    else:
                        first = first.replace("+", "y")
                first = first.replace("+", "")
                self._suffix = first + turkishSuffix.suffixes[index + turkishSuffix.vowels.index(letter)
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
