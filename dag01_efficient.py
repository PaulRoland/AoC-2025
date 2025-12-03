# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 22:09:16 2024

@author: Paul
"""

import time
start_time = time.time_ns()


p1=0
p2=0
clicks=100
prev=50
f = open("input.txt", "r")
for line in f:
    line=line.replace('R','').replace('L','-')
    delta=int(line)
    p2+=abs(delta)//clicks
    delta=delta//abs(delta)*(abs(delta)%clicks)
    new=prev+delta
    if new in [0,clicks]:
        p1+=1
        p2+=(delta!=0)       
    p2+=(new>clicks or prev*new<0)
    prev=new%clicks 
f.close()
    
print("Part 1",p1)
print("Part 2",p2)
print("--- %s ms ---" % ((time.time_ns() - start_time)/1000000))