# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 22:09:16 2024
New template 02-12-2025
@author: Paul
"""

import time
start_time = time.time_ns()
def n_paths(start,end):
    n=0
    if start in mem:
        return mem[start]
    if start==end:
        return 1
    if start=='out':
        #Dit is voor p2 tel geen oplossingen die langs out komen ondertussen!
        return 0
    for to in conn[start]:
        n+=n_paths(to,end)
    mem[start]=n
    return n
    
conn=dict()
f = open("input.txt", "r")
for i,line in enumerate(f):
    line=line.replace(': ',' ').replace('\n','').split(' ')
    conn[line[0]]=line[1:]
f.close()

mem=dict()
p1=n_paths('you','out')
#Mogelijke paden
paths=[['svr','fft','dac','out'],
       ['svr','dac','fft','out']]
for path in paths:
    path_nsol=1
    for start,end in zip(path,path[1:]):
        mem=dict()
        path_nsol*=n_paths(start,end)
    p2+=path_nsol

print("Part 1",p1)
print("Part 2",p2)
print("--- %s ms ---" % ((time.time_ns() - start_time)/1000000))
