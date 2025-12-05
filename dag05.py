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
ingredient_ranges=list()
ingredient_ids=list()

for i,line in enumerate(f):
    if line=='\n':
        break
    line=line.replace('(','').replace(')','').replace('=','').replace('\n','')
    ingredient_ranges.append([int(d) for d in line.split('-')])
for i,line in enumerate(f):
    line=line.replace('(','').replace(')','').replace('=','').replace('\n','')
    ingredient_ids.append(int(line))
f.close()

ranges_compiled=list()
for new_a,new_b in ingredient_ranges:
    left_ranges=[]
    right_ranges=[]
    left=new_a
    right=new_b
    
    for i,[a,b] in enumerate(ranges_compiled):
        #Links valt ergens voor
        if new_a<=a:
            #Bewaar alle ranges links tot deze, grens voor nieuwe range komt in left
            left_ranges=ranges_compiled[:i]
            left=new_a
            break
        
        #Links valt nergens voor, maar wel ergens tussen of sluit exact aan
        if new_a>a and new_a<=b+1:
            left_ranges=ranges_compiled[:i]
            #Behoud originele linkerkant van deze range
            left=a
            break
        #We zijn al ergens voorbij, maar niet direct stoppen want hij kan nog in een andere vallen
        if new_a>b:
            left_ranges=ranges_compiled[:i+1]
            left=new_a

        
    for i,[a,b] in enumerate(ranges_compiled):
        #rechts valt ergens voor, niet verder zoeken
        if new_b<a-1:
            right_ranges=ranges_compiled[i:]
            right=new_b
            break

        #recht valt ergens tussen, niet verder zoeken
        if new_b>=a-1 and new_b<=b:
            right_ranges=ranges_compiled[i+1:]
            right=b
            break
        #We zijn all ergens voorbij, maar hij kan nog in de volgende vallen
        if new_b>b:
            right_ranges=ranges_compiled[i+1:]
            right=new_b

    ranges_compiled=[]
    ranges_compiled.extend(left_ranges)
    ranges_compiled.append([left,right])
    ranges_compiled.extend(right_ranges)

                     
for a,b in ranges_compiled:
    p2+=b-a+1
    
#p1 is sneller met de gecompileerde ranges 
for ing_id in ingredient_ids:
    fresh=False
    for l,r in ranges_compiled:
        if ing_id>=l and ing_id<=r:
            fresh=True
            break
    if fresh==True:
        p1+=1
    

print("Part 1",p1)
print("Part 2",p2)
print("--- %s ms ---" % ((time.time_ns() - start_time)/1000000))