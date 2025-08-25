# -*- coding: utf-8 -*-

"""
A. Condorcet Elections
time limit per test2 seconds
memory limit per test1024 megabytes
It is a municipality election year. Even though the leader of the country has not changed for two decades, the elections are always transparent and fair.

There are n
 political candidates, numbered from 1
 to n
, contesting the right to govern. The elections happen using a variation of the Ranked Voting System. In their ballot, each voter will rank all n
 candidates from most preferable to least preferable. That is, each vote is a permutation of {1,2,…,n}
, where the first element of the permutation corresponds to the most preferable candidate.

We say that candidate a
 defeats candidate b
 if in more than half of the votes candidate a
 is more preferable than candidate b
.

As the election is fair and transparent, the state television has already decreed a list of m
 facts—the i
-th fact being "candidate ai
 has defeated candidate bi
"—all before the actual election!

You are in charge of the election commission and tallying up the votes. You need to present a list of votes that produces the outcome advertised on television, or to determine that it is not possible. However, you are strongly encouraged to find a solution, or you might upset higher-ups.
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
