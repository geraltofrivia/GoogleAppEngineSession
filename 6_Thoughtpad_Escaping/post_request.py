import webapp2	#imports webapp2 module
import cgi

home_html = """
						<h1> Thoughtpad </h1>
						<p> The point of random scribbling is that it helps you clear your head </p>
						<div> 
							<a href="/edit/">
								<e> Let us </e> 
							</a>
						</div>	

						<!--Add post html here -->
						"""

edit_html = """
						<form method = "post">
						<label> name </label>
						<input name = "name" type = "text">
						<input type = "submit" value = "post">
						<br>
						<textarea name = "thoughts"> </textarea>
						<br>
						</form>
						"""









class MainPage(webapp2.RequestHandler):
	def get(self):
		self.response.headers['Content-Type'] = 'text/html'
		self.response.write(home_html)

		


class EditPage(webapp2.RequestHandler):
	#Gets invoked upon opening the /edit page.
	def get(self):
		self.response.headers['Content-Type'] = 'text/html'
		self.response.write(edit_html)
		#self.response.write(self.request)

	def post(self):
		self.response.headers['Content-Type'] = 'text/html'
		#self.response.write(self.request)

		#Let us render the form's output here.
		name = self.request.get("name")
		text = self.request.get("thoughts")

		#Uncomment to enable HTML Escaping
		#name = cgi.escape(name,quote="True")
		#text = cgi.escape(text,quote="True")

		self.response.write("<h4>My name is %s </h4>"% name)
		self.response.write('<p indent= "1"> %s </p> <br>' % text)

				
	


#url handler application
app = webapp2.WSGIApplication([
    				('/', MainPage),
    				('/edit/', EditPage)    
										], debug=True) 