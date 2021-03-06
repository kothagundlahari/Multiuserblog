import os
import jinja2
import webapp2
import re


template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir),
                               autoescape=True)


class Handler(webapp2.RequestHandler):

    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))

    def valid_username(self, username):
        USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
        return username and USER_RE.match(username)

    def valid_password(self, password):
        PASS_RE = re.compile(r"^.{3,20}$")
        return password and PASS_RE.match(password)

    def valid_email(self, email):
        EMAIL_RE = re.compile(r'^[\S]+@[\S]+\.[\S]+$')
        return not email or EMAIL_RE.match(email)


class SignUp(Handler):

    def get(self):
        self.render("signup.html")

    def post(self):
        have_error = False
        username = self.request.get('username')
        password = self.request.get('password')
        verify = self.request.get('verify')
        email = self.request.get('email')

        params = dict(username=username,
                      email=email)

        if not self.valid_username(username):
            params['error_username'] = "That's not a valid username."
            have_error = True
            print "username"

        if not self.valid_password(password):
            params['error_password'] = "That wasn't a valid password."
            have_error = True
            print "password"
        if password != verify:
            params['error_verify'] = "the passwords don't match"
            have_error = True

        if not self.valid_email(email):
            params['error_email'] = "That's not a valid email."
            have_error = True
            print "email"

        if have_error:
            self.render('signup.html', **params)
        else:
            self.redirect('/welcome?username=' + username)


class WelcomePage(Handler):

    def get(self):
        username = self.request.get('username')

        if self.valid_username(username):
            self.render('welcome.html', username=username)
        else:
            self.redirect('/signup')


app = webapp2.WSGIApplication(
    [('/', SignUp), ('/welcome', WelcomePage)], debug=True)
