"""
3195. Find the Minimum Area to Cover All Ones I
Medium
Topics
premium lock icon
Companies
Hint
You are given a 2D binary array grid. Find a rectangle with horizontal and vertical sides with the smallest area, such that all the 1's in grid lie inside this rectangle.

Return the minimum possible area of the rectangle.

 

Example 1:

Input: grid = [[0,1,0],[1,0,1]]

Output: 6

Explanation:



The smallest rectangle has a height of 2 and a width of 3, so it has an area of 2 * 3 = 6.

Example 2:

Input: grid = [[1,0],[0,0]]

Output: 1

Explanation:



The smallest rectangle has both height and width 1, so its area is 1 * 1 = 1.

 

Constraints:

1 <= grid.length, grid[i].length <= 1000
grid[i][j] is either 0 or 1.
The input is generated such that there is at least one 1 in grid.
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
        m = len(grid)
        n = len(grid[0])
        summ = [0]*m
        sumn = [0]*n

        ### caculate sum of each row and column
        for rr in range(m):
            for cc in range(n):
                summ[rr] += grid[rr][cc]
                sumn[cc] += grid[rr][cc]

        if sum(summ) == 0:
            return 0

        ### get rid of empty rows and columns
        while summ[0] == 0:
            summ.pop(0)
        while summ[-1] == 0:
            summ.pop()
        while sumn[0] == 0:
            sumn.pop(0)
        while sumn[-1] == 0:
            sumn.pop()

        return len(summ)*len(sumn)


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
