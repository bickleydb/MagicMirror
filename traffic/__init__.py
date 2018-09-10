import json
import os

DIR_PATH = os.path.dirname(os.path.realpath(__file__))

def load_configuration(filename="/configuration.json"):
    config_file = open(DIR_PATH + filename, 'r')
    return json.loads(config_file.read())

CONFIG_DATA = load_configuration()
GOOGLE_API_KEY = CONFIG_DATA["GoogleApiKey"]

