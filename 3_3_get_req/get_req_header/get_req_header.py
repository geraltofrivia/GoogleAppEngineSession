form='''<form>
	<input type="text" name="q" value="yolo"></input>
	<input type="submit"></input>
</form>'''

import webapp2	#imports webapp2 module

class MainPage(webapp2.RequestHandler):
	def get(self):
		#self.response.headers['Content-Type'] = 'text/plain'
		self.response.write(form)	#the form here is a variable defined in the first line
		q=self.request.get('q')
		self.response.write(self.request)


#url handler application
app = webapp2.WSGIApplication([
    				('/', MainPage)    
										], debug=True) 