import webapp2	#imports webapp2 module

form = """<form method="get" action="/answer/">
						<label> Value 1 </label>
						<input type="text" name="value1">
						<br>
						<label> Value 2 </label>
						<input type="text" name="value2">
						<br>
						<input type="submit">	
					</form>"""

back = """<form action="/">
						<input type="submit">
					</form>"""

#Home page handler which asks for value
class MainPage(webapp2.RequestHandler):
	def get(self):
		self.response.headers['Content-Type'] = 'text/html'
		self.response.write(form)
		

#New page handler which prints a result
class Answer(webapp2.RequestHandler):
	def get(self):
		value1 = int(self.request.get("value1"))
		value2 = int(self.request.get("value2"))
		self.response.headers['Content-Type'] = 'text/html'
		self.response.write(value1+value2)
		self.response.write(back)

#url handler application
app = webapp2.WSGIApplication([
    				('/', MainPage),
    				('/answer/', Answer)    
										], debug=True) 