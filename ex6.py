#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File              : ex6.py
# Author            : Gharvhel Carre <gc2767@columbia.edu>
# Date              : 21.03.2018
# Last Modified Date: 21.03.2018
# Last Modified By  : Gharvhel Carre <gc2767@columbia.edu>

x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

print "I said %r." % x
print "I said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of ..."
e = "a string with a right side."

print w + e
