# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 22:09:16 2024
New template 02-12-2025
@author: Paul
"""

import time
from collections import deque
start_time = time.time_ns()

f = open("input.txt", "r")
splitters=dict()
splitters=dict()

for r,line in enumerate(f):
    for c,s in enumerate(line):
        #Start conditie
        if s=='S':
            sr,sc=r,c
        #Splitters, gesorteerd op kolom. Op volgorde van rij
        if s=='^':
            if c in splitters:
                splitters[c].append(r)
            else:
                splitters[c]=[r]  
f.close()

def timelines(r,c):
    #Kijk in het opgebouwde geheugen
    if (r,c) in mem:
        return mem[(r,c)]
    #Als er splitters in deze kolom zijn
    if c in splitters:
        for new_r in splitters[c]:
            #Pak de eerstvolgende
            if r<new_r:
                #Open nieuwe timelimes
                resulting_timelines = timelines(new_r,c+1)+timelines(new_r,c-1)
                #Sla het resultaat op voor snelle toegang de volgende keer
                mem[(r,c)]=resulting_timelines
                return resulting_timelines
    return 1

p1=0
p2=0
beams_going=deque([[sr,sc]])
splitters_had=set()
while beams_going:
    r,c = beams_going.popleft()
    if c in splitters:
        for new_r in splitters[c]:
            if r<new_r:
                #Als de splitter al gebruikt is, niet nog een keer gebruiken
                if (new_r,c) in splitters_had:
                    break
                p1+=1
                splitters_had.add((new_r,c))
                beams_going.append([new_r,c-1])
                beams_going.append([new_r,c+1])
                break
        
mem=dict()   
p2=timelines(sr,sc)
 
    
print("Part 1",p1)
print("Part 2",p2)
print("--- %s ms ---" % ((time.time_ns() - start_time)/1000000))