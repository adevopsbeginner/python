# -*- coding: utf-8 -*-

"""
D. Eating
time limit per test5 seconds
memory limit per test512 megabytes
There are n
 slimes on a line, the i
-th of which has weight wi
. Slime i
 is able to eat another slime j
 if wi≥wj
; afterwards, slime j
 disappears and the weight of slime i
 becomes wi⊕wj
∗
.

The King of Slimes wants to run an experiment with parameter x
 as follows:

Add a new slime with weight x
 to the right end of the line (after the n
-th slime).
This new slime eats the slime to its left if it is able to, and then takes its place (moves one place to the left). It will continue to do this until there is either no slime to its left or the weight of the slime to its left is greater than its own weight. (No other slimes are eaten during this process.)
The score of this experiment is the total number of slimes eaten.
The King of Slimes is going to ask you q
 queries. In each query, you will be given an integer x
, and you need to determine the score of the experiment with parameter x
.

Note that the King does not want you to actually perform each experiment; his slimes would die, which is not ideal. He is only asking what the hypothetical score is; in other words, the queries are not persistent.

∗
Here ⊕
 denotes the bitwise XOR operation.

Input
The first line contains an integer t
 (1≤t≤104
) — the number of test cases.

The first line of each test case contains integers n
 and q
 (1≤n,q≤2⋅105
) — the number of slimes and the number of queries, respectively.

The following line contains n
 integers w1,w2,…,wn
 (1≤wi<230
) — the weights of the slimes.

The following q
 lines contain a single integer x
 (1≤x<230
) — the parameter for the experiment.

The sum of n
 does not exceed 2⋅105
 and the sum of q
 does not exceed 2⋅105
 across all test cases.

Output
For each query, output a single integer — the score of the experiment.
"""

import string
import heapq
from typing import List
from collections import defaultdict
import sys

def codeforces(n: int, s: str):
    ll = len(nums)
    result = 0

    for ii in range(ll):
        pass

    return result

if __name__ ==  "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        s = input()
        print(codeforces(n,s))

