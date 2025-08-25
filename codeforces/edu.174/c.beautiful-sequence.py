# -*- coding: utf-8 -*-

"""
C. Beautiful Sequence
time limit per test2 seconds
memory limit per test256 megabytes
Let's call an integer sequence beautiful if the following conditions hold:

its length is at least 3
;
for every element except the first one, there is an element to the left less than it;
for every element except the last one, there is an element to the right larger than it;
For example, [1,4,2,4,7]
 and [1,2,4,8]
 are beautiful, but [1,2]
, [2,2,4]
, and [1,3,5,3]
 are not.

Recall that a subsequence is a sequence that can be obtained from another sequence by removing some elements without changing the order of the remaining elements.

You are given an integer array a
 of size n
, where every element is from 1
 to 3
. Your task is to calculate the number of beautiful subsequences of the array a
. Since the answer might be large, print it modulo 998244353
.

Input
The first line contains a single integer t
 (1≤t≤104
) — the number of test cases.

The first line of each test case contains a single integer n
 (3≤n≤2⋅105
).

The second line contains n
 integers a1,a2,…,an
 (1≤ai≤3
).

Additional constraint on the input: the sum of n
 over all test cases doesn't exceed 2⋅105
.

Output
For each test case, print a single integer — the number of beautiful subsequences of the array a
, taken modulo 998244353
.

Example
InputCopy
4
7
3 2 1 2 2 1 3
4
3 1 2 2
3
1 2 3
9
1 2 3 2 1 3 2 2 3
OutputCopy
3
0
1
22
Note
In the first test case of the example, the following subsequences are beautiful:

[a3,a4,a7]
;
[a3,a5,a7]
;
[a3,a4,a5,a7]
.
"""

import string
import heapq
from typing import List
from collections import defaultdict
import sys

def codeforces(n, arr):
    ### the first element must be 1
    while arr[0] != 1:
        arr.pop(0)
    ### the last element must be 3
    while arr[-1] != 3:
        arr.pop()
        
    ll = len(arr)
    ### total number of possible substrings
    result = 2**ll-1
    count2 = 0
    for ii in range(ll):
        if arr[ii] == 2:
            count2 += 1
    result -= 2**count2-1
    
    return result
    
if __name__ ==  "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        print(codeforces(n,arr))


def codeforces(n, arr):
    ll = len(arr)
    result = 0
    for ii in range(ll-2):
        if arr[ii] == 1:
            count2 = 0
            for jj in range(ii+1, ll):
                if arr[jj] == 2:
                    count2 += 1
                elif arr[jj] == 3:
                    result += 2**count2-1
    return result
                    
    ### wrong answer for 9 / 1 2 3 2 1 3 2 2 3
    ### the first element must be 1
    while arr[0] != 1:
        arr.pop(0)
    ### the last element must be 3
    while arr[-1] != 3:
        arr.pop()
        
    ll = len(arr)
    ### total number of possible substrings
    result = 2**ll-1
    count2 = 0
    for ii in range(ll):
        if arr[ii] == 2:
            count2 += 1
    result -= 2**count2-1
    
    return result
    
if __name__ ==  "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        print(codeforces(n,arr))