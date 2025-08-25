# -*- coding: utf-8 -*-

"""
C. Trapmigiano Reggiano
time limit per test2 seconds
memory limit per test256 megabytes

In an Italian village, a hungry mouse starts at vertex st
 on a given tree∗
 with n
 vertices.

Given a permutation p
 of length n
†
, there are n
 steps. For the i
-th step:

A tempting piece of Parmesan cheese appears at vertex pi
. If the mouse is currently at vertex pi
, it will stay there and enjoy the moment. Otherwise, it will move along the simple path to vertex pi
 by one edge.
Your task is to find such a permutation so that, after all n
 steps, the mouse inevitably arrives at vertex en
, where a trap awaits.

Note that the mouse must arrive at en
 after all n
 steps, though it may pass through en
 earlier during the process.
"""

import string
import heapq
from typing import List
from collections import defaultdict
import sys

from collections import defaultdict
 
def codeforces(n: int, st: int, en: int, edges: list):
    def dfs(node):
        if node in visited:
            return
        visited.add(node)
        result.append(node)
        for each in sorted(graph[node]):
            dfs(each)
            
    graph = defaultdict(list)
    for u,v in edges:
        graph[u].append(v)
        graph[v].append(u)
        
    visited = set()
    result = []
    dfs(st)
    result.remove(en)
    result.append(en)
    result = list(map(str, result))
    
    return " ".join(result)
 
if __name__ ==  "__main__":
    t = int(input())
    for _ in range(t):
        n,st,en = list(map(int, input().split()))
        edges = []
        for ii in range(n-1):
            u, v = list(map(int, input().split()))
            edges.append([u,v])
        print(codeforces(n,st,en,edges))
