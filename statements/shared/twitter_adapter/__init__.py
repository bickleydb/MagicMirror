import json
import os

DIR_PATH = os.path.dirname(os.path.realpath(__file__))

def load_configuration(filename="/configuration.json"):
    config_file = open(DIR_PATH + filename, 'r')
    return json.loads(config_file.read())


CONFIG_DATA = load_configuration()
CONSUMER_KEY = CONFIG_DATA["consumer_key"],
CONSUMER_SECRET = CONFIG_DATA["consumer_secret"],
ACCESS_TOKEN_KEY = CONFIG_DATA["access_token_key"],
ACCESS_TOKEN_SECRET = CONFIG_DATA["access_token_secret"],
