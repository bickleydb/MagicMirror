import json
from . import SubredditThread

class subreddit_response():

    def __init__(self, backingJSON):
        self.raw_json = backingJSON
        data =  self.raw_json["data"]
        list_of_children =  data["children"]

        self.threadList = []
        for jsonThread in list_of_children:
            thread = jsonThread["data"]
            self.threadList.append(SubredditThread.subreddit_thread(thread))
        self.index = 0

    def get_json(self):
        return self.raw_json
    
    def __iter__(self):
        return self

    def __next__(self):
        if(self.index == len(self.threadList)):
            self.index = 0
            raise StopIteration
        self.index =  self.index + 1
        return self.threadList[self.index-1]

    def __str__(self):
        return_str=""
        for result in self:
            return_str = return_str + str(result) + "\n"
        return return_str

    def get_list(self):
        return self.threadList