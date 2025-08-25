"""
840. Magic Squares In Grid
Medium
Topics
Companies
A 3 x 3 magic square is a 3 x 3 grid filled with distinct numbers from 1 to 9 such that each row, column, and both diagonals all have the same sum.

Given a row x col grid of integers, how many 3 x 3 contiguous magic square subgrids are there?

Note: while a magic square can only contain numbers from 1 to 9, grid may contain numbers up to 15.



Example 1:


Input: grid = [[4,3,8,4],[9,5,1,9],[2,7,6,2]]
Output: 1
Explanation:
The following subgrid is a 3 x 3 magic square:

while this one is not:

In total, there is only one magic square inside the given grid.
Example 2:

Input: grid = [[8]]
Output: 0


Constraints:

row == grid.length
col == grid[i].length
1 <= row, col <= 10
0 <= grid[i][j] <= 15
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
        row = len(grid)
        col = len(grid[0])

        result = 0
        if min(row,col) < 3:
            return result
        for r in range(1,row-1):
            for c in range(1,col-1):
                if grid[r][c] != 5:
                    continue
                ten = grid[r-1][c-1:c+2] + grid[r][c-1:c+2] + grid[r+1][c-1:c+2]
                #print(ten)
                flag = 0
                for ii in range(1,10):
                    if ii not in ten:
                        flag = 1
                        break
                if flag:
                    continue

                if grid[r-1][c-1] + grid[r-1][c] + grid[r-1][c+1] != 15:
                    continue
                if grid[r][c-1] + grid[r][c] + grid[r][c+1] != 15:
                    continue
                if grid[r+1][c-1] + grid[r+1][c] + grid[r+1][c+1] != 15:
                    continue
                if grid[r-1][c-1] + grid[r][c-1] + grid[r+1][c-1] != 15:
                    continue
                if grid[r-1][c] + grid[r][c] + grid[r+1][c] != 15:
                    continue
                if grid[r-1][c+1] + grid[r][c+1] + grid[r+1][c+1] != 15:
                    continue
                if grid[r-1][c-1] + grid[r][c] + grid[r+1][c+1] != 15:
                    continue
                if grid[r-1][c+1] + grid[r][c] + grid[r+1][c-1] != 15:
                    continue
                result += 1
        return result


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
