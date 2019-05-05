import os


if "MagicMirrorCredDirectory" not in os.environ:
    CREDENTIAL_DIRECTORY = os.path.dirname(os.path.realpath(__file__))
else:
    CREDENTIAL_DIRECTORY = os.environ["MagicMirrorCredDirectory"]

if "MagicMirrorAppCredDirectory" not in os.environ:
    APP_SECRET_DIRECTORY = os.path.dirname(os.path.realpath(__file__))
else:
    APP_SECRET_DIRECTORY = os.environ["MagicMirrorAppCredDirectory"] + "appCredentials.json"