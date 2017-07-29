#!/usr/bin/python3
def tostd(s):
	s2=s[0].upper()
	for i in s[1:]:
		s2=s2+i.lower()
#	s=[s[0].upper()]+[i.lower() for i in s[1:]]
#	print(s)
	return s2
l=input("Enter a string:\n").split()
l=map(tostd,l)
l=list(l)
print(l)
