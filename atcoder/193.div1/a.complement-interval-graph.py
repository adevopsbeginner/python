# -*- coding: utf-8 -*-

"""
A - Complement Interval Graph / 
Time Limit: 2 sec / Memory Limit: 1024 MB

Score : 
700 points

Problem Statement
For integers 
l,r, let 
[l,r] denote the set of all integers from 
l through 
r. That is, 
[l,r]={l,l+1,l+2,…,r−1,r}.

You are given 
N pairs of integers 
(L 
1
​
 ,R 
1
​
 ),(L 
2
​
 ,R 
2
​
 ),…,(L 
N
​
 ,R 
N
​
 ). Based on these pairs, consider an undirected graph 
G defined as follows:

It has 
N vertices numbered 
1,2,…,N.
For all 
i,j∈[1,N], there is an undirected edge between vertices 
i and 
j if and only if the intersection of 
[L 
i
​
 ,R 
i
​
 ] and 
[L 
j
​
 ,R 
j
​
 ] is empty.
In addition, for each 
i=1,2,…,N, define the weight of vertex 
i to be 
W 
i
​
 .

You are given 
Q queries about 
G. Process these queries in the order they are given. For each 
i=1,2,…,Q, the 
i-th query is the following:

You are given integers 
s 
i
​
  and 
t 
i
​
  (both between 
1 and 
N, inclusive) such that 
s 
i
​
 

=t 
i
​
 . Determine whether there exists a path from vertex 
s 
i
​
  to vertex 
t 
i
​
  in 
G. If it exists, print the minimum possible weight of such a path.

Here, the weight of a path from vertex 
s to vertex 
t is defined as the sum of the weights of the vertices on that path (including both endpoints 
s and 
t).

Constraints
2≤N≤2×10 
5
 
1≤Q≤2×10 
5
 
1≤W 
i
​
 ≤10 
9
 
1≤L 
i
​
 ≤R 
i
​
 ≤2N
1≤s 
i
​
 ,t 
i
​
 ≤N
s 
i
​
 

=t 
i
​
 
All input values are integers.
"""

import string
import heapq
from typing import List
from collections import defaultdict
import sys

from collections import defaultdict
import heapq

class AtCoder:
  def dijkstra(self, n, w, graph, start):
      # Min heap to store (cost, node)
      pq = [(w[start], start)]  # Start with the node's own weight
      
      while pq:
          curr_cost, u = heapq.heappop(pq)
          
          if curr_cost == -1 or curr_cost > self.grid[start][u]:
              continue
          
          for v in self.graph[u]:
              new_cost = curr_cost + w[v]
              if self.grid[start][v] == -1 or new_cost < self.grid[start][v]:
                  self.grid[start][v] = new_cost
                  heapq.heappush(pq, (new_cost, v))

  def __init__(self, n: int, w: list, lr: list):
    self.n = n
    self.w = w
    self.graph = defaultdict(list)
    ll = len(lr)
    for ii in range(ll-1):
      for jj in range(ii+1, ll):
        if lr[ii][0] > lr[jj][1] or lr[ii][1] < lr[jj][0]:
          self.graph[ii].append(jj)
          self.graph[jj].append(ii)

    self.grid = [[-1 for cc in range(n)] for rr in range(n)]
    for ii in range(n):
      self.grid[ii][ii] = self.w[ii]

    for ii in range(n):
        self.dijkstra(n, w, self.graph, ii)
    
    #print(self.grid)

    return


  def distance(self, u: int, v: int):
    #print(u, v)
    #return self.path[u][v]
    return self.grid[u][v]

if __name__ == "__main__":
  n = int(input())
  w = list(map(int, input().split()))
  lr = []
  for _ in range(n):
    l, r = list(map(int, input().split()))
    lr.append([l,r])
  atcoder = AtCoder(n,w,lr)

  q = int(input())
  for _ in range(q):
    u, v = list(map(int, input().split()))
    print(atcoder.distance(u-1, v-1))

