# -*- coding: utf-8 -*-

"""
C. Remove the Ends
time limit per test3 seconds
memory limit per test256 megabytes
You have an array a
 of length n
 consisting of non-zero integers. Initially, you have 0
 coins, and you will do the following until a
 is empty:

Let m
 be the current size of a
. Select an integer i
 where 1≤i≤m
, gain |ai|
∗
 coins, and then:
if ai<0
, then replace a
 with [a1,a2,…,ai−1]
 (that is, delete the suffix beginning with ai
);
otherwise, replace a
 with [ai+1,ai+2,…,am]
 (that is, delete the prefix ending with ai
).
Find the maximum number of coins you can have at the end of the process.

∗
Here |ai|
 represents the absolute value of ai
: it equals ai
 when ai>0
 and −ai
 when ai<0
.

Input
The first line contains an integer t
 (1≤t≤104
) — the number of testcases.

The first line of each testcase contains an integer n
 (1≤n≤2⋅105
) — the length of a
.

The second line of each testcase contains n
 integers a1,a2,…,an
 (−109≤ai≤109
, ai≠0
).

The sum of n
 across all testcases does not exceed 2⋅105
.

Output
For each test case, output the maximum number of coins you can have at the end of the process.
"""

import string
import heapq
from typing import List
from collections import defaultdict
import sys

def codeforces(n: int, arr: list):
    """
    recursive function
    """
    ll = len(arr)
    
    ### edge condition 0
    if ll == 0:
        return 0

    ### edge condition 1
    if ll == 1:
        return abs(arr[0])
        
    result = 0
    left, right = 0, 0
    
    ### all left positive numbers are ok to be added
    for ii in range(ll):
        if arr[ii] > 0:
            result += arr[ii]
        else:
            ### the firt positive number
            left = ii
            break
        
        ### if we are lucky, the recursive is finished here
        if ii == ll-1:
            return sum(arr)
        
    ### all right side numbers numbers are ok to be added
    for ii in range(ll-1, -1, -1):
        if arr[ii] < 0:
            result += -arr[ii]
        else:
            ### the firt positive number
            right = ii
            break
        
        ### if we are lucky, the recursive is finished here
        if ii == 0:
            return 0-sum(arr)
    
    ### for left side of the unlucky part
    left_negative = 0
    left1 = 0
    for ii in range(left, ll):
        if arr[ii] < 0:
            left_negative += arr[ii]
        else:
            left1 = ii
            break
        
    ### for right side of the unlucky part
    right_positive = 0
    right1 = 0
    for ii in range(right, -1, -1):
        if arr[ii] > 0:
            right_positive += arr[ii]
        else:
            right1 = ii
            break
        
    maxlr = max(left_negative, codeforces(right-left+1, arr[left: right+1]))
    
    result += codeforces(right-left+1, arr[left: right+1])
    return 

if __name__ ==  "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        print(codeforces(n,arr))


