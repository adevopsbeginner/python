# -*- coding: utf-8 -*-

"""
A. Brogramming Contest
time limit per test1 second
memory limit per test256 megabytes
One day after waking up, your friend challenged you to a brogramming contest. In a brogramming contest, you are given a binary string∗
 s
 of length n
 and an initially empty binary string t
. During a brogramming contest, you can make either of the following moves any number of times:

remove some suffix†
 from s
 and place it at the end of t
, or
remove some suffix from t
 and place it at the end of s
.
To win the brogramming contest, you must make the minimum number of moves required to make s
 contain only the character 0
 and t
 contain only the character 1
. Find the minimum number of moves required.
∗
A binary string is a string consisting of characters 0
 and 1
.

†
A string a
 is a suffix of a string b
 if a
 can be obtained from deletion of several (possibly, zero or all) elements from the beginning of b
.

Input
The first line contains an integer t
 (1≤t≤100
) — the number of test cases.

The first line of each test case is an integer n
 (1≤n≤1000
) — the length of the string s
.

The second line of each test case contains the binary string s
.

The sum of n
 across all test cases does not exceed 1000
.

Output
For each testcase, output the minimum number of moves required.
"""

import string
import heapq
from typing import List
from collections import defaultdict
import sys

def codeforces(n: int, s: str):
    s = "0"+s
    if s[-1] == "0":
        s += "1"
    else:
        s += "0"
    ll = len(s)
    flag1 = 0
    result = 0
    for ii in range(1,ll):
        if flag1 and s[ii] != s[ii-1]:
            result += 1
        if s[ii] == "1":
            flag1 = 1
    return result

if __name__ ==  "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        s = input()
        print(codeforces(n,s))