import webapp2	#imports webapp2 module

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
						<form method = "get">
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
		self.response.write(self.request)

		#Add a show post handler function here
		#Move showpost to frontpage. Form -> Action
		





#url handler application
app = webapp2.WSGIApplication([
    				('/', MainPage),
    				('/edit/', EditPage)    
										], debug=True) 