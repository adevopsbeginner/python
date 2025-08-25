# -*- coding: utf-8 -*-

"""
C. Limited Repainting
time limit per test2 seconds
memory limit per test512 megabytes
You are given a strip, consisting of n
 cells, all cells are initially colored red.

In one operation, you can choose a segment of consecutive cells and paint them blue. Before painting, the chosen cells can be either red or blue. Note that it is not possible to paint them red. You are allowed to perform at most k
 operations (possibly zero).

For each cell, the desired color after all operations is specified: red or blue.

It is clear that it is not always possible to satisfy all requirements within k
 operations. Therefore, for each cell, a penalty is also specified, which is applied if the cell ends up the wrong color after all operations. For the i
-th cell, the penalty is equal to ai
.

The penalty of the final painting is calculated as the maximum penalty among all cells that are painted the wrong color. If there are no such cells, the painting penalty is equal to 0
.

What is the minimum penalty of the final painting that can be achieved?
"""

import string
import heapq
from typing import List
from collections import defaultdict
import sys

def codeforces(n: int):

 
if __name__ ==  "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        print(codeforces(n))

if __name__ ==  "__main__":
    t = int(input())
    for _ in range(t):
        n,m = list(map(int, input().split()))
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        print(codeforces(n,1,a,b))
