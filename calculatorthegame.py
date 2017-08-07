#!/usr/bin/env python3
__author__="Yimin Gu"

import math
error=-999999
inf=999998
maxfigure=6

def sgn(n):
    if n>0:
        return 1
    elif n==0:
        return 0
    else:
        return -1
def plus(n,a):
    return n+a
def minus(n,a):
    return n-a
def mul(n,a):
    return n*a
def div(n,a):
    if n%a!=0:
        return error
    return n//a
def add(n,a):
    for i in range(1,maxfigure):
        if a<10**i:
            return n*10**i+a
def rm(n):
    return n//10
def reverse(n):
    return sgn(n)*int(str(abs(n))[::-1])
def change(n,f,t):
    if str(f) not in str(n):
        return error
    return int(str(n).replace(str(f),str(t)))
    '''
    pos=[0]
    i=0
    while f in n[pos[i]+len(f):]:
        pos.append(n[pos[i]+len(f):].index(f))
        i+=1
    for i in pos:
        n=n[:pos]+t+n[pos+len(f):]
    return sign*int(n)
    '''
def mirror(n):
    return sgn(n)*int(str(abs(n))+str(abs(n))[::-1])
def shiftl(n):
    return sgn(n)*int(str(abs(n))[1:]+str(abs(n))[0])
def shiftr(n):
    return sgn(n)*int(str(abs(n))[-1]+str(abs(n))[:-1])
def ssum(n):
    ans=0
    for i in str(abs(n)):
        ans+=int(i)
    return sgn(n)*ans
def oppo(n):
    return -n
def inv10(n):
    n1=''
    for i in str(n):
        n1+=str((10-int(i))%10)
    return int(n1)
def keyplus(n,add):
    pass


mydict={'plus':plus,'minus':minus,'mul':mul,'div':div,'add':add,'rm':rm,'reverse':reverse,'change':change,'mirror':mirror,'shiftl':shiftl,'shiftr':shiftr,'ssum':ssum,'oppo':oppo,'inv10':inv10,'keyplus':keyplus}


ans=[]
l1=[]
l2=[]
move=int(input("move:"))
goal=int(input("goal:"))
init=int(input("init:"))
btn=int(input("button number:"))
i=0
while i<btn:
    l1.append(str(input('operator>')))
    if (l1[i] in mydict)==False:
        print("No such button!")
        l1.pop()
        continue
    l2.append(input('number(Enter for none)>').split())
    if l2[i]!=[]:
        for j in range(len(l2[i])):
            l2[i][j]=int(l2[i][j])
    i+=1
#print(l1)
#print(l2)

def mloop(move,now,keyplusnum):
    if now==goal:
        return 1
    if move<=0 or now>inf or now==error:
        return 0
    for i in range(len(l1)):
        ff=mydict[l1[i]]
        if ff==keyplus:
            keyplusnum+=l2[i][0]
            isok=mloop(move-1,now,keyplusnum)
            keyplusnum-=l2[i][0]
        else:
            if len(l2[i])==1:
                new=ff(now,l2[i][0]+keyplusnum)
            else:
                new=ff(now,*l2[i])
            isok=mloop(move-1,new,keyplusnum)
        #print(new)
        if isok:
            ans.append(i)
            return 1
    return 0
            

mloop(move,init,0)
if ans==[]:
    print("No answer!")
else:
    for i in ans[::-1]:
        print(l1[i],*l2[i])

