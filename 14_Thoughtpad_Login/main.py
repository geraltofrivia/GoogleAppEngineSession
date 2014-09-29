import webapp2			#Our web application framework
import os						#To Fetch filename of Template directory
import jinja2 			#To Render HTML Easily. Template API

from google.appengine.ext import ndb 		#Importing the datastore API
from google.appengine.api import users		#Importing Google user from Google API


#Setup Jinja2
template_dir = os.path.join(os.path.dirname(__file__),'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),autoescape = True)


#Handler class which has few utility function for easy rendering and printing
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
	user_id=ndb.StringProperty()		#This stores user object retrived from google user
	name = ndb.StringProperty()
	thought = ndb.TextProperty(required = True)
	created = ndb.DateTimeProperty(auto_now_add = True)


#Home page
class MainPage(Handler):	
	def get(self):
		user = users.get_current_user()		#Checks for active Google account session
		temp_counter=0;
		if user:
			self.render("home.html")
			posts = ndb.gql("SELECT * FROM Thoughts ORDER BY created DESC")

			user_id=str(user.user_id())
			self.response.headers.add_header('Set-Cookie', 'user_cookie=%s' %user_id)


			for post in posts:
				self.write(post.user_id)
				if post.user_id==str(user.user_id()):
					self.render("post.html", name=post.name,
														   thoughts=post.thought)
					#Every entry is indexed by GAE Datastore.
		
					#self.write("Key = %s" %post.key.id())
		else:
			self.redirect(users.create_login_url(self.request.uri))			

	#Invoked when form is submitted.
	def post(self):

		self.response.headers['Content-Type'] = 'text/html'
		username = self.request.get("name")
		text = self.request.get("thoughts")
		user_cookie_id=str(self.request.cookies.get('user_cookie'))
		print user_cookie_id
		#Now I need to find which google user does this id relate to 
#		if user_cookie_id:
#			user_db=ndb.gql("SELECT * FROM Thoughts")
#			for node in user_db:
#				if node.user_obj.user_id()==user_cookie_id:
#					print "Hello"
#					user_object=node.user_obj
		#Insert the thought in our entity (table)


		entry = Thoughts(name = username, thought = text,user_id=user_cookie_id)
		entry.put()
		self.redirect('/')
		
		#Query the database
#		posts = ndb.gql("SELECT * FROM Thoughts ORDER BY created DESC")
#		for post in posts:
#			self.render("post.html", name=post.name,
#														 thoughts=post.thought)


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