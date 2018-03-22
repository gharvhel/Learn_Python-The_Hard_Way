#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File              : ex5.py
# Author            : Gharvhel Carre <gc2767@columbia.edu>
# Date              : 21.03.2018
# Last Modified Date: 21.03.2018
# Last Modified By  : Gharvhel Carre <gc2767@columbia.edu>

MY_NAME = 'Gharvhel Carre'
MY_AGE = 21
MY_HEIGHT = 5.9  # feet
MY_WEIGHT = 138  # lbs
MY_EYES = 'Brown'
MY_TEETH = 'White'
MY_HAIR = 'Black'

print "Let's talk about %s." % MY_NAME
print "He's %f feet tall." % MY_HEIGHT
print "He's %d pounds heavy." % MY_WEIGHT
print "Thats not heavy though."
print "He's got %s eyes and %s hair" % (MY_EYES, MY_HAIR)
print "He's teeth are %s." % MY_TEETH

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
    MY_AGE, MY_HEIGHT,  MY_WEIGHT, MY_AGE + MY_WEIGHT + MY_HEIGHT)
