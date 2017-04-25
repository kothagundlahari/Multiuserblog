import os
import jinja2
import webapp2
import string

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(template_dir), autoescape=True)


class Handler(webapp2.RequestHandler):

    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))


class MainHandler(Handler):

    def get_translation(self):
        return string.maketrans(
            "ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz",
            "NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm")

    def get(self):
        self.render("rot13.html")

    def post(self):
        word = str(self.request.get('text'))
        output = word.translate(self.get_translation())
        self.render('Rot13.html', text=output)


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)