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

def joltage(line,n):
    value=0
    min_ind=0
    for cnt in range(0,n):
        max_digit=0
        #Laat genoeg digits over met zoeken
        max_ind=len(line)-n+cnt 
        for ind in range(min_ind,max_ind+1):
            digit=int(line[ind])
            if digit>max_digit:
                max_digit=digit
                
                #Set minimum index for the next digit
                min_ind=ind+1
                
        #Add digit to value
        value*=10
        value+=max_digit

    return value

f = open("input.txt", "r")
for line in f:
    p1+=joltage(line[:-1],2)
    p2+=joltage(line[:-1],12)
f.close()

print("Part 1",p1)
print("Part 2",p2)
print("--- %s ms ---" % ((time.time_ns() - start_time)/1000000))