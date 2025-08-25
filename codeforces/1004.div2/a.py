# -*- coding: utf-8 -*-

"""
A. Adjacent Digit Sums
time limit per test1 second
memory limit per test256 megabytes
Given two numbers x,y
. You need to determine if there exists an integer n
 such that S(n)=x
, S(n+1)=y
.

Here, S(a)
 denotes the sum of the digits of the number a
 in the decimal numeral system.

Input
Each test contains multiple test cases. The first line contains the number of test cases t
 (1≤t≤500
). The description of the test cases follows.

The first line of each test case contains two integers x,y
 (1≤x≤1000,1≤y≤1000
).

Output
For each test case, print "NO" if a suitable n
 does not exist. Otherwise, output "YES".

You can output each letter in any case (for example, "YES", "Yes", "yes", "yEs", "yEs" will be recognized as a positive answer).

Example
InputCopy
7
1 2
77 77
997 999
999 1
1000 1
1 11
18 1
OutputCopy
Yes
No
No
Yes
No
No
Yes
Note
In the first test case, for example, n=100
 works. S(100)=1
, S(101)=2
.

In the second test case, it can be shown that S(n)≠S(n+1)
 for all n
; therefore, the answer is No.

In the fourth test case, n=10111−1
 works, which is a number consisting of 111
 digits of 9
.
"""

import string
import heapq
from typing import List
from collections import defaultdict
import sys


def codeforces(x: int, y: int):
    result = "no"
    if (x-y+1) >= 0 and (x-y+1)%9 == 0:
        result = "yes"

    return result
    
if __name__ ==  "__main__":
    t = int(input())
    for _ in range(t):
        x,y = list(map(int, input().split()))
        print(codeforces(x,y))
