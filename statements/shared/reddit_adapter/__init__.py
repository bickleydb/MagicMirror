import json
import os

dir_path = os.path.dirname(os.path.realpath(__file__))

def load_configuration(filename="/configuration.json"):
    config_file = open(dir_path + filename, 'r')
    return json.loads(config_file.read())

CONFIG_DATA = load_configuration()
USER_AGENT = CONFIG_DATA["UserAgentString"]
NUM_POSTS = CONFIG_DATA["NumberPosts"]
