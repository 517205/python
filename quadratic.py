#!/usr/bin/python3
import math
def myroot(a,b,c):
	d=b**2-4*a*c
	if a==0:
		print('illegal!\a')
		return None
	elif d<0:
		print('Two imaginary roots:')
		r=-b/(2*a)
		i=math.sqrt(-d)
		print(complex(r,i),complex(r,-i))
	elif d==0:
		print('Two equal roots:')
		print(-b/(2*a))
	else:
		print('Two real roots:')
		x1=(-b-math.sqrt(d))/(2*a)
		x2=(-b+math.sqrt(d))/(2*a)
		print(x1,x2)
l=input("ax^2+bx+c=0\nEnter a b c:")
l=l.split(" ")
for i in range(len(l)):
	l[i]=int(l[i])
myroot(l[0],l[1],l[2])
#l=[input("ax^2+bx+c=0\nEnter a b c:").split(" ")]
#print(l)
