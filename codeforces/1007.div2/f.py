# -*- coding: utf-8 -*-

"""
F. Towering Arrays
time limit per test6 seconds
memory limit per test1024 megabytes

An array b=[b1,b2,…,bm]
 of length m
 is called p
-towering if there exists an index i
 (1≤i≤n
) such that for every index j
 (1≤j≤m
), the following condition holds:
bj≥p−|i−j|.

Given an array a=[a1,a2,…,an]
 of length n
, you can remove at most k
 elements from it. Determine the maximum value of p
 for which the remaining array can be made p
-towering.
"""

import string
import heapq
from typing import List
from collections import defaultdict
import sys

def codeforces(n: int, arr: list):

if __name__ ==  "__main__":
    t = int(input())
    for _ in range(t):
        n,m = list(map(int, input().split()))
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        print(codeforces(n,1,a,b))
