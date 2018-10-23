import webapp2
from twitterrss import fetch
from scrapeBbcDailyNews import scrape

class VidenskabDk(webapp2.RequestHandler):

      def get(self):
          self.response.headers['Content-Type'] = 'application/rss+xml'
          self.response.write(fetch())


class BbcDailyNews(webapp2.RequestHandler):

    def get(self):
        self.response.headers['Content-Type'] = 'application/rss+xml'
        self.response.write(scrape())

app = webapp2.WSGIApplication([('/rss/videnskabdk', VidenskabDk), ('/rss/bbcdailynews', BbcDailyNews), ], debug=True)

#rss = fetch()
#print (rss)