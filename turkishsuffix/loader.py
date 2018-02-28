class TurkishSuffixConfig:
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


config = TurkishSuffixConfig()
