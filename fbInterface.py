import cgi
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from models import *
from ccUtils import *

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
        if results.get() ==None : self.response.out.write("")
        else:
            for result in results:
                self.response.out.write(to_dict(result))

    def post(self):
        fb_id = cgi.escape(self.request.get('fb_id'))
        results = fbUser.gql("WHERE fb_id = :1", int(fb_id))
        if results.get() == None:
            # Create a new user
            user = fbUser()
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
        if results.get() ==None : self.response.out.write("")
        else:
            for result in results:
                self.response.out.write(to_dict(result))

    def post(self):
        org_name = cgi.escape(self.request.get('org_name'))
        results = Organization.gql("WHERE org_name = :1", org_name)
        if results.get() == None:
            # Create a new orgnization
            org = Organization()
            org.org_id = Organization.all().count() + 1
            api_key = org.put()
            org.api_key = str(api_key)
            self.response.out.write(str(api_key))
        else:
            org = results.get()
        org.org_name = cgi.escape(self.request.get('org_name'))
        if self.request.get('url'):
            org.url = cgi.escape(self.request.get('url'))
        if self.request.get('rank'):
            org.rank = int(cgi.escape(self.request.get('rank')))
        if self.request.get('active'):
            if int(self.request.get('active')) == 1:            
                org.active = True
            else:
                org.active = False
        if self.request.get('fbaccount'):
            org.fbaccount = cgi.escape(self.request.get('fbaccount'))
        if self.request.get('badge_image_url'):            
            org.skills = cgi.escape(self.request.get('badge_image_url'))
        if self.request.get('admins'):            
            org.interests = cgi.escape(self.request.get('admins')).split(',')
        db.put(org)            

class TaskHandler(webapp.RequestHandler):
    def get(self):
        if self.request.get('org_id') and self.request.get('task_name'):
            org_id = int(cgi.escape(self.request.get('org_id')))
            task_name = cgi.escape(self.request.get('task_name'))
            results = Task.gql("WHERE org_id = :1 AND name = :2", 
                org_id,
                task_name)
        elif self.request.get('task_id'):
            task_id = int(cgi.escape(self.request.get('task_id')))
            results = Task.gql("WHERE task_id = :1", task_id)
        elif self.request.get('org_id'):
            org_id = int(cgi.escape(self.request.get('org_id')))
            results = Task.gql("WHERE org_id = :1", org_id)
        elif self.request.get('skills'):
            resultList = []
            for skill in self.request.get('skills').split(','):
                requestList.append(Task.gql("WHERE skills_needed = :1", skill))
            results = set(resultList)
        elif self.request.get('skills_strict'):
            resultList = Task.all()
            for skill in self.request.get('skills').split(','):
                requestList = requestList.filter("skills_needed=", skill)
            results = set(resultList)
        else:
            results = Task.all()
        if results.get() ==None : self.response.out.write("")
        else:
            for result in results:
                self.response.out.write(to_dict(result))

    def post(self):
        org_id = int(cgi.escape(self.request.get('org_id')))
        task_name = cgi.escape(self.request.get('task_name'))
        results = Task.gql("WHERE org_id = :1 AND name = :2", org_id, task_name)
        if results.get() == None:
            # Create a new user
            task = Task()
            task.org_id = org_id
            task.name = task_name
            task.task_id = Task.all().count() + 1
            task.owning_org = Organization.all().filter('org_id=',org_id).get()
            if task.owning_org: # FIX ME LATER!
                task.callback = "http://crisiscorpsapp.appspot.com/api/" + str(task.owning_org.org_id) + "/" + task.task_id
                self.response.out.write("{callback:\"" + task.callback +"\" /}")
            else: self.response.out.write("{callback: }")
        else:
            task = results.get()
        if self.request.get('desc'):
            task.desc = cgi.escape(self.request.get('desc'))
        if self.request.get('skills_needed'):
            task.skills_needed = cgi.escape(self.request.get('skills_needed()')).split(',')
        if self.request.get('url'):            
            task.url = cgi.escape(self.request.get('url'))
        if self.request.get('status'):
            task.status = cgi.escape(self.request.get('status'))
        db.put(org)            

class User_TaskHandler(webapp.RequestHandler):
    def get(self):
        if self.request.get('fb_id') and self.request.get('task_id'):
            fb_id = int(cgi.escape(self.request.get('fb_id')))
            task_id = int(cgi.escape(self.request.get('task_id')))
            results = User_Task.gql("WHERE fb_id = :1 AND task_id = :2", fb_id, task_id)
        elif self.request.get('fb_id'):
            fb_id = int(cgi.escape(self.request.get('fb_id')))
            results = User_Task.gql("WHERE fb_id=:1", fb_id)
        else:
            results = User_Task.all()
        if results.get() ==None : self.response.out.write("")
        else:
            for result in results:
                self.response.out.write(to_dict(result))

    def post(self):
        fb_id = int(cgi.escape(self.request.get('fb_id')))
        task_id = int(cgi.escape(self.request.get('fb_id')))
        results = User_Task.gql("WHERE fb_id = :1 AND task_id = :2", fb_id, task_id)
        if results.get() == None:
            # Create a new orgnization
            user_task = User_Task()
            user_task.fb_id = fb_id
            user_task.task_id = task_id
            user_task.fbUser = fbUser.all().filter('fb_id=',fb_id).get()
            user_task.Task = Task.all().filter('task_id=',task_id).get()
            user_task.org_id = user_task.Task.owning_org.org_id
        else:
            user_task = results.get()
        if self.request.get('score'):
            user.score = int(cgi.escape(self.request.get('score')))
        if self.request.get('status'):
            user.status = int(cgi.escape(self.request.get('status')))
        db.put(org)            


app = webapp.WSGIApplication([
        ('/fb/', testRoot),
        ('/fb/fbUser', fbUserHandler),
        ('/fb/Organization', OrgHandler),
        ('/fb/Task', TaskHandler),
        ('/fb/User_Task', User_TaskHandler)
        ], debug=True)

def main():
    run_wsgi_app(app)

if __name__ == "__main__":
    main()
