# -*- coding: utf-8 -*-

"""
D1. Infinite Sequence (Easy Version)
time limit per test2 seconds
memory limit per test256 megabytes

This is the easy version of the problem. The difference between the versions is that in this version, l=r
. You can hack only if you solved all versions of this problem.

You are given a positive integer n
 and the first n
 terms of an infinite binary sequence a
, which is defined as follows:

For m>n
, am=a1⊕a2⊕…⊕a⌊m2⌋
∗
.
Your task is to compute the sum of elements in a given range [l,r]
: al+al+1+…+ar
.
"""

import string
import heapq
from typing import List
from collections import defaultdict
import sys

def codeforces(n: int, l: int, r: int, arr: list):
    if r <= n:
        return arr[r - 1]  # Since Python uses 0-based indexing
    
    # Compute prefix XOR for given values
    prefix_xor = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix_xor[i] = prefix_xor[i - 1] ^ arr[i - 1]
    
    # Compute a[r] using the recurrence relation
    computed_values = arr[:]
    while len(computed_values) <= r:
        m = len(computed_values)
        new_value = prefix_xor[m // 2]  # XOR of first m//2 elements
        computed_values.append(new_value)
        prefix_xor.append(prefix_xor[-1] ^ new_value)
    
    return computed_values[r - 1]
    
if __name__ ==  "__main__":
    t = int(input())
    for _ in range(t):
        n,l,r = list(map(int, input().split()))
        arr = list(map(int, input().split()))
        print(codeforces(n,l,r,arr))
