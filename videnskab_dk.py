import twitter
from email.utils import parsedate
import time
from email import utils
from models import Item, Feed
import http_get
from bs4 import BeautifulSoup
import re

consumer_key = "xxx"
consumer_secret = "xxx"
access_token_key = "xxx"
access_token_secret = "xxx"

api = twitter.Api(consumer_key, consumer_secret, access_token_key, access_token_secret)


def get_url(item):
    print item
    url = next(iter(filter(lambda x: "videnskab.dk" in x.expanded_url, item.urls)), None)
    if url is None:
        url = next(iter(filter(lambda x: "twitter.com/i/web/status" in x.expanded_url, item.urls)), None)
        scraped_url = scrape_links(url.expanded_url)
        if scraped_url is not None:
            return scraped_url
        else:
            return ""
    else:
        return url.expanded_url


def scrape_links(url):
    response = http_get.simple_get(url)
    if response is not None:
        html = BeautifulSoup(response, 'html.parser')
        for link in html.select('a.twitter-timeline-link'):
            if 'u-hidden' not in link['class']:
                return link['href']
    return None


def format_datetime(str):
    return utils.formatdate(time.mktime(parsedate(str)))


def tweet_to_item(tweet):
    return Item(tweet.id, tweet.text, get_url(tweet), format_datetime(tweet.created_at))


def is_from_videnskabdk(tweet):
    return tweet.user.screen_name == "videnskabdk"


def fetch():
    tweets = api.GetSearch(raw_query="q=videnskabdk")
    filtered = filter(lambda tweet: is_from_videnskabdk(tweet), tweets)
    items = list(map(lambda tweet: tweet_to_item(tweet), filtered))
    feed = Feed('Videnskabdk', items)
    return feed.to_string()
