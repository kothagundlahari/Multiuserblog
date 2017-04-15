
import webapp2
form = """
<form method="post">
What is your Birthday?
<br>
<label>Month
<input type="text" name="month" value="%(month)s">
</label>
<label>Date
<input type="text" name="day" value="%(day)s">
</label>
<label>Year
<input type="text" name="year" value="%(year)s">
</label>
<div style= "color : red">%(error)s</div>

<br>
<br>
  <input <input type="submit">
</form>
"""


class MainHandler(webapp2.RequestHandler):
    def write_form(self,error="", month="", day="",year=""):
        self.response.out.write(form % {"error": error, "month":month,"day":day,"year":year})
    def valid_month(self,month):
        months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October','November','December']
        if month:
            cap_month = month.capitalize()
            if cap_month in months:
                return cap_month
    def valid_day(self,day):
        if day and day.isdigit():
            day = int(day)
        if day > 0 and day <= 31:
            return day
    def valid_year(self,year):
        if year and year.isdigit():
            year = int(year)
            if year > 1990 and year < 2020:
                return year

    def get(self):
        self.write_form()

    def post(self):
        user_month = self.request.get('month')
        user_day = self.request.get('day')
        user_year = self.request.get('year')


        month = valid_month(user_month)
        day = valid_day(user_day)
        year = valid_year(user_year)

        if not(month and day and year):
            self.write_form("This is not a valid statement ", user_month, user_day, user_year)
        else:
            self.response.out.write("Thanks. This is a valid syntax")


app = webapp2.WSGIApplication([('/', MainHandler)], debug=True)
