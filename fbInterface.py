import cgi
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from models import *

class testRoot(webapp.RequestHandler):
    def get(self):
        self.response.out.write("This is the root of the fb api.")

class fbUserHandler(webapp.RequestHandler):
    def get(self):
        if self.request.get('fb_id'):
            fb_id = cgi.escape(self.request.get('fb_id'))
            results = fbUser.gql("WHERE fb_id = :1", int(fb_id))
        else:
            results = fbUser.all()
        if results.get() ==None : self.response.out.write("{}")
        else:
            for result in results:
                self.response.out.write(result.to_xml())

    def post(self):
        fb_id = cgi.escape(self.request.get('fb_id'))
        results = fbUser.gql("WHERE fb_id = :1", int(fb_id))
        if results.get() == None:
            # Create a new user
            users = fbUser()
        else:
            user = results.get()
        user.fb_id = int(cgi.escape(self.request.get('fb_id')))
        if self.request.get('lname'):
            user.lname = cgi.escape(self.request.get('lname'))
        if self.request.get('fname'):            
            user.fname = cgi.escape(self.request.get('fname'))
        if self.request.get('email'):
            user.email = cgi.escape(self.request.get('email'))
        if self.request.get('location'):            
            user.location = cgi.escape(self.request.get('location'))
        if self.request.get('interest_locations'):
            user.interest_locations = cgi.escape(self.request.get('interest_locations')).split(',')
        if self.request.get('skills'):            
            user.skills = cgi.escape(self.request.get('skills')).split(',')
        if self.request.get('interests'):            
            user.interests = cgi.escape(self.request.get('interests')).split(',')
        if self.request.get('contact_preferences'):            
            user.contact_preferences = cgi.escape(self.request.get('contact_preferences'))
        db.put(user)            

class OrgHandler(webapp.RequestHandler):
    def get(self):
        if self.request.get('org_name'):
            org_name = cgi.escape(self.request.get('org_name'))
            results = Organization.gql("WHERE org_name = :1", org_name)
        else:
            results = Organization.all()
        if results.get() ==None : self.response.out.write("{}")
        else:
            for result in results:
                self.response.out.write(result.to_xml())

    def post(self):
        org_name = cgi.escape(self.request.get('org_name'))
        results = Organization.gql("WHERE org_name = :1", org_name)
        if results.get() == None:
            # Create a new user
            org = Organization()
            api_key = org.put()
            org.api_key = api_key
        else:
            org = results.get()
        org.org_name = cgi.escape(self.request.get('org_name'))
        if self.request.get('url'):
            org.url = cgi.escape(self.request.get('url'))
        if self.request.get('rank'):
            org.rank = int(cgi.escape(self.request.get('rank')))
        if self.request.get('active'):            
            org.active = cgi.escape(self.request.get('active'))
        if self.request.get('fbaccount'):
            org.fbaccount = cgi.escape(self.request.get('fbaccount'))
        if self.request.get('badge_image_url'):            
            org.skills = cgi.escape(self.request.get('badge_image_url'))
        if self.request.get('admins'):            
            org.interests = cgi.escape(self.request.get('admins')).split(',')
        db.put(org)            



app = webapp.WSGIApplication([
        ('/fb/', testRoot),
        ('/fb/fbUser', fbUserHandler),
        ('fb/Organization', OrgHandler)
        ], debug=True)

def main():
    run_wsgi_app(app)

if __name__ == "__main__":
    main()
