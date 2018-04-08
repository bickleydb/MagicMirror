import json

class subreddit_thread():

    def get_text(self):
        return self.get_title()
  
    def get_site(self):
        return "RE"

    def get_subsite(self):
        return self.get_subreddit()

    def __init__(self, backingJSON):
        self.stats = reddit_stats(
            score=backingJSON['score'],
            ups=backingJSON['ups'],
            downs=backingJSON['downs'],
            num_comments=backingJSON['num_comments'])

        self.text_info = thread_text(
            text=backingJSON['selftext'],
            html_text=backingJSON['selftext_html'],
            title=backingJSON['title'])

        self.metadata = thread_metadata(
            post_id=backingJSON['id'],
            post_name=backingJSON['name'], 
            author=backingJSON['author'], 
            created_time=backingJSON['created'], 
            is_censored=backingJSON['over_18'], 
            is_spoiler=backingJSON['spoiler'], 
            has_visited=backingJSON['visited'])

        self.links = thread_links(
            url=backingJSON['url'],
            permaLink=backingJSON['permalink']
        )

        self.subreddit = subreddit_metadata(
            subreddit=backingJSON['subreddit'],
            id=backingJSON["subreddit_id"]
        )

        self.title = self.text_info.text

    def get_subreddit(self):
        return self.subreddit.get_subreddit()

    def get_subreddit_id(self):
        return self.subreddit.subreddit_id()

    def get_html_text(self):
        return self.text_info.get_html_text()

    def get_title(self):
        return self.text_info.get_title()

    def get_post_id(self):
        return self.metadata.get_post_id()

    def get_author(self):
        return self.metadata.get_author()

    def get_create_time(self):
        return self.metadata.get_create_time()

    def get_is_censored(self):
        return self.metadata.get_is_censored()

    def get_post_name(self):
        return self.metadata.get_post_name()

    def get_is_spoiler(self):
        return self.metadata.get_is_spoiler()

    def get_has_been_visited(self):
        return self.metadata.get_has_been_visited()

    def get_url(self):
        return self.links.get_url()

    def get_permalink(self):
        return self.links.get_permalink()

    def __str__(self):
        return self.get_author() + " on " + self.get_subreddit() + "\n" + self.get_title() + "\n" + self.get_text()

class thread_text:

    def __init__(self, text="", html_text="", title="" ):
        self.text = text 
        self.html_text = html_text
        self.title = title

    def get_text(self):
        return self.text

    def get_html_text(self):
        return self.html_text

    def get_title(self):
        return self.title

class thread_metadata:
    def __init__(self, post_id="",post_name="",author="",created_time=0,is_censored=False,is_spoiler=False,has_visited=False,):
        self.post_id = post_id
        self.author = author
        self.created_time = created_time
        self.is_censored = is_censored
        self.is_spoiler = is_spoiler
        self.has_visited = has_visited
        self.post_name = post_name

    def get_post_id(self):
        return self.post_id

    def get_author(self):
        return self.author

    def get_create_time(self):
        return self.created_time

    def get_is_censored(self):
        return self.is_censored

    def get_is_spoiler(self):
        return self.is_spoiler

    def get_has_been_visited(self):
        return self.has_visited

    def get_post_name(self):
        return self.post_name

class thread_links:

    def __init__(self, url="", permaLink=""):
        self.url = url
        self.permalink = permaLink

    def get_permalink(self):
        return self.permalink

    def get_url(self):
        return self.url

class subreddit_metadata:
    def __init__(self, subreddit="", id=""):
        self.subreddit=subreddit
        self.subreddit_id=id
    
    def get_subreddit(self):
        return self.subreddit

    def get_subreddit_id(self):
        return self.subreddit_id

class reddit_stats:

    total_score = 0
    num_up_votes = 0
    num_down_votes = 0
    num_comments = 0


    def __init__(self, score=0, ups=0, downs=0, num_comments=0):
        self.total_score = score
        self.num_up_votes = ups
        self.num_down_votes = downs
        self.num_comments = num_comments

    def get_total_score(self):
        return self.total_score

    def get_num_up_votes(self):
        return self.num_up_votes

    def get_num_down_votes(self):
        return self.num_down_votes

    def get_num_comments(self):
        return self.num_comments