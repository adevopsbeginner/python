# -*- coding: utf-8 -*-

"""
F - Prefix LIS Query / 
Time Limit: 2 sec / Memory Limit: 1024 MB

×
It is prohibited to use generative AI in ongoing AtCoder contests. Please refer to the following rules for more details.

AtCoder Rules against Generative AI - Version 20241206


Score : 
500 points

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
N.

Answer 
Q queries. The 
i-th query (
1≤i≤Q) is as follows:

You are given integers 
R 
i
​
  and 
X 
i
​
 . Consider a subsequence (not necessarily contiguous) of 
(A 
1
​
 ,A 
2
​
 ,…,A 
R 
i
​
 
​
 ) that is strictly increasing and consists only of elements at most 
X 
i
​
 . Find the maximum possible length of such a subsequence. It is guaranteed that 
X 
i
​
 ≥min{A 
1
​
 ,A 
2
​
 ,…,A 
R 
i
​
 
​
 }.
Constraints
1≤N,Q≤2×10 
5
 
1≤A 
i
​
 ≤10 
9
 
1≤R 
i
​
 ≤N
min{A 
1
​
 ,A 
2
​
 ,…,A 
R 
i
​
 
​
 }≤X 
i
​
 ≤10 
9
 
All input values are integers.
Input
The input is given from Standard Input in the following format:

N 
Q
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
 
R 
1
​
  
X 
1
​
 
R 
2
​
  
X 
2
​
 
⋮
R 
Q
​
  
X 
Q
​
 
Output
Print 
Q lines. The 
i-th line should contain the answer to the 
i-th query.
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
