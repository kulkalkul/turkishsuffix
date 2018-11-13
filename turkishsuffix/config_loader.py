import collections
import pkg_resources

config = {}


class ConfigLoader:
    def __init__(self):
        executed = {}
        for file in pkg_resources.resource_listdir(__name__, "config"):
            if file.endswith(".py"):
                name = file[:-3]
                path = pkg_resources.resource_filename(__name__, "config\\" + file)
                executed[name] = {}
                exec(open(path, encoding='utf8').read(), executed[name])
                values = [value for value in executed[name] if value != "__builtins__"]
                Tuple = collections.namedtuple(name, values)
                config[name] = Tuple(*[executed[name][value] for value in values if value != "__builtins__"])


ConfigLoader()
