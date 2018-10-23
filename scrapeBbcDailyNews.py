from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
import datetime
import re

rss_template = '<?xml version="1.0" encoding="utf-8" ?><rss version="2.0" xml:base="https://identity-jweibel-88507.appspot.com/rss/bbcdailynews" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:atom="http://www.w3.org/2005/Atom">' \
               '<channel>' \
               '<title>BBC Daily News</title>'\
                '<link>https://identity-jweibel-88507.appspot.com/rss/bbcdailynews</link>'\
                '<description> </description>'\
                '<language>da</language>'\
                '<atom:link href = "https://identity-jweibel-88507.appspot.com/rss/bbcdailynews" rel="self" type="application/rss+xml"/>'\
               '%s' \
               '</channel>' \
               '</rss>'



def simple_get(url):
    """
    Attempts to get the content at `url` by making an HTTP GET request.
    If the content-type of response is some kind of HTML/XML, return the
    text content, otherwise return None.
    """
    try:
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None

    except RequestException as e:
        print('Error during requests to {0} : {1}'.format(url, str(e)))
        return None


def is_good_response(resp):
    """
    Returns True if the response seems to be HTML, False otherwise.
    """
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200
            and content_type is not None
            and content_type.find('html') > -1)


class Item:

    def __init__(self, id, title, url):
        self.id = id
        self.title = title
        self.url = url
        self.item_template = '<item>'\
'<title>%s</title>'\
'<link>%s</link>'\
'<description>%s</description>'\
'<guid isPermaLink="false">%s</guid>'\
'<pubDate>%s</pubDate>'\
'</item>'

    def to_string(self):
        return self.item_template % (self.title, self.url, "", self.id,
                                     datetime.datetime.now().strftime("%a, %d %b %Y %H:%M:%S %z"))


def scrape_links():
    url = 'https://www.bbc.co.uk/news/topics/cm8m1391ddrt/news-daily'
    response = simple_get(url)
    if response is not None:
        html = BeautifulSoup(response, 'html.parser')
        for link in html.select('a.qa-heading-link'):
            m = re.match(r"^/news/uk-([\w]+)\?intlink", link['href'])
            item = Item(m.group(1), link.find('span').text, "https://www.bbc.co.uk{href}".format(href=link['href']))
            yield item.to_string()


def scrape():
    return rss_template % "\n".join(scrape_links())

