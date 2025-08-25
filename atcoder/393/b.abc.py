# -*- coding: utf-8 -*-

"""
B - A..B..C / 
Time Limit: 2 sec / Memory Limit: 1024 MB

×
It is prohibited to use generative AI in ongoing AtCoder contests. Please refer to the following rules for more details.

AtCoder Rules against Generative AI - Version 20241206


Score : 
200 points

Problem Statement
A string 
S is given.

Find how many places in 
S have A, B, and C in this order at even intervals.

Specifically, find the number of triples of integers 
(i,j,k) that satisfy all of the following conditions. Here, 
∣S∣ denotes the length of 
S, and 
S 
x
​
  denotes the 
x-th character of 
S.

1≤i<j<k≤∣S∣
j−i=k−j
S 
i
​
 = A
S 
j
​
 = B
S 
k
​
 = C
Constraints
S is an uppercase English string with length between 
3 and 
100, inclusive.
"""

import string
import heapq
from typing import List
from collections import defaultdict
import sys
  
def atcoder(s: str):
  ll = len(s)
  result = 0
  for ii in range(ll):
    if s[ii] == "B":
      for jj in range(ii):
        if s[jj] == "A":
          if ii+(ii-jj) < ll and s[ii+(ii-jj)] == "C":
            result += 1
            
    return result


if __name__ == "__main__":
  s = input()
  print(atcoder(s))