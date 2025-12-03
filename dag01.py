# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 22:09:16 2024

@author: Paul
"""

import time
start_time = time.time_ns()

f = open("input.txt", "r")
p1=0
p2=0
clicks=100
rot=50
instr=list()
for i,line in enumerate(f):
    r,n=[line[0],int(line[1:])]
    
    if r=='R':
        for i in range(0,n):
            rot=(rot+1)%clicks
            if rot==0:
                p2+=1
    else:
        for i in range(0,n):
            rot=(rot-1)%clicks
            if rot==0:
                p2+=1
    if rot==0:
        p1+=1
        
f.close()
    
print("Part 1",p1)
print("Part 2",p2)
print("--- %s ms ---" % ((time.time_ns() - start_time)/1000000))