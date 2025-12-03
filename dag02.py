# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 22:09:16 2024

@author: Paul
"""

import time
start_time = time.time_ns()
p1,p2=[0,0]

def check_pattern(input_id):
    if input_id[:len(input_id)//2]==input_id[len(input_id)//2:]:
        return int(input_id)
    return 0

def check_pattern2(input_id):
    for i in range(1,len(input_id)//2+1):
        if input_id[:i]*(len(input_id)//i)==input_id:
            return int(input_id)
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
        p1+=check_pattern(str(n))
        p2+=check_pattern2(str(n))

print("String comparison")
print("Part 1",p1)
print("Part 2",p2)
print("--- %s ms ---" % ((time.time_ns() - start_time)/1000000))