import webapp2
import cgi
import re
import os
import urllib2
from xml.dom import minidom
from google.appengine.api import users


from google.appengine.ext import db
#here i am declaring form variable
form="""
<form method="post">
<input type="submit">
</form>
"""


class MainPage(webapp2.RequestHandler):

    def get(self):
        # Checks for active Google account session
        user = users.get_current_user()

        #if found display its user name... whatelse can we do from the user ??
        if user:
            self.response.write('Hello, ' + user.nickname())
            self.response.write(form)
        else:#if not .. direct the user to the login page of gmail and after user has logged in .. redirect him/her to the original page
            self.redirect(users.create_login_url(self.request.uri))

    def post(self):
    	self.redirect(users.create_logout_url('/LoggedOut'))



class LoggedOut(webapp2.RequestHandler):
	def get(self):
		self.response.write("you are logged out")



app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/LoggedOut',LoggedOut)
], debug=True)


