# -*- coding: utf-8 -*-

"""
B - Broken Wheel / 
Time Limit: 2 sec / Memory Limit: 1024 MB

Score : 
800 points

Problem Statement
You are given a positive integer 
N and a length-
N string 
s 
0
​
 s 
1
​
 …s 
N−1
​
  consisting only of 0 and 1.

Consider a simple undirected graph 
G with 
(N+1) vertices numbered 
0,1,2,…,N, and the following edges:

For each 
i=0,1,…,N−1, there is an undirected edge between vertices 
i and 
(i+1)modN.
For each 
i=0,1,…,N−1, there is an undirected edge between vertices 
i and 
N if and only if 
s 
i
​
 = 1.
There are no other edges.
Furthermore, create a directed graph 
G 
′
  by assigning a direction to each edge of 
G. That is, for each undirected edge 
{u,v} in 
G, replace it with either a directed edge 
(u,v) from 
u to 
v or a directed edge 
(v,u) from 
v to 
u.

For each 
i=0,1,…,N, let 
d 
i
​
  be the in-degree of vertex 
i in 
G 
′
 . Print the number, modulo 
998244353, of distinct sequences 
(d 
0
​
 ,d 
1
​
 ,…,d 
N
​
 ) that can be obtained.

Constraints
3≤N≤10 
6
 
N is an integer.
Each 
s 
i
​
  is 0 or 1.
"""

import string
import heapq
from typing import List
from collections import defaultdict
import sys

def atcoder(n: int, arr: list):
    ll = len(arr)
    result = 0

    for ii in range(ll):
        pass

    return result


if __name__ == "__main__":
  t = int(input())
  for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(atcoder(n,arr))
