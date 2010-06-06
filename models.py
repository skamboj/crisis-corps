from google.appengine.ext import db

class fbUser(db.Model):
    fb_id = db.IntegerProperty()
    lname = db.StringProperty()
    fname = db.StringProperty()
    email = db.EmailProperty()
    location = db.StringProperty()
    interest_locations = db.StringListProperty()
    skills = db.StringListProperty()
    interests = db.StringListProperty()
    contact_properties = db.IntegerProperty()

class Organization(db.Model):
    org_name = db.StringProperty()
    url = db.LinkProperty()
    api_key = db.StringProperty()
    rank = db.IntegerProperty()
    active = db.BooleanProperty()
    fbaccount = db.StringProperty()
    badge_image_url = db.StringProperty()
    admins = db.ListProperty(db.Email)

class Task(db.Model):
    org_id = db.ReferenceProperty(Organization)
    name = db.StringProperty()
    desc = db.TextProperty()
    skills_needed = db.StringListProperty()
    url = db.LinkProperty()
    status = db.IntegerProperty()
    
class User_Task(db.Model):
    fb_id = db.ReferenceProperty(fbUser)
    Task_id = db.ReferenceProperty(Task)
    Score = db.IntegerProperty()
    Status = db.IntegerProperty()
    org_id = db.ReferenceProperty(Organization)
