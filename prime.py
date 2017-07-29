#!/usr/bin/env python3
def full():
	n=1
	while True:
		n+=1
		yield n
def is_divide(n):
	return lambda ans: ans%n!=0
def p():
	it=full()
	while True:
		a=next(it)
		yield a
		it=filter(is_divide(a),it)
for i in p():
	if i<100000000:
		print(i)
	else:
		break

