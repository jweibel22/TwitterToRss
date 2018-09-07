import twitter
from email.utils import parsedate
import time
from email import utils

consumer_key = "xxx"                    
consumer_secret = "xxx"
access_token_key = "xxx"
access_token_secret = "xxx"

api = twitter.Api(consumer_key, consumer_secret, access_token_key, access_token_secret)
        
rss_template = '<?xml version="1.0" encoding="utf-8" ?><rss version="2.0" xml:base="https://identity-jweibel-88507.appspot.com/rss/videnskabdk" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:atom="http://www.w3.org/2005/Atom">' \
               '<channel>' \
               '<title>Videnskabdk</title>'\
                '<link>https://identity-jweibel-88507.appspot.com/rss/videnskabdk</link>'\
                '<description> </description>'\
                '<language>da</language>'\
                '<atom:link href = "https://identity-jweibel-88507.appspot.com/rss/videnskabdk" rel="self" type="application/rss+xml"/>'\
               '%s' \
               '</channel>' \
               '</rss>'

item_template = '<item>'\
'<title>%s</title>'\
'<link>%s</link>'\
'<description>%s</description>'\
'<guid isPermaLink="false">%s</guid>'\
'<pubDate>%s</pubDate>'\
'</item>'

def get_url(item):
    url = next(iter(filter(lambda x: "videnskab.dk" in x.expanded_url, item.urls)), None)
    if url is None:
        return ""
    else:
        return url.expanded_url

def formatDateTime(str):
    return utils.formatdate(time.mktime(parsedate(str)))

def tweetToItem(tweet):
    return item_template % (tweet.text, get_url(tweet), "", tweet.id, formatDateTime(tweet.created_at))

def is_from_videnskabdk(tweet):
    return tweet.user.screen_name == "videnskabdk"

def fetch():
    tweets = api.GetSearch(raw_query="q=videnskabdk")
    filtered = filter(lambda tweet: is_from_videnskabdk(tweet), tweets)
    items = list(map(lambda tweet: tweetToItem(tweet), filtered))
    return rss_template % "\n".join(items)
