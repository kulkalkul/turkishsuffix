import os
import collections

config = {}


class ConfigLoader:
    def __init__(self):
        executed = {}
        for file in os.scandir("config"):
            if file.path.endswith(".py"):
                name = file.name[:-3]
                executed[name] = {}
                exec(open(file.path, encoding='utf8').read(), executed[name])
                values = [value for value in executed[name] if value != "__builtins__"]
                Tuple = collections.namedtuple(name, values)
                config[name] = Tuple(*[executed[name][value] for value in values if value != "__builtins__"])


ConfigLoader()
