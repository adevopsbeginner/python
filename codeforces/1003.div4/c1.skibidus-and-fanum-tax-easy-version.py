# -*- coding: utf-8 -*-

"""
C1. Skibidus and Fanum Tax (easy version)
time limit per test2 seconds
memory limit per test256 megabytes
This is the easy version of the problem. In this version, m=1
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
, m = 1
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
1 1
5
9
3 1
1 4 3
3
4 1
1 4 2 5
6
4 1
5 4 10 5
4
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

In the third test case, we can set a3:=b1−a3=6−2=4
. The sequence [1,4,4,5]
 is in nondecreasing order.

In the last case, we can apply operations on each index. The sequence becomes [−1,0,1]
, which is in nondecreasing order.
"""

import string
import heapq
from typing import List
from collections import defaultdict
import sys

def codeforces(n: int, m: int, a: [], b: int):
    ll = len(a)
    a[0] = min(a[0], b-a[0])
    for ii in range(1, ll):
        if max(a[ii], b-a[ii]) < a[ii-1]:
            return "no"
        if min(a[ii], b-a[ii]) >= a[ii-1]:
            a[ii] = min(a[ii], b-a[ii])
        else:
            a[ii] = max(a[ii], b-a[ii])
    
    return "yes"
 
if __name__ ==  "__main__":
    t = int(input())
    for _ in range(t):
        n,m = list(map(int, input().split()))
        a = list(map(int, input().split()))
        b = int(input())
        print(codeforces(n,1,a,b))
