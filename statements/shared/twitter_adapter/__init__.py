import json
import os

DIR_PATH = os.path.dirname(os.path.realpath(__file__))

CONSUMER_KEY = os.environ["TwitterConsumerKey"]
CONSUMER_SECRET = os.environ["TwitterConsumerSecret"],
ACCESS_TOKEN_KEY = os.environ["TwitterAccessTokenKey"],
ACCESS_TOKEN_SECRET = os.environ["TwitterAccessTokenSecret"],


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