# -*- coding: utf-8 -*-

"""
A. FizzBuzz Remixed
time limit per test1 second
memory limit per test512 megabytes
FizzBuzz is one of the most well-known problems from coding interviews. In this problem, we will consider a remixed version of FizzBuzz:

Given an integer n
, process all integers from 0
 to n
. For every integer such that its remainders modulo 3
 and modulo 5
 are the same (so, for every integer i
 such that imod3=imod5
), print FizzBuzz.

However, you don't have to solve it. Instead, given the integer n
, you have to report how many times the correct solution to that problem will print FizzBuzz.
"""

import string
import heapq
from typing import List
from collections import defaultdict
import sys

def codeforces(n: int):
    result = 0
    n15 = n//15
    n %= 15
    
    ## 0, 1, 2
    result = n15*3
    result += min(n,2)+1
    
    return result
 
if __name__ ==  "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        print(codeforces(n))
