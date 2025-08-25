# -*- coding: utf-8 -*-

"""
B. Robot Program
time limit per test2 seconds
memory limit per test512 megabytes
There is a robot on the coordinate line. Initially, the robot is located at the point x
 (x≠0
). The robot has a sequence of commands of length n
 consisting of characters, where L represents a move to the left by one unit (from point p
 to point (p−1)
) and R represents a move to the right by one unit (from point p
 to point (p+1)
).

The robot starts executing this sequence of commands (one command per second, in the order they are presented). However, whenever the robot reaches the point 0
, the counter of executed commands is reset (i. e. it starts executing the entire sequence of commands from the very beginning). If the robot has completed all commands and is not at 0
, it stops.

Your task is to calculate how many times the robot will enter the point 0
 during the next k
 seconds.
"""

import string
import heapq
from typing import List
from collections import defaultdict
import sys

def codeforces(n: int, x: int, k: int, ss: str):
    result = 0
    
    ###1. start from x, to check if we can move to 0
    indexs = 0
    if x:
        while k:
            if x == 0:
                indexs = 0
                break
            
            if indexs == n:
                return result
            
            if ss[indexs] == "L":
                x -= 1
            else:
                x += 1
            k -= 1
            indexs += 1
        result = 1
        
    ### start from 0, to check if we can move to 0 again
    countl = 0
    countr = 0
    back0 = -1
    for ii in range(min(k,n)):
        if ss[ii] == "L":
            countl += 1
        else:
            countr += 1
            
        if countl == countr:
            back0 = ii+1
            break
        
        if ii == n-1:
            return result
        if ii == k-1:
            return result
            
    if back0 > 0:
        result += k//back0
    
    return result
 
if __name__ ==  "__main__":
    t = int(input())
    for _ in range(t):
        n,x,k = list(map(int, input().split()))
        ss = input()
        print(codeforces(n,x,k,ss))
