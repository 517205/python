#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' another test module '

__author__ = 'Peter Gu'

import testmodule


print('***__name__:',__name__,'***')
print('***__author__:',__author__,'***')
print('***__doc__:',__doc__,'***')

print('Result is:\n')
testmodule.test()