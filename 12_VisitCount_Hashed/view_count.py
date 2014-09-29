import webapp2
import hmac
secret="googleappengine"


def hash_str(s):
	return hmac.new(secret,s).hexdigest()

def make_secure_val(s):
	return "%s|%s" %(s,hash_str(s))

def check_secure_val(h):
	value=h.split('|')[0]
	if h == make_secure_val(value):
		return value

#Mainpage handler
class MainPage(webapp2.RequestHandler):
	def get(self):

		self.response.headers['Content-Type'] = 'text/plain'
		visits=0
		visits_cookies_str = self.request.cookies.get('visits','0')				#0 is default value, if visits var not found

		if visits_cookies_str:
			cookie_val = check_secure_val(visits_cookies_str)
			if cookie_val:
				visits=int(cookie_val)
		

		visits=visits+1
		self.response.write("You've been here %s times!" % visits)
		 
		new_cookie_val = make_secure_val(str(visits))
		self.response.headers.add_header('Set-Cookie', 'visits=%s' % new_cookie_val)


app = webapp2.WSGIApplication([
    			('/', MainPage)
					], debug=True)