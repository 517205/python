#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'Peter Gu'

import sys

def test():
	args=sys.argv
	if len(args)==1:
		print('No argument...')
	else:
		print('Arguments:')
		for i in args[1:]:
			print(i)


if __name__=='__main__':
	print('***__name__:',__name__,'***')
	print('***__author__:',__author__,'***')
	print('***__doc__:',__doc__,'***')
	test()

