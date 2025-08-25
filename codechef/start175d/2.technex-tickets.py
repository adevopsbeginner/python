# -*- coding: utf-8 -*-

"""
Technex Tickets
You are standing in a queue that is infinitely long, waiting to get tickets for various events during Technex.
The ticket distribution follows these rules:

Every second, tickets are given to the 
1
s
t
1 
st
  and 
3
r
d
3 
rd
  persons in the queue.
After receiving their tickets, those people leave the queue.
The person who was originally in the 
2
n
d
2 
nd
  position (before the 
1
s
t
1 
st
  and 
3
r
d
3 
rd
  people left) moves up to the 
1
s
t
1 
st
  position.
This process repeats every second, with the 
1
s
t
1 
st
  and 
3
r
d
3 
rd
  persons receiving tickets and leaving.
Initially, you are at position 
N
N in the queue.

Determine after how many seconds you will get the tickets.

Input Format
The first line of input will contain a single integer 
T
T, denoting the number of test cases.
Each test case contains a single line of input 
N
N your initial position in the line.
Output Format
For each test case, output on a new line after how many seconds will you get the tickets.

Constraints
1
≤
T
≤
1000
1≤T≤1000
1
≤
N
≤
1000
1≤N≤1000
"""

import string
import heapq
from typing import List
from collections import defaultdict
import sys


# cook your dish here

def codechef(n: int):
    q = [0,1,2,1,3,2]
    if n < 6:
        return q[n]
    if n%2 == 0:
        return n//2+1
    return n//2

    
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        print(codechef(n))

    # t = int(sys.stdin.readline().strip())
    # for _ in range(t):
    #     stra = sys.stdin.readline().strip()
    #     strb = sys.stdin.readline().strip()
    #     codechef(stra,strb)
