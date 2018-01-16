import requests
import json

class comment_request:
    
    
    urlPattern = "https://www.reddit.com/r/{}/comments/article/.json?article={}&sort={}&truncate={}&depth={}"

    def __init__(self, subreddit="all", sort="hot",depth=1,truncate=2,article=""):
        self.article = article
        self.truncate = truncate
        self.sort = sort
        self.depth = depth
        self.subreddit = subreddit


    def __str__(self):
        return self.urlPattern.format(self.subreddit,self.article, self.sort,self.truncate,self.depth)

    def get_data(self):
        responseObject = json.loads(requests.get(str(self),{'User-agent': 'magicMirror 0.02'}).text)
        return responseObject
    



    
