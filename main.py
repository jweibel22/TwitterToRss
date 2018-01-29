import webapp2
from twitterrss import fetch

class MainPage(webapp2.RequestHandler):

      def get(self):
          self.response.headers['Content-Type'] = 'application/rss+xml'
          self.response.write(fetch())

app = webapp2.WSGIApplication([('/rss/videnskabdk', MainPage),], debug=True)

#rss = fetch()
#print (rss)