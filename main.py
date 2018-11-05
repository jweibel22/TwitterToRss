import webapp2
from videnskab_dk import fetch
from bbc_daily_news import scrape

class VidenskabDk(webapp2.RequestHandler):

      def get(self):
          self.response.headers['Content-Type'] = 'application/rss+xml; charset=utf-8'
          self.response.write(fetch())


class BbcDailyNews(webapp2.RequestHandler):

    def get(self):
        self.response.headers['Content-Type'] = 'application/rss+xml; charset=utf-8'
        self.response.write(scrape())


app = webapp2.WSGIApplication([('/rss/videnskabdk', VidenskabDk), ('/rss/bbcdailynews', BbcDailyNews), ], debug=True)
