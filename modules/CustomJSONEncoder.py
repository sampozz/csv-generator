# Imports
from json import JSONEncoder


class CustomJSONEncoder(JSONEncoder):

    def default(self, o):
        return o.__dict__