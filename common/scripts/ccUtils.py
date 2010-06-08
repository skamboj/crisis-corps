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
A set of utilities for converting types 
"""
__author__    = "Alex Schoof <alex.schoof@gmail.com>"
__copyright__ = "CrisisCorps.org"
__license__   = "GPL v3"
__date__      = "2010-06-05"
__version__   = 0.1

# Major Revisions:
# 
# ---------------------------------------------------------------------------

import datetime
import time

SIMPLE_TYPES = (int, long, float, bool, dict, basestring, list)

def to_dict(model):
    output = {}

    for key, prop in model.properties().iteritems():
        value = getattr(model, key)

        if value is None or isinstance(value, SIMPLE_TYPES):
            output[key] = value
        elif isinstance(value, datetime.date):
            # Convert date/datetime to ms-since-epoch ("new Date()").
            ms = time.mktime(value.utctimetuple()) * 1000
            ms += getattr(value, 'microseconds', 0) / 1000
            output[key] = int(ms)
        elif isinstance(value, db.Model):
            output[key] = to_dict(value)
        else:
            raise ValueError('cannot encode ' + repr(prop))

    return output
