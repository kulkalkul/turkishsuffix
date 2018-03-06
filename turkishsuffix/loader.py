# Config class which loads every value from config.
class TurkishSuffixConfig:
    def __init__(self):
        import configparser, json, pkg_resources
        path = pkg_resources.resource_filename(__name__, "config.ini")
        config = configparser.ConfigParser()
        config.read_file(open(path, "r", encoding="utf-8"))
        # Dynamic config loading.
        for value in config.options("Settings"):
            setattr(self, value, json.loads(config.get("Settings", value)))
        self.exceptions = []
        for i, exception in enumerate(self.types):
            try:
                self.exceptions.append(json.loads(config.get("Exceptions", exception)))
            except configparser.NoOptionError:
                self.exceptions.append(None)


config = TurkishSuffixConfig()
