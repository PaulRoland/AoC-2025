# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 22:09:16 2024
New template 02-12-2025
@author: Paul
"""

import time
start_time = time.time_ns()

f = open("input.txt", "r")
splitters=dict()

#Start conditie
sr,sc=0,f.readline().index('S')
for r,line in enumerate(f):
    #Skip the lines with .....
    if r%2==0:
        continue
    for c,s in enumerate(line):
        #Splitters, gesorteerd op kolom. Op volgorde van rij
        if s=='^':
            if c in splitters:
                splitters[c].append(r+1)
            else:
                splitters[c]=[r+1]
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
                splitters_had.add((new_r,c))
                #Open nieuwe timelimes
                resulting_timelines = timelines(new_r,c+1)+timelines(new_r,c-1)
                #Sla het resultaat op voor snelle toegang de volgende keer
                mem[(r,c)]=resulting_timelines
                return resulting_timelines
    #Geen vertakkingen meer
    return 1

splitters_had=set()
mem=dict()   
p2=timelines(sr,sc)
  
print("Part 1",len(splitters_had))
print("Part 2",p2)
print("--- %s ms ---" % ((time.time_ns() - start_time)/1000000))