import cgi
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from models import *

class testRoot(webapp.RequestHandler):
    def get(self):
        self.response.out.write("This is the root of the fb api.")

class fbUserHandler(webapp.RequestHandler):
    def get(self):
        self.response.out.write("Get!\n")
        if self.request.get('fb_id'):
            fb_id = cgi.escape(self.request.get('fb_id'))
            results = fbUser.gql("WHERE fb_id = :1", int(fb_id))
        else:
            results = fbUser.all()
        if results.get() ==None : self.response.out.write("NOTHING FOUND\n")
        else:
            for result in results:
                self.response.out.write(result.to_xml())

    def post(self):
        fb_id = cgi.escape(self.request.get('fb_id'))
        results = fbUser.gql("WHERE fb_id = :1", fb_id)
        if results.get() == None:
            # Create a new user
            newUser = fbUser()
            newUser.fb_id = int(cgi.escape(self.request.get('fb_id')))
            newUser.lname = cgi.escape(self.request.get('lname'))
            newUser.fname = cgi.escape(self.request.get('fname'))
            if self.request.get('email'):
                newUser.email = cgi.escape(self.request.get('email'))
            newUser.location = cgi.escape(self.request.get('location'))
            if self.request.get('interest_locations'):
                newUser.interest_locations = cgi.escape(self.request.get('interest_locations')).split(',')
            if self.request.get('skills'):            
                newUser.skills = cgi.escape(self.request.get('skills')).split(',')
            if self.request.get('interests'):            
                newUser.interests = cgi.escape(self.request.get('interests')).split(',')
            newUser.contact_preferences = cgi.escape(self.request.get('contact_preferences'))
            newUser.put()
        else:
            user = results.get()
            user.fb_id = int(cgi.escape(self.request.get('fb_id')))
            user.lname = cgi.escape(self.request.get('lname'))
            user.fname = cgi.escape(self.request.get('fname'))
            if self.request.get('email'):
                user.email = cgi.escape(self.request.get('email'))
            user.location = cgi.escape(self.request.get('location'))
            if self.request.get('interest_locations'):
                user.interest_locations = cgi.escape(self.request.get('interest_locations')).split(',')
            if self.request.get('skills'):            
                user.skills = cgi.escape(self.request.get('skills')).split(',')
            if self.request.get('interests'):            
                user.interests = cgi.escape(self.request.get('interests')).split(',')
            user.contact_preferences = cgi.escape(self.request.get('contact_preferences'))
            user.put()            

app = webapp.WSGIApplication([
        ('/fb/', testRoot),
        ('/fb/fbUser', fbUserHandler)
        ], debug=True)

def main():
    run_wsgi_app(app)

if __name__ == "__main__":
    main()
