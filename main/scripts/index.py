import os, cgi
import sys
from google.appengine.ext.webapp import template
from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from common.scripts.models import *


class MainPage(webapp.RequestHandler):
    def get(self):
        if users.get_current_user():
            url = users.create_logout_url(self.request.uri)
            url_linktext = 'Logout'
        else:
            url = users.create_login_url(self.request.uri)
            url_linktext = 'Login'

        template_values = {
            'url': url,
            'url_linktext': url_linktext,
            'individuals_url': self.request.uri+'/individuals',
            'organizations_url': self.request.uri+'/organizations'
            }

        path = os.path.join(os.path.dirname(__file__), '../templates/index.html')
        self.response.out.write(template.render(path, template_values))

class Individuals(webapp.RequestHandler):
    def get(self):
        template_values = {} 

        path = os.path.join(os.path.dirname(__file__), '../templates/welcome-individuals.html')
        self.response.out.write(template.render(path, template_values))

class Organizations(webapp.RequestHandler):
    def get(self):
        template_values = {} 

        path = os.path.join(os.path.dirname(__file__), '../templates/welcome-organizations.html')
        self.response.out.write(template.render(path, template_values))

    def post(self):
        # Create a Organization
        org = Organization()
        org.org_name = cgi.escape(self.request.get('organization[org_name]'))
        org.url = cgi.escape(self.request.get('organization[url]'))
        org.fbaccount = cgi.escape(self.request.get('organization[fbaccount]'))
        org.admins = [db.Email(elem) for elem in cgi.escape(self.request.get('organization[admins]')).split(';')]

        template_values = {}

        if db.put(org):
            path = os.path.join(os.path.dirname(__file__), '../templates/organizations-create.html')
            self.response.out.write(template.render(path, template_values))
	else:
            path = os.path.join(os.path.dirname(__file__), '../templates/welcome-organizations.html')
            self.response.out.write(template.render(path, template_values))

application = webapp.WSGIApplication(
    [('/', MainPage),
     ('/individuals', Individuals),
     ('/organizations', Organizations)],
    debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
