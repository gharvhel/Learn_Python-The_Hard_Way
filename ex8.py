#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File              : ex8.py
# Author            : Gharvhel Carre <gc2767@columbia.edu>
# Date              : 22.03.2018
# Last Modified Date: 22.03.2018
# Last Modified By  : Gharvhel Carre <gc2767@columbia.edu>

formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)
