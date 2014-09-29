import webapp2

#Mainpage handler
class MainPage(webapp2.RequestHandler):
	def get(self):

		self.response.headers['Content-Type'] = 'text/plain'
		visits = self.request.cookies.get('visits','0')				#0 is default value, if visits var not found
		if visits.isdigit():
			visits = int(visits) + 1
		else:
			visits = 0
		self.response.write(" You have been here %s times!\n\n" % visits)
		self.response.headers.add_header('Set-cookie', 'visits=%s' %visits)
		self.response.write(self.request)

application = webapp2.WSGIApplication([
    			('/', MainPage)
					], debug=True)