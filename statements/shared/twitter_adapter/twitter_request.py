import requests
import json
import twitter
import statements.shared.twitter_adapter as shared
from . import twitter_response as tr


class twitter_request():
    urlPattern = "https://www.reddit.com/r/{}/{}/.json?limit={}?raw_json=1"

    def __init__(self, twitter_id):
        self.api_instance = twitter.Api(
            consumer_key=shared.get_consumer_key(),
            consumer_secret=shared.get_consumer_secret(),
            access_token_key=shared.get_access_token_key(),
            access_token_secret=shared.get_access_token_secret()
        )
        self.twitter_id = twitter_id

    def get_data(self):
        data = self.getTimeline()
        return tr.twitterResponse(data)
     
    def getTimeline(self):
        return self.api_instance.GetUserTimeline(screen_name=self.twitter_id,
                                                 exclude_replies=True)
