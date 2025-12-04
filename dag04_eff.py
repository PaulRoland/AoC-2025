# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 22:09:16 2024
New template 02-12-2025
@author: Paul
"""

import time
from collections import deque
start_time = time.time_ns()
p1=0
p2=0
f = open("input.txt", "r")
rolls=dict()
for r,line in enumerate(f):
    line=line.replace('(','').replace(')','').replace('=','').replace('\n','')
    for c,s in enumerate(line):
        if s=='@':
            key=str(r)+','+str(c)
            rolls[key]=0
    
f.close()

max_r=3
to_remove=deque([])
for key in rolls:
    roll_count=0
    nbrs=[]
    [r,c]=[int(d) for d in key.split(',')]
    for dr in [-1,0,1]:
        for dc in [-1,0,1]:
            if dr==0 and dc==0:
                continue
            new_key=str(r+dr)+','+str(c+dc)
            if new_key in rolls:
                roll_count+=1
                nbrs.append(new_key)
    if roll_count<=max_r:
        to_remove.append(key)
        p1+=1
    rolls[key]=[roll_count,nbrs]

removed=set(to_remove)
while to_remove:
    remove_roll = to_remove.popleft()
    nbrs=rolls[remove_roll][1]
    for nbr in nbrs:
        rolls[nbr][0]-=1
        if rolls[nbr][0]<=max_r and nbr not in removed:
            to_remove.append(nbr)
            removed.add(nbr)   

print("Part 1",p1)
print("Part 2",len(removed))
print("--- %s ms ---" % ((time.time_ns() - start_time)/1000000))