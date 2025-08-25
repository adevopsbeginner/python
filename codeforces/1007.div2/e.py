# -*- coding: utf-8 -*-

"""
E. LeaFall
time limit per test3 seconds
memory limit per test512 megabytes

You are given a tree∗
 with n
 vertices. Over time, each vertex i
 (1≤i≤n
) has a probability of piqi
 of falling. Determine the expected value of the number of unordered pairs†
 of distinct vertices that become leaves‡
 in the resulting forest§
, modulo 998244353
.

Note that when vertex v
 falls, it is removed along with all edges connected to it. However, adjacent vertices remain unaffected by the fall of v
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
