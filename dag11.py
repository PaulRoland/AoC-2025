# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 22:09:16 2024
New template 02-12-2025
@author: Paul
"""

import time
start_time = time.time_ns()
p1=0
p2=0

def pw_valid(pw):
    #increasing straight
    valid=False
    for [a,b,c] in zip(pw,pw[1:],pw[2:]):
        if b==a+1 and c==b+1:
            valid=True
            break
    if valid==False:
        return 0
    pairs=set()
    for [a,b] in zip(pw,pw[1:]):
        if a==b:
            pairs.add(a)
    if len(pairs)>1:
        return 1
    return 0


alph=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
alph=['a','b','c','d','e','f','g','h','j','k','m','n','p','q','r','s','t','u','v','w','x','y','z']

passw='vzbxkghb'
passn=sum([alph.index(passw[ind])*len(alph)**(len(passw)-ind-1) for ind in range(0,len(passw))])
while True:
    passn+=1
    passw=[(passn%len(alph)**(ind+1))//(len(alph)**(ind)) for ind in range(0,len(passw))][::-1]
    if pw_valid(passw):
        p1=''.join(alph[ind] for ind in passw)
        break
while True:
    passn+=1
    passw=[(passn%len(alph)**(ind+1))//(len(alph)**(ind)) for ind in range(0,len(passw))][::-1]
    if pw_valid(passw):
        p2=''.join(alph[ind] for ind in passw)
        break
print("Part 1",p1)
print("Part 2",p2)
print("--- %s ms ---" % ((time.time_ns() - start_time)/1000000))