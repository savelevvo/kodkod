import json


class JsonConfig:
    def __init__(self, path):
        self.conf = json.load(open(path))

    def __getitem__(self, item):
        return self.conf[item]
