# -*- coding: utf-8 -*-

"""
B. Variety is Discouraged
time limit per test1.5 seconds
memory limit per test256 megabytes
Define the score of an arbitrary array b
 to be the length of b
 minus the number of distinct elements in b
. For example:

The score of [1,2,2,4]
 is 1
, as it has length 4
 and only 3
 distinct elements (1
, 2
, 4
).
The score of [1,1,1]
 is 2
, as it has length 3
 and only 1
 distinct element (1
).
The empty array has a score of 0
.
You have an array a
. You need to remove some non-empty contiguous subarray from a
 at most once.

More formally, you can do the following at most once:

pick two integers l
, r
 where 1≤l≤r≤n
, and
delete the contiguous subarray [al,…,ar]
 from a
 (that is, replace a
 with [a1,…,al−1,ar+1,…,an]
).
Output an operation such that the score of a
 is maximum; if there are multiple answers, output one that minimises the final length of a
 after the operation. If there are still multiple answers, you may output any of them.

Input
The first line contains an integer t
 (1≤t≤104
) — the number of testcases.

The first line of each testcase contains an integer n
 (1≤n≤2⋅105
) — the length of the array a
.

The second line of each testcase contains n
 integers a1,a2,…,an
 (1≤ai≤n
).

The sum of n
 across all testcases does not exceed 2⋅105
.

Output
For each testcase, if you wish to not make a move, output 0
.

Otherwise, output two integers l
 and r
 (1≤l≤r≤n
), representing the left and right bound of the removed subarray.

The removed subarray should be chosen such that the score is maximized, and over all such answers choose any of them that minimises the final length of the array.
"""

import string
import heapq
from typing import List
from collections import defaultdict
import sys
from collections import defaultdict

def codeforces(n: int, arr: list):
    ll = len(arr)
    if ll == 0:
        return "0"
    if ll == 1:
        return "1 1"
    dd = defaultdict(int)
    for each in arr:
        dd[each] += 1
    if dd[arr[0]] == ll:
        return "0"

    l,r = 0, -1
    left = 0
    count = 0
    for ii in range(ll):
        if dd[arr[ii]] > 1:
            if count > r-l+1:
                l = left
                r = ii-1
            count = 0
            continue
        else:
            if count == 0:
                left = ii
            count += 1

        if ii == ll-1:
            if count > r-l+1:
                l = left
                r = ii-1
            count = 0
    if r < 0:
        return "0"
    return str(l+1) + " " + str(r+1)


if __name__ ==  "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        print(codeforces(n,arr))
