import webapp2
import os
import jinja2
import cgi



#Setup Jinja2
template_dir = os.path.join(os.path.dirname(__file__),'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),autoescape = True)

class Handler(webapp2.RequestHandler):
	def write(self, *a, **kw):
		self.response.write(*a,**kw)

	def render_str(self, template, **params):
		t = jinja_env.get_template(template)
		return t.render(params)

	def render(self, template, **kw):
		self.write(self.render_str(template, **kw))





class MainPage(Handler):
	def get(self):
		self.render("home.html")

	#Invoked when form is submitted.
	def post(self):
		self.response.headers['Content-Type'] = 'text/html'
		#self.response.write(self.request)

		#Let us render the form's output here.
		name = self.request.get("name")
		text = self.request.get("thoughts")


		#BEFORE Jinja2
		#self.response.write("<h4>My name is %s </h4>"% cgi.escape(name,quote = 'True' ))
		#self.response.write('<p indent= "1"> %s </p> <br>' % cgi.escape(text, quote = 'True'))	
		#Alternatively, render a post like this - STRING SUBSTITUTION
		#self.response.write(post_html % {"name":cgi.escape(name,quote = 'True' ),
		#																				 "thoughts":cgi.escape(text, quote = 'True') })		

		self.render("post.html", name=cgi.escape(name,quote = 'True' ),
														 thoughts=cgi.escape(text, quote = 'True'))



class EditPage(Handler):
	
	#Gets invoked upon opening the /edit page.
	def get(self):
		self.response.headers['Content-Type'] = 'text/html'
		self.render("edit.html")
		#self.response.write(self.request)

		


application = webapp2.WSGIApplication([('/',MainPage),
																			 ('/edit/',EditPage)
																			], debug = True)