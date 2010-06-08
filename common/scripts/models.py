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
# 
"""
Defines the set of data models used by the CrisisCorps application
"""
__author__    = "Alex Schoof <alex.schoof@gmail.com>"
__copyright__ = "CrisisCorps.org"
__license__   = "GPL v3"
__date__      = "2010-06-05"
__version__   = 0.1

# 
# ---------------------------------------------------------------------------

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
    org_id = db.IntegerProperty()
    url = db.StringProperty()
    application_url = db.LinkProperty()
    api_key = db.StringProperty()
    rank = db.IntegerProperty()
    active = db.BooleanProperty()
    #now pointing to facebook page as they might not know their account
    #fbaccount = db.StringProperty()
    fbaccount = db.LinkProperty()
    badge_image_url = db.StringProperty()
    admins = db.ListProperty(db.Email)

class Task(db.Model):
    task_id = db.IntegerProperty()
    org_id = db.IntegerProperty()
    owning_org = db.ReferenceProperty(Organization)
    name = db.StringProperty()
    desc = db.TextProperty()
    skills_needed = db.StringListProperty()
    url = db.StringProperty()
    status = db.IntegerProperty()
    callback = db.StringProperty()
    
class User_Task(db.Model):
    fb_id = db.IntegerProperty()
    fbUser = db.ReferenceProperty(fbUser)
    task_id = db.IntegerProperty()
    Task = db.ReferenceProperty(Task)
    Score = db.IntegerProperty()
    Status = db.IntegerProperty()
    org_id = db.IntegerProperty()
