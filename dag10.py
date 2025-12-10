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

def lights_match(code,lights):
    #Check match with lights
    if sum(lights)==len(code):
        for l in code:
            if lights[l]!=1:
                return 0
        return 1
    return 0

def not_continue_jolt(cur_jolt,joltage):
    #Check match with lights
    for a,b in zip(cur_jolt,joltage):
        if a>b:
            return 1
    return 0

from collections import deque
import scipy as sc
import numpy as np
f = open("input.txt", "r")
for i,line in enumerate(f):
    line=line.replace('\n','')
    data=line.split(' ')
    code=list()

    for n,s in enumerate(data[0][1:-1]):
        if s=='#':
            code.append(n)

    buttons=list()
    for dat in data[1:-1]:
        buttons.append([int(d) for d in dat[1:-1].split(',')])
    joltage=[int(d) for d in data[-1][1:-1].split(',')]


    ###p1
    stack=deque([[[0]*len(joltage),0,[]]])
    while stack:
        lights,length,b_had=stack.popleft()
        if lights_match(code,lights):
            min_length=length
            break
            
        #open nieuwe vertakkingen
        for button in buttons:
            if button in b_had:
                continue
            temp_lights=list(lights)
            for b in button:
                temp_lights[b]=1-temp_lights[b]
            new_had=list(b_had)
            new_had.append(button)
            #print(lights,button,temp_lights)
            stack.append([temp_lights,length+1,new_had])
        
    #print(line,min_length)
    p1+=min_length
    
    ##p2 match joltage
    #Maak een system of equations
    system=list()
    for ind,_ in enumerate(joltage):
        system_line=np.zeros(len(buttons)) #n1*a+n2*b+n3*c= n
        for ind2,button in enumerate(buttons): #a, b, c, d x deze button
            for b in button:
                if b==ind:
                    system_line[ind2]=1
        system.append(system_line)
    #minimaliseer  1*a+1*b+1*c+1*d etc
    minimize=np.ones(len(buttons))
    #constraints is het stelsel waar het aan moet voldoen (lower en upper is hetzelfde hier natuurlijk)
    constraints=sc.optimize.LinearConstraint(system,joltage,joltage)
    #milp solver! Yeah we zijn klaar
    answ=sc.optimize.milp(minimize,constraints=constraints,integrality=np.ones_like(minimize))
    p2+=int(sum(answ.x))

f.close()

print("Part 1",p1)
print("Part 2",p2)
print("--- %s ms ---" % ((time.time_ns() - start_time)/1000000))