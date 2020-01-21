import json
import os
from .PathViews import *
from .Calendar import *

EnvConfigVars = {
    "GoogleApiKey": "GoogleApiKey"
}

if EnvConfigVars["GoogleApiKey"] in os.environ:
    GOOGLE_API_KEY = os.environ["GoogleApiKey"]
else:
    GOOGLE_API_KEY = ""
