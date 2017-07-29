#!/usr/bin/python3
'''
mm=200
l=[1]
for i in range(mm):
	t=[]
	for i in range(mm):
		t.append(0)
	l.append(t)
def tri(num):
	l[0][0]=1
	i=0
	while i<num:
		j=0
		while j<=i+1:
			l[i+1][j]=l[i][j]+l[i][j-1]
			j+=1
		yield(l[i])
		i+=1
	return
'''
def tri2(num):
	i=1
	l=[1]
	yield l
	while i<num:
		l=[1]+[l[j-1]+l[j] for j in range(1,i)]+[1]
		yield l
		i+=1

n=int(input("Enter a number:"))
for i in tri2(n):
	print(i)

