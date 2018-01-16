import requests
import json
import twitter

import statements.shared as shared
from . import twitter_response as tr

class twitter_request():
    urlPattern = "https://www.reddit.com/r/{}/{}/.json?limit={}?raw_json=1"

    def __init__(self, twitter_id):
        self.api_instance = twitter.Api(
            consumer_key = shared.twitter_adapter.CONSUMER_KEY,
            consumer_secret = 	shared.twitter_adapter.CONSUMER_SECRET,
            access_token_key = shared.twitter_adapter.ACCESS_TOKEN_KEY,
            access_token_secret = shared.twitter_adapter.ACCESS_TOKEN_SECRET,
        )
        self.twitter_id = twitter_id

    def get_data(self):
        data = self.getTimeline()
        return  tr.twitterResponse(data)
     
    def getTimeline(self):
        return self.api_instance.GetUserTimeline(screen_name=self.twitter_id)
