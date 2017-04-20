
import webapp2


class MainHandler(webapp2.RequestHandler):

    def get(self):
        self.response.write('just for the heck. why not?')

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
