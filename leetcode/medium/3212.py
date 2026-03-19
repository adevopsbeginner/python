"""
3212. Count Submatrices With Equal Frequency of X and Y
Solved
Medium
Topics
premium lock icon
Companies
Hint
Given a 2D character matrix grid, where grid[i][j] is either 'X', 'Y', or '.', return the number of submatrices that contain:

grid[0][0]
an equal frequency of 'X' and 'Y'.
at least one 'X'.
 

Example 1:

Input: grid = [["X","Y","."],["Y",".","."]]

Output: 3

Explanation:



Example 2:

Input: grid = [["X","X"],["X","Y"]]

Output: 0

Explanation:

No submatrix has an equal frequency of 'X' and 'Y'.

Example 3:

Input: grid = [[".","."],[".","."]]

Output: 0

Explanation:

No submatrix has at least one 'X'.

 

Constraints:

1 <= grid.length, grid[i].length <= 1000
grid[i][j] is either 'X', 'Y', or '.'.
"""

import string
import heapq
from typing import List
from collections import defaultdict

class Solution:
    def leetcode(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        countx = [[0 for _ in range(n)] for _ in range(m)]
        county = [[0 for _ in range(n)] for _ in range(m)]

        if grid[0][0] == "X":
            countx[0][0] = 1
        elif grid[0][0] == "Y":
            county[0][0] = 1

        for ii in range(1,n):
            countx[0][ii] = countx[0][ii-1]
            county[0][ii] = county[0][ii-1]
            if grid[0][ii] == "X":
                countx[0][ii] += 1
            elif grid[0][ii] == "Y":
                county[0][ii] += 1

        for ii in range(1,m):
            countx[ii][0] = countx[ii-1][0]
            county[ii][0] = county[ii-1][0]
            if grid[ii][0] == "X":
                countx[ii][0] += 1
            elif grid[ii][0] == "Y":
                county[ii][0] += 1

        for rr in range(1,m):
            for cc in range(1,n):
                countx[rr][cc] = countx[rr-1][cc] + (countx[rr][cc-1]-countx[rr-1][cc-1])
                county[rr][cc] = county[rr-1][cc] + (county[rr][cc-1]-county[rr-1][cc-1])
                if grid[rr][cc] == "X":
                    countx[rr][cc] += 1
                elif grid[rr][cc] == "Y":
                    county[rr][cc] += 1                    

        #print(countx)
        #print(county)
        result = 0
        for rr in range(m):
            for cc in range(n):
                if countx[rr][cc] == 0:
                    continue
                if countx[rr][cc] == county[rr][cc]:
                    result += 1

        return result
