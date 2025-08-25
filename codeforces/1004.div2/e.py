# -*- coding: utf-8 -*-

"""
E. White Magic
time limit per test2 seconds
memory limit per test256 megabytes

We call a sequence a1,a2,…,an
 magical if for all 1≤i≤n−1
 it holds that: min(a1,…,ai)≥mex(ai+1,…,an)
. In particular, any sequence of length 1
 is considered magical.

The minimum excluded (MEX) of a collection of integers a1,a2,…,ak
 is defined as the smallest non-negative integer t
 which does not occur in the collection a
.

You are given a sequence a
 of n
 non-negative integers. Find the maximum possible length of a magical subsequence∗
 of the sequence a
.

∗
A sequence a
 is a subsequence of a sequence b
 if a
 can be obtained from b
 by the deletion of several (possibly, zero or all) element from arbitrary positions.

Input
Each test contains multiple test cases. The first line contains the number of test cases t
 (1≤t≤104
). The description of the test cases follows.

The first line of each test case contains an integer n
 (1≤n≤2⋅105
) — the length of the sequence a
.

The second line of each test case contains n
 integers a1,a2,…,an
 (0≤ai≤109
) — the elements of the sequence a
.

It is guaranteed that the sum of n
 across all test cases does not exceed 2⋅105
.

Output
For each test case, output a single number — the maximum possible length of a magical subsequence of the sequence a
.

Example
InputCopy
8
5
4 3 2 1 0
6
4 3 3 2 1 0
4
2 0 1 2
1
777
4
1000000000 1 7 9
2
0 1
2
1 2
4
0 1 0 1
OutputCopy
5
5
3
1
4
2
2
3
Note
In the first test case, the sequence [4,3,2,1,0]
 is magical, since:

min(4)=4,mex(3,2,1,0)=4
. 4≥4
min(4,3)=3,mex(2,1,0)=3
. 3≥3
min(4,3,2)=2,mex(1,0)=2
. 2≥2
min(4,3,2,1)=1,mex(0)=1
. 1≥1
In the second test case, the sequence [4,3,3,2,1,0]
 is not magical, since min(4,3)=3,mex(3,2,1,0)=4
, 3<4
. However, the subsequence [4,3,2,1,0]
 of this sequence is magical, so the answer is 5
.
"""

import string
import heapq
from typing import List
from collections import defaultdict
import sys

def codeforces(self, head: Optional[ListNode]) -> List[int]:
    ll = len(nums)
    result = 0

    for ii in range(ll):
        pass

    return result

if __name__ ==  "__main__":
    t = int(input())
    for _ in range(t):
        n,m = list(map(int, input().split()))
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        print(codeforces(n,1,a,b))
