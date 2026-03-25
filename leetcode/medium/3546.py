"""
3546. Equal Sum Grid Partition I
Medium
Topics
premium lock icon
Companies
Hint
You are given an m x n matrix grid of positive integers. Your task is to determine if it is possible to make either one horizontal or one vertical cut on the grid such that:

Each of the two resulting sections formed by the cut is non-empty.
The sum of the elements in both sections is equal.
Return true if such a partition exists; otherwise return false.

 

Example 1:

Input: grid = [[1,4],[2,3]]

Output: true

Explanation:



A horizontal cut between row 0 and row 1 results in two non-empty sections, each with a sum of 5. Thus, the answer is true.

Example 2:

Input: grid = [[1,3],[2,4]]

Output: false

Explanation:

No horizontal or vertical cut results in two non-empty sections with equal sums. Thus, the answer is false.

 

Constraints:

1 <= m == grid.length <= 105
1 <= n == grid[i].length <= 105
2 <= m * n <= 105
1 <= grid[i][j] <= 105
"""

import string
import heapq
from typing import List
from collections import defaultdict

class Solution:
    def leetcode(self, grid: List[List[int]]) -> bool:
        m = len(grid)
        n = len(grid[0])
        row = [0 for _ in range(m)]
        col = [0 for _ in range(n)]
        for rr in range(m):
            for cc in range(n):
                row[rr] += grid[rr][cc]
                col[cc] += grid[rr][cc]
        total = sum(row)
        half = 0
        for rr in range(m):
            half += row[rr]
            if half*2 == total:
                return True
        
        half = 0
        for cc in range(n):
            half += col[cc]
            if half*2 == total:
                return True

        return False
