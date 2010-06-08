#!/usr/bin/env python
# ---------------------------------------------------------------------------
# CrisisCorps.org
# Copyright (c) 2010
# 
# CrisisCorps is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# CrisisCorps is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with CrisisCorps.  If not, see <http://www.gnu.org/licenses/>.
# ---------------------------------------------------------------------------
"""
Main index code used for dispatching requests to the correct handlers
"""
__author__    = "Alex Schoof <alex.schoof@gmail.com>"
__copyright__ = "CrisisCorps.org"
__license__   = "GPL v3"
__date__      = "2010-06-05"
__version__   = 0.1

# Major Revisions:
# 
# ---------------------------------------------------------------------------


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
