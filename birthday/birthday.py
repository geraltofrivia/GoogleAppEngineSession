"""A simple webapp2 server."""
form = """
<form  method = "post">
	What is your Birthday?
	<br>
	<label> Month	<input type = "text" name = "Month" value = "%(month)s">	</label>
	<label> Day <input type = "text" name = "Day" value = "%(day)s">	</label>
	<label> Year <input type = "text" name = "Year" value = "%(year)s">	</label>
	<div style="color: red">%(error)s</div>
	<br>
	<br>
	<input type = "submit">
</form>
"""

import webapp2
import cgi

def valid_year(year):
	if year and year.isdigit():
		year = int(year)
	if year >= 1900 and year <= 2020:
		return year
	return

def valid_day(day):
	days = range(32)
	day_v = []
	del days[0]
	for d in days:
		day_v.append(str(d))
	if day in day_v:
		return int(day)
	return

months = ['January',
  	'February',
  	'March',
  	'April',
  	'May',
  	'June',
  	'July',
  	'August',
  	'September',
  	'October',
  	'November',
  	'December']
          
def valid_month(month): 
	d = {}
	for m in months :
		d[m[:3].lower()] = m
	month = month.lower()
	if month[:3] in d:
		return d[month[:3]]
	return


class MainPage(webapp2.RequestHandler):

		def write_form(self, error='',month='',day='',year=''):
			self.response.out.write( form % {'error':error,
																			 'month':cgi.escape(month, quote = 'True'),
																			 'day':cgi.escape(day, quote = 'True'),
																			 'year':cgi.escape(year, quote = 'True')})
		
		def get(self):
			self.response.headers['Content-Type'] = 'text/html'
			self.write_form()

		def post(self):

			year = self.request.get('Year')
			month = self.request.get('Month')
			day = self.request.get('Day')
			cyear = valid_year(year)
			cmonth = valid_month(month)
			cday = valid_day(day)

			if cday and cmonth and cyear:
				#self.response.out.write('Thanks!')
				self.redirect("/thanks")
			else:
				#self.response.out.write('Month = '+month)
				#self.response.out.write('Day = '+str(day))
				#self.response.out.write('Year = '+str(year))
				
				self.write_form("This does not look good! Retry!",month,day,year)



class Thankshandler(webapp2.RequestHandler):

		def get(self):
			self.response.out.write("Thanks! That is a valid date")







application = webapp2.WSGIApplication([('/', MainPage),
																			 ('/thanks', Thankshandler),],
									 debug=True)
