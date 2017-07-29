#!/usr/bin/env python3
import functools

def log(text):
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args,**kw):
			print('function %s start:%s' % (func.__name__ , text))
			l=func(*args,**kw)
			print('function %s end.' % (func.__name__))
			return l
		return wrapper
	return decorator

#@log('aaa')
def hello(*args):
	for i in args:
		print(i)
	return True
a=log('aaa')(hello)('a','7',8,True)
print(a)

