import json
import os

DIR_PATH = os.path.dirname(os.path.realpath(__file__))

APP_KEY = os.environ["WeatherPrivateKey"]
ZIP_CODE = os.environ["ZipCode"]
COUNTRY_CODE = os.environ["CountryCode"]
