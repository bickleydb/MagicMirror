import json
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
USER_AGENT = os.environ.get("UserAgentString") or ''
NUM_POSTS = os.environ.get("NumberPosts") or ''
