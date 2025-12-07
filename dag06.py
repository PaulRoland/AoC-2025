# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 22:09:16 2024
New template 02-12-2025
@author: Paul
"""

import time
import re

start_time = time.time_ns()
p1=0
p2=0
f = open("input.txt", "r")
nums=list()
nums_p2=list()
data=list()
for i,line in enumerate(f):
    line=line.replace('\n','')
    if '+' in line:
        operators = re.findall('[+,*]',line)
    else:
        nums.append([int(d) for d in re.findall('\d+',line)])
        data.append(line)
f.close()

#Ga in de andere richting door de data,van links naar rechts 
current_numbers=[]
for ind in range(0,len(data[0])):
    num_string=data[0][ind]+data[1][ind]+data[2][ind]+data[3][ind]#van onder naar boven
    if num_string=='    ':#lege kolom, door naar getallen voor volgende operator
        nums_p2.append(current_numbers)
        current_numbers=[]
    else:
        current_numbers.append(int(num_string))
nums_p2.append(current_numbers)


for n_op,op in enumerate(operators):
    
    numbers=list()
    for row in nums:
        numbers.append(row[n_op])
        
    if op=='+':
        total1=0
        total2=0
        for n in numbers:
            total1+=n
        for m in nums_p2[n_op]:
            total2+=m        
    else:
        total1=1
        total2=1
        for n in numbers:
            total1*=n
        for m in nums_p2[n_op]:
            total2*=m
    p1+=total1
    p2+=total2            
        


print("Part 1",p1)
print("Part 2",p2)
print("--- %s ms ---" % ((time.time_ns() - start_time)/1000000))