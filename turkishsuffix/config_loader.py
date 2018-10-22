import os
import functools

config = {}

class ConfigLoader:
    def __init__(self):
        for file in os.scandir("config"):
            if file.path.endswith(".py"):
                name = file.name.replace(".py", "")
                config[name] = {}
                exec(open(file.path, encoding='utf8').read(), config[name])

ConfigLoader()
