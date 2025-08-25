# -*- coding: utf-8 -*-

"""
B. Set of Strangers
time limit per test2 seconds
memory limit per test256 megabytes
You are given a table of n
 rows and m
 columns. Initially, the cell at the i
-th row and the j
-th column has color ai,j
.

Let's say that two cells are strangers if they don't share a side. Strangers are allowed to touch with corners.

Let's say that the set of cells is a set of strangers if all pairs of cells in the set are strangers. Sets with no more than one cell are sets of strangers by definition.

In one step, you can choose any set of strangers such that all cells in it have the same color and paint all of them in some other color. You can choose the resulting color.

What is the minimum number of steps you need to make the whole table the same color?

Input
The first line contains a single integer t
 (1≤t≤104
) — the number of test cases. Next, t
 cases follow.

The first line of each test case contains two integers n
 and m
 (1≤n≤m≤700
) — the number of rows and columns in the table.

The next n
 lines contain the colors of cells in the corresponding row ai,1,…,ai,m
 (1≤ai,j≤nm
).

It's guaranteed that the total sum of nm
 doesn't exceed 5⋅105
 over all test cases.

Output
For each test case, print one integer — the minimum number of steps to paint all cells of the table the same color.

Example
InputCopy
4
1 1
1
3 3
1 2 1
2 3 2
1 3 1
1 6
5 4 5 4 4 5
3 4
1 4 2 2
1 4 3 5
6 6 3 5
OutputCopy
0
2
1
10
Note
In the first test case, the table is painted in one color from the start.

In the second test case, you can, for example, choose all cells with color 1
 and paint them in 3
. Then choose all cells with color 2
 and also paint them in 3
.

In the third test case, you can choose all cells with color 5
 and paint them in color 4
.
"""

import string
import heapq
from typing import List
from collections import defaultdict
import sys

from collections import defaultdict

def codeforces(n: int, m: int, grid: []):
    dd = defaultdict(int)
    for nn in range(n):
        for mm in range(m):
            dd[grid[nn][mm]] = 1
            if nn > 0 and grid[nn][mm] == grid[nn-1][mm]:
                dd[grid[nn][mm]] = 2
            if nn < n-1 and grid[nn][mm] == grid[nn+1][mm]:
                dd[grid[nn][mm]] = 2
            if mm > 0 and grid[nn][mm] == grid[nn][mm-1]:
                dd[grid[nn][mm]] = 2
            if mm < m-1 and grid[nn][mm] == grid[nn][mm+1]:
                dd[grid[nn][mm]] = 2

    result = 0
    for each in dd:
        result += dd[each]
    
    result -= 1
    for each in dd:
        if dd[each] == 2:
            result -= 1
            break
            
    return result
        
    
if __name__ ==  "__main__":
    t = int(input())
    for _ in range(t):
        n, m = list(map(int, input().split()))
        arr = []
        for _ in range(n):
            arr.append(list(map(int, input().split())))
        print(codeforces(n, m, arr))