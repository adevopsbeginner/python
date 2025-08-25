# -*- coding: utf-8 -*-

"""
D - Magnets / 
Time Limit: 2 sec / Memory Limit: 1024 MB

Score : 
1000 points

Problem Statement
You are given two length-
N strings 
A=A 
1
​
 A 
2
​
 …A 
N
​
  and 
B=B 
1
​
 B 
2
​
 …B 
N
​
 , each consisting of 0 and 1.

There are 
N squares aligned in a row from left to right. For 
i=1,2,…,N, the 
i-th square from the left is called square 
i. Initially, square 
i contains a piece if 
A 
i
​
 = 1, and no piece if 
A 
i
​
 = 0.

You may repeat the following operation any number of times (possibly zero):

Choose an integer 
i between 
1 and 
N, inclusive.
Move all pieces simultaneously one square closer to square 
i. That is, for each piece, let square 
j be its current position and square 
j 
′
  be its new position, and the following holds:
if 
i<j, then 
j 
′
 =j−1;
if 
i>j, then 
j 
′
 =j+1;
if 
i=j, then 
j 
′
 =j.
Determine whether it is possible to reach a configuration satisfying the following condition, and if it is possible, find the minimum number of operations needed to do so:

For every 
i=1,2,…,N, there is at least one piece in square 
i if and only if 
B 
i
​
 = 1.

You are given 
T independent test cases. Print the answer for each of them.

Constraints
1≤T≤2×10 
5
 
1≤N≤10 
6
 
T and 
N are integers.
A and 
B are strings of length 
N, each consisting of 0 and 1.
There exists 
i such that 
A 
i
​
 = 1.
There exists 
i such that 
B 
i
​
 = 1.
The sum of 
N over all test cases is at most 
10 
6
 .
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
