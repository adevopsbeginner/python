# -*- coding: utf-8 -*-

"""
D2. Infinite Sequence (Hard Version)
time limit per test2 seconds
memory limit per test256 megabytes

This is the hard version of the problem. The difference between the versions is that in this version, l≤r
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

def codeforces(n: int, arr: list):

if __name__ ==  "__main__":
    t = int(input())
    for _ in range(t):
        n,m = list(map(int, input().split()))
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        print(codeforces(n,1,a,b))
