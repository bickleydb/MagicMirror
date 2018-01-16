import requests
import json
import statements.shared

from statements.shared.request import statement_request
from statements.shared.reddit_adapter import SubredditResponse
import statements.shared.reddit_adapter

class SubredditRequest(statement_request):
    urlPattern = "https://www.reddit.com/r/{}/{}/.json?limit={}?raw_json=1"

    def __init__(self, subreddit="all", queryType="hot",limit=statements.shared.reddit_adapter.NUM_POSTS ,startingPoint=0):
        self.subreddit = subreddit
        self.query_type = queryType
        self.limit = limit
        self.count = startingPoint

    def __str__(self):
        return self.urlPattern.format(
            self.subreddit,
            self.query_type,
            self.limit
        )

    def get_data(self):
        response_object = json.loads(
            requests.get(str(self),
                         headers={'User-agent':
                                  statements.shared.reddit_adapter.USER_AGENT
                                 }
                        ).text)
        return SubredditResponse.subreddit_response(response_object)

    def get_site(self):
        return "RE"

    def get_subsite(self):
        return self.subreddit
