# -*- coding: utf-8 -*-

"""
D - Swap to Gather / 
Time Limit: 2 sec / Memory Limit: 1024 MB

×
It is prohibited to use generative AI in ongoing AtCoder contests. Please refer to the following rules for more details.

AtCoder Rules against Generative AI - Version 20241206


Score : 
425 points

Problem Statement
You are given a string 
S of length 
N consisting of 0 and 1. It is guaranteed that 
S contains at least one 1.

You may perform the following operation any number of times (possibly zero):

Choose an integer 
i (
1≤i≤N−1) and swap the 
i-th and 
(i+1)-th characters of 
S.
Find the minimum number of operations needed so that all 1s are contiguous.

Here, all 1s are said to be contiguous if and only if there exist integers 
l and 
r (
1≤l≤r≤N) such that the 
i-th character of 
S is 1 if and only if 
l≤i≤r, and 0 otherwise.

Constraints
2≤N≤5×10 
5
 
N is an integer.
S is a length 
N string of 0 and 1.
S contains at least one 1.
Input
The input is given from Standard Input in the following format:

N
S
Output
Print the answer.
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
