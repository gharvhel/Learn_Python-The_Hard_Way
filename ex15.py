#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File              : ex15.py
# Author            : Gharvhel Carre <gc2767@columbia.edu>
# Date              : 27.03.2018
# Last Modified Date: 27.03.2018
# Last Modified By  : Gharvhel Carre <gc2767@columbia.edu>

from sys import argv

script, filename = argv

txt = open(filename)

print "Here's your file %r:" % filename
print txt.read()
txt.close()
print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()
txt_again.close()
