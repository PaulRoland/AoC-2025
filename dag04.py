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
f = open("input.txt", "r")
rolls=dict()
for r,line in enumerate(f):
    line=line.replace('(','').replace(')','').replace('=','').replace('\n','')
    for c,s in enumerate(line):
        if s=='@':
            key=str(r)+','+str(c)
            rolls[key]=0
    
f.close()
#Count rolls
max_r=4
for key in rolls:
    roll_count=0
    [r,c]=[int(d) for d in key.split(',')]
    for dr in [-1,0,1]:
        for dc in [-1,0,1]:
            new_key=str(r+dr)+','+str(c+dc)
            if new_key in rolls:
                roll_count+=1
    
    if roll_count<=max_r:
        p1+=1
        
status_prev=len(rolls)
while True:
    rolls_to_remove=list()
    for key in rolls:
        roll_count=0
        [r,c]=[int(d) for d in key.split(',')]
        for dr in [-1,0,1]:
            for dc in [-1,0,1]:
                new_key=str(r+dr)+','+str(c+dc)
                if new_key in rolls:
                    roll_count+=1
        
        if roll_count<=max_r:
            rolls_to_remove.append(key)
    
    for key in rolls_to_remove:
        p2+=1
        del rolls[key]
    
    if len(rolls)==status_prev:
        break
    status_prev=len(rolls)
            
            
        

print("Part 1",p1)
print("Part 2",p2)
print("--- %s ms ---" % ((time.time_ns() - start_time)/1000000))