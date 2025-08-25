# -*- coding: utf-8 -*-

"""
F. Bitwise Slides
time limit per test2 seconds
memory limit per test256 megabytes

You are given an array a1,a2,…,an
. Also, you are given three variables P,Q,R
, initially equal to zero.

You need to process all the numbers a1,a2,…,an
, in the order from 1
 to n
. When processing the next ai
, you must perform exactly one of the three actions of your choice:

P:=P⊕ai
Q:=Q⊕ai
R:=R⊕ai
⊕
 denotes the bitwise XOR operation.

When performing actions, you must follow the main rule: it is necessary that after each action, all three numbers P,Q,R
 are not pairwise distinct.

There are a total of 3n
 ways to perform all n
 actions. How many of them do not violate the main rule? Since the answer can be quite large, find it modulo 109+7
.

Input
Each test contains multiple test cases. The first line contains the number of test cases t
 (1≤t≤104
). The description of the test cases follows.

The first line of each test case contains an integer n
 (1≤n≤2⋅105
) — the length of the array a
.

The second line of each test case contains n
 integers a1,a2,…,an
 (1≤ai≤109
) — the elements of the array a
.

It is guaranteed that the sum of the values of n
 for all test cases does not exceed 2⋅105
.

Output
For each test case, output the number of ways to perform all n
 actions without violating the main rule, modulo 109+7
.

Example
InputCopy
5
3
1 7 9
4
179 1 1 179
5
1 2 3 3 2
12
8 2 5 3 9 1 8 12 9 9 9 4
1
1000000000
OutputCopy
3
9
39
123
3
Note
In the first test case, there are 3 valid sequences of operations: PPP, QQQ, RRR.

In the second test case, there are 9 valid sequences of operations: PPPP, PPPQ, PPPR, QQQP, QQQQ, QQQR, RRRP, RRRQ, RRRR.
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
