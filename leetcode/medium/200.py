"""
200. Number of Islands
Medium
Topics
premium lock icon
Companies
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.
"""

import string
import heapq
from typing import List
from collections import defaultdict

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def leetcode(self, grid: List[List[str]]) -> int:
        def dfs(rr, cc):
            #print(grid)
            if rr > 0:
                if grid[rr-1][cc] == "1":
                    grid[rr-1][cc] = str(result)
                    dfs(rr-1, cc)

            if rr < m-1:
                if grid[rr+1][cc] == "1":
                    grid[rr+1][cc] = str(result)
                    dfs(rr+1, cc)

            if cc > 0:
                if grid[rr][cc-1] == "1":
                    grid[rr][cc-1] = str(result)
                    dfs(rr, cc-1)

            if cc < n-1:
                if grid[rr][cc+1] == "1":
                    grid[rr][cc+1] = str(result)
                    dfs(rr, cc+1)

        result = 1000
        m = len(grid)
        n = len(grid[0])
        for rr in range(m):
            for cc in range(n):
                if grid[rr][cc] == "1":
                    result += 1
                    grid[rr][cc] = str(result)
                    dfs(rr, cc)

        return result-1000


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
