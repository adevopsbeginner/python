# -*- coding: utf-8 -*-

"""
C - Grid Coloring 3 / 
Time Limit: 4 sec / Memory Limit: 1024 MB

Score : 
1000 points

Problem Statement
There is a grid of 
H rows and 
W columns. Initially, all cells are uncolored.

You can repeat the following procedure any number of times:

Choose an integer 
i between 
1 and 
C, inclusive, and choose exactly one cell in the grid.
Then, color that chosen cell, as well as all cells in the same row as the chosen cell and all cells in the same column as the chosen cell (a total of 
(H+W−1) cells), with color 
i. (If any cell is already colored, its color is overwritten with color 
i.)
Print the number, modulo 
998244353, of different grids in which every cell is colored that can be obtained by repeating the procedure above.

Constraints
1≤H,W≤400
1≤C≤10 
9
 
All input values are integers.
"""

import string
import heapq
from typing import List
from collections import defaultdict
import sys

def atcoder(n: int, arr: list):
    ll = len(arr)
    result = 0

    for ii in range(ll):
        pass

    return result


if __name__ == "__main__":
  t = int(input())
  for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(atcoder(n,arr))
