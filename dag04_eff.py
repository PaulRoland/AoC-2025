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
            key=(r,c)
            rolls[key]=0
    
f.close()

max_r=3
to_remove=deque([])
for key in rolls:
    roll_count=0
    nbrs=[]
    r,c=key
    #Kijk in de vakjes rondom (offset rond r en cmet dr en dc)
    for dr,dc in ((-1,-1),(-1,0),(-1,1),(1,-1),(1,0),(1,1),(0,-1),(0,1)):
        new_key=(r+dr,c+dc)
        if new_key in rolls:
            #Tel het aantal buren, en maak een lijstje van de buur'keys'
            roll_count+=1
            nbrs.append(new_key)
    if roll_count<=max_r:
        #Maak een lijst van te verwijderen blokjes voor p2
        to_remove.append(key)
        p1+=1
    rolls[key]=[roll_count,nbrs]

#Set van verwijderde items, geeft uiteindelijk p2 en wordt gebruikt als check
removed=set(to_remove)
while to_remove:
    remove_roll = to_remove.popleft()
    #Verwijder een punt bij alle buren en controleer of ze wegmogen
    nbrs=rolls[remove_roll][1]
    for nbr in nbrs:
        rolls[nbr][0]-=1
        #Als een van de buren van een verwijderd blokje minder dan max_r buren heeft en nog niet op de removed lijst staat mag hij weg
        if rolls[nbr][0]<=max_r and nbr not in removed:
            to_remove.append(nbr)
            removed.add(nbr)   

print("Part 1",p1)
print("Part 2",len(removed))

print("--- %s ms ---" % ((time.time_ns() - start_time)/1000000))
