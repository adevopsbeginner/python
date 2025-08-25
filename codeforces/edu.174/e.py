# -*- coding: utf-8 -*-

"""
E. A, B, AB and BA
time limit per test2 seconds
memory limit per test256 megabytes
You are given a string s
 consisting of characters A and B.

Your task is to split it into blocks of length 1
 and 2
 in such a way that

there are no more than a
 strings equal to "A";
there are no more than b
 strings equal to "B";
there are no more than ab
 strings "AB";
there are no more than ba
 strings "BA";
Strings "AA" and "BB" are prohibited. Each character of the initial string s
 should belong to exactly one block.

Input
The first line contains one integer t
 (1≤t≤104
) — the number of test cases. Next, t
 independent cases follow.

The first line of each test case contains a single string s
 (1≤|s|≤5⋅105
) consisting only of characters A and/or B.

The second line of each test case contains four integers a
, b
, ab
, and ba
 (0≤a,b,ab,ba≤5⋅105
) — the maximum allowed number of strings "A", "B", "AB", and "BA" correspondingly.

It's guaranteed that the total length of s
 doesn't exceed 5⋅105
 over all test cases.

Output
For each test case, print YES if it's possible to split string s
. Otherwise, print NO.

Example
InputCopy
7
A
0 0 10 10
B
0 1 0 0
ABA
0 0 1 1
ABBABAAB
5 5 0 0
ABABBAABBAAB
1 1 2 3
ABBBBAB
0 3 2 0
BAABBA
1 3 2 0
OutputCopy
NO
YES
NO
YES
YES
YES
NO
Note
In the third test case, all possible splits are: A|B|A, AB|A or A|BA. All of them have at least one "A".

In the fourth test case, one of the possible splits is the following: A|B|B|A|B|A|A|B.

In the fifth test case, one of the possible splits is the following: A|BA|B|BA|AB|BA|AB
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
