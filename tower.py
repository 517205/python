#!/usr/bin/python3
#move n plates from a to c via b
def move(a,b,c,n):
	if n==0:
		return
	move(a,c,b,n-1)
	print(a,'->',c)
	move(b,a,c,n-1)
num=int(input("Enter number of plates:"))
move(1,2,3,num)
