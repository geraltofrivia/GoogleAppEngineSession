import webapp2	#imports webapp2 module

class MainPage(webapp2.RequestHandler):
	def get(self):
		self.response.headers['Content-Type'] = 'text/plain'
		self.response.write(self.request)	#the "information" that server gives to 

#url handler application
app = webapp2.WSGIApplication([
    				('/', MainPage)    
										], debug=True) 