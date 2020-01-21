import json
import os

DIR_PATH = os.path.dirname(os.path.realpath(__file__))

EnvConfigVars = {
    "TwitterConsumerKey": "TwitterConsumerKey",
    "TwitterConsumerSecret": "TwitterConsumerSecret",
    "TwitterAccessTokenKey": "TwitterAccessTokenKey",
    "TwitterAccessTokenSecret": "TwitterAccessTokenSecret",
}


if EnvConfigVars["TwitterConsumerKey"] in os.environ:
    CONSUMER_KEY = os.environ["TwitterConsumerKey"]
else:
    CONSUMER_KEY = ""

if EnvConfigVars["TwitterConsumerSecret"] in os.environ:
    CONSUMER_SECRET = os.environ["TwitterConsumerSecret"]
else:
    CONSUMER_SECRET = ""

if EnvConfigVars["TwitterAccessTokenKey"] in os.environ:
    ACCESS_TOKEN_KEY = os.environ["TwitterAccessTokenKey"]
else:
    ACCESS_TOKEN_KEY = ""

if EnvConfigVars["TwitterAccessTokenSecret"] in os.environ:
    ACCESS_TOKEN_SECRET = os.environ["TwitterAccessTokenKey"]
else:
    ACCESS_TOKEN_SECRET = ""


def get_consumer_key():
    key = CONSUMER_KEY
    return parseSecret(key)


def get_consumer_secret():
    key = CONSUMER_SECRET
    return parseSecret(key)


def get_access_token_key():
    key = ACCESS_TOKEN_KEY
    return parseSecret(key)


def get_access_token_secret():
    key = ACCESS_TOKEN_SECRET
    return parseSecret(key)


def parseSecret(secretString):
    return secretString.encode('utf-8')