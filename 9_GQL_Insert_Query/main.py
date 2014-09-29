import webapp2			#Our web application framework
import os						#To Fetch filename of Template directory
import jinja2 			#To Render HTML Easily. Template API

from google.appengine.ext import ndb 		#Importing the datastore API


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


#Create table.
class Thoughts(ndb.Model):
	name = ndb.StringProperty()
	thought = ndb.TextProperty(required = True)
	created = ndb.DateTimeProperty(auto_now_add = True)


#Home page
class MainPage(Handler):	
	def get(self):
		self.render("home.html")
		#Query the database
		posts = ndb.gql("SELECT * FROM Thoughts ORDER BY created DESC")
		for post in posts:
			self.render("post.html", name=post.name,
														   thoughts=post.thought)
			#self.write("Key = %s" %post.key)


	#Invoked when form is submitted.
	def post(self):
		self.response.headers['Content-Type'] = 'text/html'
		username = self.request.get("name")
		text = self.request.get("thoughts")

		#Insert the thought in our entity (table)
		entry = Thoughts(name = username, thought = text)
		entry.put()
		
		#Query the database
		posts = ndb.gql("SELECT * FROM Thoughts ORDER BY created DESC")
		for post in posts:
			self.render("post.html", name=post.name,
														 thoughts=post.thought)


#Page used to edit/compose a thought
class EditPage(Handler):
	#Gets invoked upon opening the /edit page.
	def get(self):
		self.response.headers['Content-Type'] = 'text/html'
		self.render("edit.html")
		#self.response.write(self.request)


application = webapp2.WSGIApplication([('/',MainPage),
																			 ('/edit/',EditPage)
																			], debug = True)