import http_get
from bs4 import BeautifulSoup
import re
from models import Item
import datetime
from models import Feed


def scrape_links():
    url = 'https://www.bbc.co.uk/news/topics/cm8m1391ddrt/news-daily'
    response = http_get.simple_get(url)
    if response is not None:
        html = BeautifulSoup(response, 'html.parser')
        for link in html.select('a.qa-heading-link'):
            m = re.match(r"^/news/uk-([\w]+)\?intlink", link['href'])
            item = Item(m.group(1), link.find('span').text, "https://www.bbc.co.uk{href}".format(href=link['href']),
                        datetime.datetime.now().strftime("%a, %d %b %Y %H:%M:%S %z"))
            yield item


def scrape():
    feed = Feed('BBC Daily News', scrape_links())
    return feed.to_string()

