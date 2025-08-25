# -*- coding: utf-8 -*-

"""
G - Unevenness / 
Time Limit: 2 sec / Memory Limit: 1024 MB

×
It is prohibited to use generative AI in ongoing AtCoder contests. Please refer to the following rules for more details.

AtCoder Rules against Generative AI - Version 20241206


Score : 
675 points

Problem Statement
There is a grid with 
N rows and 
N columns. Let 
(i,j) denote the cell at the 
i-th row and 
j-th column. 
(i,j) contains an integer 
A 
i,j
​
 .
You are also given two coprime positive integers 
P and 
Q.

You may perform the following operation any number of times (possibly zero), as long as the total cost does not exceed 
Q
P
​
 :

Choose a real number 
x. Choose one cell in the grid and either increase or decrease the value in that cell by 
x. This operation incurs a cost of 
x.
After performing all operations, let 
B 
i,j
​
  be the value in cell 
(i,j). Define the non-uniformity 
U as the sum of absolute differences of adjacent cells. Formally,

U= 
i=1
∑
N
​
  
j=1
∑
N−1
​
 ∣B 
i,j
​
 −B 
i,j+1
​
 ∣+ 
i=1
∑
N−1
​
  
j=1
∑
N
​
 ∣B 
i,j
​
 −B 
i+1,j
​
 ∣.
Find the minimum possible value of 
U after performing the operations in an optimal way, and print that value. Also, print one valid final configuration 
B 
i,j
​
  that achieves this minimum 
U.

Constraints
2≤N≤10
1≤P≤10 
12
 
1≤Q≤10 
12
 
gcd(P,Q)=1
0≤A 
i,j
​
 ≤10
All input values are integers.
Input
The input is given from Standard Input in the following format:

N 
P 
Q
A 
1,1
​
  
A 
1,2
​
  
… 
A 
1,N
​
 
A 
2,1
​
  
A 
2,2
​
  
… 
A 
2,N
​
 
⋮
A 
N,1
​
  
A 
N,2
​
  
… 
A 
N,N
​
 
Output
Print 
U and 
B 
i,j
​
  in the following format:

U
B 
1,1
​
  
B 
1,2
​
  
… 
B 
1,N
​
 
B 
2,1
​
  
B 
2,2
​
  
… 
B 
2,N
​
 
⋮
B 
N,1
​
  
B 
N,2
​
  
… 
B 
N,N
​
 
Your output is considered correct if it meets all of the following conditions. (Note that the tolerance for 
U is very strict.)

The absolute or relative error between your output 
U and its true minimum value is at most 
2 
−51
 (≈4.44×10 
−16
 ).
The absolute or relative error between 
∑ 
i=1
N
​
 ∑ 
j=1
N−1
​
 ∣B 
i,j
​
 −B 
i,j+1
​
 ∣+∑ 
i=1
N−1
​
 ∑ 
j=1
N
​
 ∣B 
i,j
​
 −B 
i+1,j
​
 ∣ and 
U is at most 
10 
−10
 .
∑ 
i=1
N
​
 ∑ 
j=1
N
​
 ∣A 
i,j
​
 −B 
i,j
​
 ∣ is at most 
Q
P
​
 +max(1, 
Q
P
​
 )×10 
−10
 .
If there are multiple solutions, you may print any one of them.
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
