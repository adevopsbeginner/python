# -*- coding: utf-8 -*-

"""
B. Perfecto
time limit per test1.5 seconds
memory limit per test256 megabytes

A permutation p
 of length n
∗
 is perfect if, for each index i
 (1≤i≤n
), it satisfies the following:

The sum of the first i
 elements p1+p2+…+pi
 is not a perfect square†
.
You would like things to be perfect. Given a positive integer n
, find a perfect permutation of length n
, or print −1
 if none exists.

∗
A permutation of length n
 is an array consisting of n
 distinct integers from 1
 to n
 in arbitrary order. For example, [2,3,1,5,4]
 is a permutation, but [1,2,2]
 is not a permutation (2
 appears twice in the array), and [1,3,4]
 is also not a permutation (n=3
 but there is 4
 in the array).

†
A perfect square is an integer that is the square of an integer, e.g., 9=32
 is a perfect square, but 8
 and 14
 are not.
"""

import string
import heapq
from typing import List
from collections import defaultdict
import sys

def codeforces(n: int):
    arr = [1,8,49,288,1681,9800,57121,332928]
    result = [str(ii) for ii in range(1,n+1)]
    if n in arr:
        return -1
    else:
        for ii in range(8):
            if arr[ii] > n:
                break
            result[arr[ii]-1], result[arr[ii]] = result[arr[ii]], result[arr[ii]-1]
        
    return " ".join(result)
 
 
if __name__ ==  "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        print(codeforces(n))
