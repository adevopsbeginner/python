# -*- coding: utf-8 -*-

"""
C2. Skibidus and Fanum Tax (hard version)
time limit per test2 seconds
memory limit per test256 megabytes
This is the hard version of the problem. In this version, m≤2⋅105
.

Skibidus has obtained two arrays a
 and b
, containing n
 and m
 elements respectively. For each integer i
 from 1
 to n
, he is allowed to perform the operation at most once:

Choose an integer j
 such that 1≤j≤m
. Set ai:=bj−ai
. Note that ai
 may become non-positive as a result of this operation.
Skibidus needs your help determining whether he can sort a
 in non-decreasing order∗
 by performing the above operation some number of times.

∗
a
 is sorted in non-decreasing order if a1≤a2≤…≤an
.

Input
The first line contains an integer t
 (1≤t≤104
) — the number of test cases.

The first line of each test case contains two integers n
 and m
 (1≤n≤2⋅105
, 1≤m≤2⋅105
).

The following line of each test case contains n
 integers a1,a2,…,an
 (1≤ai≤109
).

The following line of each test case contains m
 integers b1,b2,…,bm
 (1≤bi≤109
).

It is guaranteed that the sum of n
 and the sum of m
 over all test cases does not exceed 2⋅105
.

Output
For each test case, if it is possible to sort a
 in non-decreasing order, print "YES" on a new line. Otherwise, print "NO" on a new line.

You can output the answer in any case. For example, the strings "yEs", "yes", and "Yes" will also be recognized as positive responses.

Example
InputCopy
5
1 3
5
9 1 1000000000
3 2
1 4 3
3 4
4 3
2 4 6 5
6 1 8
5 2
6 4 5 4 5
4 1000
3 1
9 8 7
8
OutputCopy
YES
NO
YES
NO
YES
Note
In the first test case, [5]
 is already sorted.

In the second test case, it can be shown that it is impossible.

In the third test case, we can set a2:=b1−a2=6−4=2
 and a3:=b3−a3=8−6=2
. The sequence [2,2,2,5]
 is in nondecreasing order.

In the last case, we can apply operations on each index. The sequence becomes [−1,0,1]
, which is in nondecreasing order.
"""

import string
import heapq
from typing import List
from collections import defaultdict
import sys

def codeforces(n: int, m: int, a: [], b: []):
    lla = len(a)
    llb = len(b)
    b.sort()
    a[0] = min(a[0], b[0]-a[0])
    for ii in range(1, lla):
        if max(a[ii], b[-1]-a[ii]) < a[ii-1]:
            return "no"
        for jj in range(llb):
            if min(a[ii], b[jj]-a[ii]) >= a[ii-1]:
                a[ii] = min(a[ii], b[jj]-a[ii])
                break
            # else:
            #     a[ii] = max(a[ii], b[jj]-a[ii])
    if n >= 2 and a[-1] < a[-2]:
        if max(a[-1], b[-1]-a[-1]) < a[-2]:
            return "no"
    
    return "yes"
 
if __name__ ==  "__main__":
    t = int(input())
    for _ in range(t):
        n,m = list(map(int, input().split()))
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        print(codeforces(n,1,a,b))
