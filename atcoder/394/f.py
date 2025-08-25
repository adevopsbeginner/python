# -*- coding: utf-8 -*-

"""
F - Alkane / 
Time Limit: 2 sec / Memory Limit: 1024 MB

×
It is prohibited to use generative AI in ongoing AtCoder contests. Please refer to the following rules for more details.

AtCoder Rules against Generative AI - Version 20241206


Score : 
500 points

Problem Statement
You are given an undirected tree 
T with 
N vertices, numbered 
1,2,…,N. The 
i-th edge is an undirected edge connecting vertices 
A 
i
​
  and 
B 
i
​
 .

A graph is defined to be an alkane if and only if it satisfies the following conditions:

The graph is an undirected tree.
Every vertex has degree 
1 or 
4, and there is at least one vertex of degree 
4.
Determine whether there exists a subgraph of 
T that is an alkane, and if so, find the maximum number of vertices in such a subgraph.

Constraints
1≤N≤2×10 
5
 
1≤A 
i
​
 ,B 
i
​
 ≤N
The given graph is an undirected tree.
All input values are integers.
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
