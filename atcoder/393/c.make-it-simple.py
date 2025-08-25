# -*- coding: utf-8 -*-

"""
C - Make it Simple / 
Time Limit: 2 sec / Memory Limit: 1024 MB

×
It is prohibited to use generative AI in ongoing AtCoder contests. Please refer to the following rules for more details.

AtCoder Rules against Generative AI - Version 20241206


Score : 
300 points

Problem Statement
You are given an undirected graph with 
N vertices and 
M edges, where the vertices are numbered 
1 through 
N and the edges are numbered 
1 through 
M. Edge 
i connects vertices 
u 
i
​
  and 
v 
i
​
 .
To make the graph simple by removing edges, what is the minimum number of edges that must be removed?
Here, a graph is called simple if and only if it does not contain self-loops or multi-edges.

Constraints
1≤N≤2×10 
5
 
0≤M≤5×10 
5
 
1≤u 
i
​
 ≤N
1≤v 
i
​
 ≤N
All input values are integers.
"""

import string
import heapq
from typing import List
from collections import defaultdict
import sys

def find_parent(parent, node):
  if parent[node] != node:
    parent[node] = find_parent(parent, parent[node])
  return parent[node]

def union(parent, rank, u, v):
  root_u = find_parent(parent, u)
  root_v = find_parent(parent, v)
  
  if root_u != root_v:
    if rank[root_u] > rank[root_v]:
      parent[root_v] = root_u
    elif rank[root_u] < rank[root_v]:
      parent[root_u] = root_v
    else:
      parent[root_v] = root_u
      rank[root_u] += 1
      
    ### no cycle formed
    return False

  ### cycle formed
  return True

def atcoder(n: int, m: int, edges: list):
    result = 0
    last_u = -1
    last_v = -1
    edges.sort()
    for u, v in edges:
      ### same vertice
      if u == v:
        result += 1
        continue
      
      ### duplicate edges
      if u == last_u and v == last_v:
        result += 1
        last_u = u
        last_v = v
        continue
      def atcoder(n: int, m: int, edges: list):
    result = 0
    last_u = -1
    last_v = -1
    edges.sort()
    for u, v in edges:
      ### same vertice
      if u == v:
        result += 1
        continue
      
      ### duplicate edges
      if u == last_u and v == last_v:
        result += 1
        last_u = u
        last_v = v
        continue
      last_u = u
      last_v = v

    return result


if __name__ == "__main__":
    n, m = list(map(int, input().split()))
    edges = []
    for ii in range(m):
      u, v = list(map(int, input().split()))
      edges.append([min(u,v), max(u, v)])
    print(atcoder(n,m,edges))

    return result


def atcoder(n: int, m: int, edges: list):
    result = 0
    last_u = -1
    last_v = -1
    edges.sort()
    for u, v in edges:
      ### same vertice
      if u == v:
        result += 1
        continue
      
      ### duplicate edges
      if u == last_u and v == last_v:
        result += 1
        last_u = u
        last_v = v
        continue
      last_u = u
      last_v = v

    return result


if __name__ == "__main__":
    n, m = list(map(int, input().split()))
    edges = []
    for ii in range(m):
      u, v = list(map(int, input().split()))
      edges.append([min(u,v), max(u, v)])
    print(atcoder(n,m,edges))