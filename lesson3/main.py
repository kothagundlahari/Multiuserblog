
import webapp2


class Handler(webapp2.RequestHandler):

    def write(self, *a, **kw):
        self.response.write(*a, **kw)


class MainHandler(Handler):

    def get(self):
        self.write('just for the heck. why not?')

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
