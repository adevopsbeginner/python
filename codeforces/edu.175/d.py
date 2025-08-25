# -*- coding: utf-8 -*-

"""
D. Tree Jumps
time limit per test2 seconds
memory limit per test512 megabytes
You are given a rooted tree, consisting of n
 vertices. The vertices in the tree are numbered from 1
 to n
, and the root is the vertex 1
. Let dx
 be the distance (the number of edges on the shortest path) from the root to the vertex x
.

There is a chip that is initially placed at the root. You can perform the following operation as many times as you want (possibly zero):

move the chip from the current vertex v
 to a vertex u
 such that du=dv+1
. If v
 is the root, you can choose any vertex u
 meeting this constraint; however, if v
 is not the root, u
 should not be a neighbor of v
 (there should be no edge connecting v
 and u
).

For example, in the tree above, the following chip moves are possible: 1→2
, 1→5
, 2→7
, 5→3
, 5→4
, 3→6
, 7→6
.

A sequence of vertices is valid if you can move the chip in such a way that it visits all vertices from the sequence (and only them), in the order they are given in the sequence.

Your task is to calculate the number of valid vertex sequences. Since the answer might be large, print it modulo 998244353
.
"""

import string
import heapq
from typing import List
from collections import defaultdict
import sys

def codeforces(n: int):

 
if __name__ ==  "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        print(codeforces(n))

if __name__ ==  "__main__":
    t = int(input())
    for _ in range(t):
        n,m = list(map(int, input().split()))
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        print(codeforces(n,1,a,b))
