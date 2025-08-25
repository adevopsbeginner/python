# -*- coding: utf-8 -*-

"""
E - GCD of Subset / 
Time Limit: 2 sec / Memory Limit: 1024 MB

×
It is prohibited to use generative AI in ongoing AtCoder contests. Please refer to the following rules for more details.

AtCoder Rules against Generative AI - Version 20241206


Score : 
475 points

Problem Statement
You are given a sequence 
A=(A 
1
​
 ,A 
2
​
 ,…,A 
N
​
 ) of length 
N and a positive integer 
K (at most 
N).
For each 
i=1,2,…,N, solve the following problem:

When you choose 
K elements from 
A that include 
A 
i
​
 , find the maximum possible GCD (greatest common divisor) of those chosen elements.
Constraints
1≤K≤N≤1.2×10 
6
 
1≤A 
i
​
 ≤10 
6
 
All input values are integers.
Input
The input is given from Standard Input in the following format:

N 
K
A 
1
​
  
A 
2
​
  
… 
A 
N
​
 
Output
Print 
N lines. The 
j-th line should contain the answer for 
i=j.
"""

import string
import heapq
from typing import List
from collections import defaultdict
import sys

def atcoder(n: int, arr: []):
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
    print(atcoder(n,q))
