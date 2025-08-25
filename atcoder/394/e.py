# -*- coding: utf-8 -*-

"""
E - Palindromic Shortest Path / 
Time Limit: 2 sec / Memory Limit: 1024 MB

×
It is prohibited to use generative AI in ongoing AtCoder contests. Please refer to the following rules for more details.

AtCoder Rules against Generative AI - Version 20241206


Score : 
450 points

Problem Statement
We have a directed graph with 
N vertices, numbered 
1,2,…,N.

Information about the edges is given by 
N 
2
  characters 
C 
1,1
​
 ,C 
1,2
​
 ,…,C 
1,N
​
 ,C 
2,1
​
 ,…,C 
N,N
​
 . Here, each 
C 
i,j
​
  is either a lowercase English letter or -.

If 
C 
i,j
​
  is a lowercase English letter, then there is exactly one directed edge from vertex 
i to vertex 
j labeled 
C 
i,j
​
 . If 
C 
i,j
​
  is -, there is no edge from vertex 
i to vertex 
j.

For each integer pair 
(i,j) with 
1≤i,j≤N, answer the following question:

Among all (not necessarily simple) paths from vertex 
i to vertex 
j whose concatenation of labels on the edges forms a palindrome, what is the length of the shortest such path? If there is no such path, the answer is 
−1.
Constraints
1≤N≤100
N is an integer.
Each 
C 
i,j
​
  is either a lowercase English letter or -.
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
