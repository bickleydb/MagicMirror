import json
import os

DIR_PATH = os.path.dirname(os.path.realpath(__file__))

EnvConfigVars = {
    "WeatherPrivateKey": "WeatherPrivateKey",
    "ZipCode": "ZipCode",
    "CountryCode": "CountryCode",
}

if EnvConfigVars["WeatherPrivateKey"] in os.environ:
    APP_KEY = os.environ["WeatherPrivateKey"]
else:
    APP_KEY = ""

if EnvConfigVars["ZipCode"] in os.environ:
    ZIP_CODE = os.environ["ZipCode"]
else:
    ZIP_CODE = ""

if EnvConfigVars["CountryCode"] in os.environ:
    COUNTRY_CODE = os.environ["CountryCode"]
else:
    COUNTRY_CODE = ""
