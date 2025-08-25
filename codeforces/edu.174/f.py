# -*- coding: utf-8 -*-

"""
F. Graph Inclusion
time limit per test5 seconds
memory limit per test512 megabytes
A connected component of an undirected graph is defined as a set of vertices S
 of this graph such that:

for every pair of vertices (u,v)
 in S
, there exists a path between vertices u
 and v
;
there is no vertex outside S
 that has a path to a vertex within S
.
For example, the graph in the picture below has three components: {1,3,7,8}
, {2}
, {4,5,6}
.


We say that graph A
 includes graph B
 if every component of graph B
 is a subset of some component of graph A
.

You are given two graphs, A
 and B
, both consisting of n
 vertices numbered from 1
 to n
. Initially, there are no edges in the graphs. You must process queries of two types:

add an edge to one of the graphs;
remove an edge from one of the graphs.
After each query, you have to calculate the minimum number of edges that have to be added to A
 so that A
 includes B
, and print it. Note that you don't actually add these edges, you just calculate their number.

Input
The first line contains two integers n
 and q
 (2≤n≤4⋅105
; 1≤q≤4⋅105
) — the number of vertices and queries, respectively.

Next, there are q
 lines, where the i
-th line describes the i
-th query. The description of the query begins with the character ci
 (either A or B) — the graph to which the query should be applied. Then, two integers xi
 and yi
 follow (1≤xi,yi≤n
; xi≠yi
). If there is an edge (xi,yi)
 in the corresponding graph, it should be removed; otherwise, it should be added to that graph.

Output
For each query, print one integer — the minimum number of edges that you have to add to the graph A
 so that it includes B
.

Example
InputCopy
6 9
A 2 3
B 1 3
A 2 1
A 3 2
B 5 6
A 6 5
A 3 4
A 4 2
A 4 3
OutputCopy
0
1
0
1
2
1
1
0
1


"""

import string
import heapq
from typing import List
from collections import defaultdict
import sys

def codeforces(self, head: Optional[ListNode]) -> List[int]:
    ll = len(nums)
    result = 0

    for ii in range(ll):
        pass

    return result

if __name__ ==  "__main__":
    t = int(input())
    for _ in range(t):
        n,m = list(map(int, input().split()))
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        print(codeforces(n,1,a,b))
