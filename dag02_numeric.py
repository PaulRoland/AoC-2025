# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 22:09:16 2024

@author: Paul
"""

import time
import math
start_time = time.time_ns()
p1,p2=[0,0]

def check_pattern(n,mindigits=1):
    for length in range(mindigits,math.floor(math.log10(n)+1)):
        divider=10**length
        compare=n%divider
        option=True
        rem=n
        while rem>divider:
            digits=(rem//divider)%divider
            if digits==compare:
                rem=rem//divider
            else:
                option=False
                break
        
        if option==True and rem==compare and rem>(divider/10)-1:
            #print("option",n,compare,divider)
            return n
    return 0

f = open("input.txt", "r")
for i,line in enumerate(f):
    #line=line.replace('(','').replace(')','').replace('=','').replace('\n','')
    line=line.replace('\n','')
    id_list=line.split(',')
f.close()

for ids in id_list:
    a,b=ids.split('-')
    for n in range(int(a),int(b)+1):
        p1+=check_pattern(n,(math.floor(math.log10(n))+2)//2)
        p2+=check_pattern(n)

print("Numeric")
print("Part 1",p1)
print("Part 2",p2)
print("--- %s ms ---" % ((time.time_ns() - start_time)/1000000))