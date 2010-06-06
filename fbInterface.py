import cgi
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from models import *

class testRoot(webapp.RequestHandler):
    def get(self):
        self.response.out.write("This is the root of the fb api.")

#class 

app = webapp.WSGIApplication([
        ('/fb/', testRoot)
        ], debug=True)

def main():
    run_wsgi_app(app)

if __name__ == "__main__":
    main()
