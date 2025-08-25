"""
892. Surface Area of 3D Shapes
Easy
Topics
Companies
You are given an n x n grid where you have placed some 1 x 1 x 1 cubes. Each value v = grid[i][j] represents a tower of v cubes placed on top of cell (i, j).

After placing these cubes, you have decided to glue any directly adjacent cubes to each other, forming several irregular 3D shapes.

Return the total surface area of the resulting shapes.

Note: The bottom face of each shape counts toward its surface area.



Example 1:


Input: grid = [[1,2],[3,4]]
Output: 34
Example 2:


Input: grid = [[1,1,1],[1,0,1],[1,1,1]]
Output: 32
Example 3:


Input: grid = [[2,2,2],[2,1,2],[2,2,2]]
Output: 46


Constraints:

n == grid.length == grid[i].length
1 <= n <= 50
0 <= grid[i][j] <= 50
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
    def leetcode(self, grid: List[List[int]]) -> int:
        n = len(grid)
        result = 0
        for ii in range(n):
            for jj in range(n):
                if grid[ii][jj]:
                    result += 2
                    if ii == 0:
                        result += grid[ii][jj]
                    elif grid[ii][jj] > grid[ii-1][jj]:
                        result += grid[ii][jj] - grid[ii-1][jj]

                    if ii == n-1:
                        result += grid[ii][jj]
                    elif grid[ii][jj] > grid[ii+1][jj]:
                        result += grid[ii][jj] - grid[ii+1][jj]

                    if jj == 0:
                        result += grid[ii][jj]
                    elif grid[ii][jj] > grid[ii][jj-1]:
                        result += grid[ii][jj] - grid[ii][jj-1]

                    if jj == n-1:
                        result += grid[ii][jj]
                    elif grid[ii][jj] > grid[ii][jj+1]:
                        result += grid[ii][jj] - grid[ii][jj+1]

        return result


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
