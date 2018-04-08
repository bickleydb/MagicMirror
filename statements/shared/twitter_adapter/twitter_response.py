class twitterResponse():

    def __init__(self, jsonData):
        self.tweetList = []
        self.raw_json = jsonData
        self.index = 0

        for tweet_json in jsonData:
            self.tweetList.append(tweet(tweet_json))

    def get_json(self):
        return self.raw_json
    
    def __iter__(self):
        return self

    def __next__(self):
        if(self.index == len(self.tweetList)):
            self.index = 0
            raise StopIteration
        self.index =  self.index + 1
        return self.tweetList[self.index-1]

    def __str__(self):
        return_str=""
        for result in self:
            return_str = return_str + str(result) + "\n"
        return return_str

    def get_list(self):
        return self.tweetList

class tweet():
    def __init__(self, status_data):
        print(status_data)
        self.backing_status = status_data

        self.tweet_id = status_data.id_str
        self.fav_count = status_data.favorite_count
        self.source = status_data.source
        self.text = status_data.text
        self.author = status_data.user.screen_name
  
    def __str__(self):
        return "" + str(self.source) + "; " + str(self.author)

    def get_id(self):
        return self.tweet_id

    def get_favs(self):
        return self.fav_count

    def get_source(self):
        return self.source

    def get_text(self):
        return self.text
    
    def get_author(self):
        return self.author
    
    def get_site(self):
        return "TW"
    
    def get_subsite(self):
        return "@"+self.get_author()