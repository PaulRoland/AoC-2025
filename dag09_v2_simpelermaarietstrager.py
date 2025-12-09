# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 22:09:16 2024
New template 02-12-2025
@author: Paul
"""

import time
start_time = time.time_ns()

def in_contour(x_test,y_test,corners):
    #Kijk of x_test,y_test valt binnen de contour gemaakt aan de hand van opeenvolgende corners (alleen horizontaal en verticaal, nog....)
    #Oneven aantal -> binnen contour -> True , even aantal->buiten contour -> False
    if (x_test,y_test) in in_contour_mem:
        return in_contour_mem[(x_test,y_test)]
    #Tel dus het aantal vertical lijnen links van dit punt
    count=0
    for [x1,y1],[x2,y2] in zip(corners,corners[1:]):
        #Als een punt precies op dezelfde hoogte zit als 2 knooppunten, dan telt hij 2 keer een verticale lijn (dit zou buiten zijn) truc om dit te voorkomen!
        if y1==y2:
            if y1==y_test and min(x1,x2)<=x_test and max(x1,x2)>=x_test:
                #punt valt precies op de lijn
                in_contour_mem[(x_test,y_test)]=1
                return 1
            elif y1==y_test and max(x1,x2)<x_test: #Horizontale lijn niet meetellen bij de counts
                count+=0
            continue
        if x1==x_test and min(y1,y2)<=y_test and max(y1,y2)>=y_test:
            #hij valt precies op de lijn
            in_contour_mem[(x_test,y_test)]=1
            return 1
        
        #Verticale lijn ligt voor dit punt en gaat er voorbij aan beide kanten
        if min(y1,y2)<y_test and max(y1,y2)>y_test and x1<=x_test:
            count+=1
            continue
        
        #Verticale lijn eindigt precies op dezelfde hoogte als testpunt, nu moeten we oppassen!!
        # Anders count=3 bij beide onderstaande scenarios! 
        #       __       
        #  0  _|1     0  _  0
        #    |          | |
        # Alleen erbij optellen als het het hoogste punt is van de geteste lijn
        if x1<=x_test and y_test==max(y1,y2):
            count+=1
    in_contour_mem[(x_test,y_test)]=count%2
    return count%2
               
def no_intersect(path1,path2):
    #Kijk of de bedachte rechthoek geen lijnen doorkruist. 1 als er geen kruizing is en 0 als er wel een kruizing is
    for [x1,y1],[x2,y2] in zip(path1,path1[1:]):
        for [x3,y3],[x4,y4] in zip(path2,path2[1:]):
            if (x1==x2 and x3==x4) or (y1==y2 and y3==y4): #Parallel
                continue
            x1_min,x1_max,y1_min,y1_max=min(x1,x2),max(x1,x2),min(y1,y2),max(y1,y2)
            x2_min,x2_max,y2_min,y2_max=min(x3,x4),max(x3,x4),min(y3,y4),max(y3,y4)
            #Lijnen kunnen elkaar theoretisch niet kruisen
            if x1_max<=x2_min or x1_min>=x2_max or y1_max<=y2_min or y1_min>=y2_max:
                continue
            #Kruizing in richting 1
            if (x2_min>x1_min and x2_max<x1_max):
                return 0
            #En richting 2
            if (y2_min>y1_min and y2_max<y1_max):
                return 0   
    return 1

corners=list()
f = open("input.txt", "r")
for i,line in enumerate(f):
    line=line.replace('(','').replace(')','').replace('=','').replace('\n','')
    corners.append([int(d) for d in line.split(',')])
f.close()
#Maak het cirkeltje rond
corners.append(corners[0])

p2=0
p1=0

in_contour_mem=dict()
for ind1,[a,b] in enumerate(corners):
    for ind2,[c,d] in enumerate(corners[ind1+1:]):
        area=(abs(d-b)+1)*(abs(c-a)+1)
        p1=max(p1,area)
        if area<p2:
            #geen moeite doen als het record niet verbroken kan worden
            continue
        #Kijk of de lijnen van de rechthoek de contour nergens doorkruisen
        #Kijk of de twee verzonnen hoekpunten binnen de contour liggen
        rectangle=[[a,b],[a,d],[c,d],[c,b],[a,b]]
        if in_contour(a,d,corners) and in_contour(c,b,corners) and no_intersect(rectangle,corners):
            p2=area
            
print("Part 1",p1)
print("Part 2",p2)
print("--- %s ms ---" % ((time.time_ns() - start_time)/1000000))