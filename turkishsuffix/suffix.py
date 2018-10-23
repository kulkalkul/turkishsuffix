from .config_loader import config

settings = config["settings"]
exceptions = config["exceptions"]


# The main class.
class TurkishSuffix:
    """Main class for suffix classes.

    Arguments:
    _word                     - STRING  - The word which will get suffix.
    _type                     - STRING  - Name of the suffix.
    _possessive               - STRING  - Preferred possessive state for the possessive suffix.

    Returns:
    self._word + self._suffix - STRING  - Word with proper suffix.
    """
    def __init__(self, _word, _type=None, _possessive=None):
        self._word = self._old_word = _word
        self._suffix, self._type, self._possessive = None, None, None
        if _possessive is not None:
            self._set_possessive(_type, _possessive)
        elif _type is not None:
            self._set_suffix(_type)

    def _set_suffix(self, _type):
        """Private method that creates the word with suffixes.

        Arguments:
        _type                     - STRING  - Name of the suffix.

        Returns:
        vowel                     - STRING  - Proper vowel for the type and word.
        i                         - INTEGER - Index value of vowel in reversed word.
        """
        self._type = _type
        self._word = self._old_word
        rule_set = settings["rule_set"][settings["types"].index(_type)]
        index, division = int(rule_set[0]), int(rule_set[1])
        first, last = rule_set[2], rule_set[3]
        major = self._check_major()
        for i, letter in enumerate(self._old_word[::-1]):
            first = self._check_hards(rule_set, first, letter)
            if letter in settings["vowels"]:
                first = self._check_vowel(rule_set, first, _type, i)
                vowel = settings["suffixes"][index + settings["vowels"].index(letter) // 2 % division + major]
                self._suffix = first.replace("-", "").replace("+", "") + vowel + last.replace("-", "")
                return vowel, i

    def _set_possessive(self, _type, _possessive):
        """Private method that creates the word with possessive suffixes.

        Arguments:
        _type                     - STRING  - Name of the suffix.
        _possessive               - STRING  - Possessive state of the suffix.
        """
        self._possessive = _possessive
        possessive = settings["possessive"][int(_possessive[1].replace("t", "0").replace("ç", "3"))
                                       + int(_possessive[0]) - 1]
        if ";" in possessive:
            self._set_suffix("çokluk")
            plural = TurkishSuffix(self._suffix, "iyelik")
            self._suffix = plural.get_word()
        else:
            vowel, i = self._set_suffix("iyelik")
            first, last = possessive[0], possessive[1]
            rule_set = settings["rule_set"][settings["types"].index(_type)]
            if i < 1 and self._word.lower() not in exceptions[_type] and ":" not in possessive and "," not in possessive:
                self._suffix = first.replace("-", "").replace("+", "") + last.replace("-", "")
            else:
                self._suffix = first.replace("-", "").replace("+", "") + vowel + last.replace("-", "")
            if i > 0 or self._word.lower() in exceptions[_type] or "," in possessive:
                if self._word.lower() in exceptions[_type]:
                    possessive = possessive.replace(",", "")
                consonant = self._check_vowel(possessive, rule_set[2], _type, i)
                if ":" in possessive:
                    self._suffix = vowel + self._suffix
                self._suffix = consonant.replace("-", "").replace("+", "") + self._suffix

    def _check_hards(self, _rule_set, _first, _letter):
        """Private method that checks hard consonants and do necessary changes.

        Arguments:
        _rule_set                 - STRING  - Rule-set of the type.
        _first                    - STRING  - First letter from the rule-set.
        _letter                   - STRING  - Last vowel of the word.

        Returns:
        _first                    - STRING  - First letter from the rule-set with hard check.
        """
        if _letter in settings["hards"]:
            if _first[0] in "cd":
                _first = _first.replace(_first[0], settings["hards"][settings["softs"].index(_first[0])])
            elif ";" in _rule_set:
                if settings["hards"].index(_letter) < 4:
                    self._word = self._old_word[:-1] + settings["softs"][settings["hards"].index(_letter)]
        return _first

    def _check_vowel(self, _rule_set, _first, _type, _i):
        """Private method that checks vowels and add "kaynaştırma" consonant.

        Arguments:
        _rule_set                 - STRING  -Rule-set of the type.
        _first                    - STRING  - First letter from the rule-set.
        _type                     - STRING  - Name of the suffix.
        _i                        - INTEGER - Index value of vowel in reversed word.

        Returns:
        _first                    - STRING  - First letter from the rule-set with vowel check.
        """
        if _i < 1:
            if ":" in _rule_set:
                if self._word.lower() in exceptions[_type]:
                    _first = _first.replace("+", "y")
                else:
                    _first = _first.replace("+", "n")
            elif "," in _rule_set:
                _first = _first.replace("+", "s")
            else:
                _first = _first.replace("+", "y")
        return _first

    def _check_major(self):
        if self._word.lower() in exceptions["major_vowel_exception"]:
            return 1
        return 0

    def get_word(self, _type=None, _proper=False, _possessive=None):
        """Public method that returns the word with proper suffix and changes.
        This method can also apply other suffixes and cases.

        Arguments:
        _type                     - STRING  - Name of the suffix.
        _proper                   - BOOLEAN - Word is proper noun or not.
        _possessive               - STRING  - Preferred possessive state for the possessive suffix.

        Returns:
        self._word + self._suffix - STRING  - Word with proper suffix.
        """
        if _possessive is not None:
            self._set_possessive(_type, _possessive)
        elif _type is not None:
            self._set_suffix(_type)
        if _proper is True:
            return self._old_word + "'" + self._suffix
        return self._word + self._suffix

    def get_old_word(self):
        """Public method that returns the unchanged word.

        Returns:
        self._old_word            - STRING  - Unchanged word.
        """
        return self._old_word

    def get_suffix(self):
        """Public method that returns only the suffix.

        Returns:
        self._suffix              - STRING  - Suffix.
        """
        return self._suffix

    def get_type(self):
        """Public method that returns the suffix type.

        Returns:
        self._type                - STRING  - Name of the suffix.
        """
        return self._type

    def get_possessive(self):
        """Public method that returns possessive state of the suffix.

        Returns:
        self._possessive          - STRING  - Possessive state of the suffix.
        """
        return self._possessive
