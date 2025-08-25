"""
463. Island Perimeter
Solved
Easy
Topics
Companies
You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.



Example 1:


Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
Output: 16
Explanation: The perimeter is the 16 yellow stripes in the image above.
Example 2:

Input: grid = [[1]]
Output: 4
Example 3:

Input: grid = [[1,0]]
Output: 4


Constraints:

row == grid.length
col == grid[i].length
1 <= row, col <= 100
grid[i][j] is 0 or 1.
There is exactly one island in grid.
"""

import string
from typing import List
from collections import defaultdict

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def leetcode(self, grid: List[List[int]]) -> int:
        row = len(grid)
        if row == 0:
            return 0
        col = len(grid[0])
        result = 0
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 0:
                    continue

                if r == 0:
                    result += 1
                elif grid[r-1][c] == 0:
                    result += 1

                if r == row-1:
                    result += 1
                elif grid[r+1][c] == 0:
                    result += 1

                if c == 0:
                    result += 1
                elif grid[r][c-1] == 0:
                    result += 1

                if c == col-1:
                    result += 1
                elif grid[r][c+1] == 0:
                    result += 1

        return result

if __name__ == "__main__":
    app = Solution()
    a = 5
    b = [[1,2]]
    print(app.leetcode(a,b))
