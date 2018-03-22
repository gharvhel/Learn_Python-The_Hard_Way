#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File              : ex11.py
# Author            : Gharvhel Carre <gc2767@columbia.edu>
# Date              : 22.03.2018
# Last Modified Date: 22.03.2018
# Last Modified By  : Gharvhel Carre <gc2767@columbia.edu>

print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy." % (
    age, height, weight)
