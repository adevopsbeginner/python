# -*- coding: utf-8 -*-

"""
B - cat / 
Time Limit: 2 sec / Memory Limit: 1024 MB

×
It is prohibited to use generative AI in ongoing AtCoder contests. Please refer to the following rules for more details.

AtCoder Rules against Generative AI - Version 20241206


Score : 
200 points

Problem Statement
You are given 
N strings 
S 
1
​
 ,S 
2
​
 ,…,S 
N
​
 , each consisting of lowercase English letters. The lengths of these strings are all distinct.

Sort these strings in ascending order of length, and then concatenate them in that order to form a single string.

Constraints
2≤N≤50
N is an integer.
Each 
S 
i
​
  is a string consisting of lowercase English letters with length between 
1 and 
50, inclusive.
If 
i

=j, the length of 
S 
i
​
  is different from the length of 
S 
j
​
 .

"""

import string
import heapq
from typing import List
from collections import defaultdict
import sys

def atcoder(n: int, arr: list):
    arr.sort(key=lambda x:len(x))
    result = "".join(arr)

    return result

if __name__ == "__main__":
  n = int(input())
  arr = []
  for _ in range(n):
    s = input()
    arr.append(s)
  print(atcoder(n,arr))

