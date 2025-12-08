# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 22:09:16 2024
New template 02-12-2025
@author: Paul
"""

import time
start_time = time.time_ns()

f = open("input.txt", "r")
box=list()
for i,line in enumerate(f):
    box.append([int(d) for d in line.split(',')])
f.close()

#Maak een lijst van alle afstanden met bijbehorende indices
distances=list()
for ind1,[x1,y1,z1] in enumerate(box):
    for ind_,[x2,y2,z2] in enumerate(box[ind1+1:]):
        ind2=ind_+ind1+1
        dist=(x1-x2)**2+(y1-y2)**2+(z1-z2)**2
        distances.append([dist,ind1,ind2])
#sorteer van klein naar groot
distances.sort()

#Ga de indices af en gooi ze samen in groepen
circuit_count=0
i=0
box_group=dict() #Voor elke junction box bijhouden in welke group hij zit
group_boxes=dict() #Voor elke group bijhouden welke boxes erin zitten
while True:
    [_,ind1,ind2]=distances[i]
    i+=1
    if ind1 in box_group and ind2 not in box_group:
        #ind2 toevoegen aan de groep van ind1
        group=box_group[ind1]
        group_boxes[group].append(ind2)
        box_group[ind2]=group
    elif ind2 in box_group and ind1 not in box_group:
        #ind1 toevoegen aan de groep van ind2
        group=box_group[ind2]
        group_boxes[group].append(ind1)
        box_group[ind1]=group
    elif ind1 in box_group and ind2 in box_group:
        #Samenvoegen van twee groepen junction boxes
        group1=box_group[ind1]
        group2=box_group[ind2]
        if group1==group2:
            continue
        for index in group_boxes[group2]:
            box_group[index]=group1
        group_boxes[group1].extend(group_boxes[group2])
        del group_boxes[group2]
    else:
        #Nieuwe groep junction boxes
        group_boxes[circuit_count]=[ind1]
        group_boxes[circuit_count].append(ind2)
        box_group[ind1]=circuit_count
        box_group[ind2]=circuit_count
        circuit_count+=1
    #Conditie p1
    if i==999: 
        p1_sizes=[]   
        for g in group_boxes:
            p1_sizes.append(len(group_boxes[g]))
        p1_sizes.sort(reverse=True)
    #Conditie p2 en klaar
    if len(group_boxes)==1 and len(box_group)==len(box):
           break   
print("Part 1",p1_sizes[0]*p1_sizes[1]*p1_sizes[2])
print("Part 2",box[ind1][0]*box[ind2][0])
print("--- %s ms ---" % ((time.time_ns() - start_time)/1000000))