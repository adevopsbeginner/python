# -*- coding: utf-8 -*-

"""
F. We Be Summing
time limit per test3 seconds
memory limit per test256 megabytes
You are given an array a
 of length n
 and an integer k
.

Call a non-empty array b
 of length m
 epic if there exists an integer i
 where 1≤i<m
 and min(b1,…,bi)+max(bi+1,…,bm)=k
.

Count the number of epic subarrays∗
 of a
.

∗
An array a
 is a subarray of an array b
 if a
 can be obtained from b
 by the deletion of several (possibly, zero or all) elements from the beginning and several (possibly, zero or all) elements from the end.

Input
The first line contains an integer t
 (1≤t≤104
) — the number of testcases.

The first line of each testcase contains integers n
 and k
 (2≤n≤2⋅105
; n<k<2⋅n
) — the length of the array a
 and k
.

The second line of each testcase contains n
 integers a1,a2,…,an
 (1≤ai≤n
).

The sum of n
 across all testcases does not exceed 2⋅105
.

Output
For each testcase, output the number of epic contiguous subarrays of a
.
"""

import string
import heapq
from typing import List
from collections import defaultdict
import sys

def codeforces(n: int, s: str):
    ll = len(nums)
    result = 0

    for ii in range(ll):
        pass

    return result

if __name__ ==  "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        s = input()
        print(codeforces(n,s))

