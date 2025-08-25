"""
994. Rotting Oranges
Solved
Medium
Topics
premium lock icon
Companies
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

 

Example 1:


Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
Example 2:

Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
Example 3:

Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 10
grid[i][j] is 0, 1, or 2.
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
        lr = len(grid)
        if lr == 0:
            return 0
        lc = len(grid[0])
        if lc == 0:
            return 0

        l2 = []
        ans = 0
        
        for r in range(lr):
            for c in range(lc):
                if grid[r][c] == 2:
                    l2.append([r,c])
        l2.append([lr,lc])
                    
        while len(l2):
            x,y = l2.pop(0)
            if x == lr and y == lc:
                ans += 1
                if len(l2):
                    l2.append([lr,lc])
                continue
            if x > 0 and grid[x-1][y] == 1:
                l2.append([x-1,y])
                grid[x-1][y] = 2
            if x < lr-1 and grid[x+1][y] == 1:
                l2.append([x+1,y])
                grid[x+1][y] = 2
            if y < lc-1 and grid[x][y+1] == 1:
                l2.append([x,y+1])
                grid[x][y+1] = 2
            if y > 0 and grid[x][y-1] == 1:
                l2.append([x,y-1])
                grid[x][y-1] = 2
                
        for r in range(lr):
            for c in range(lc):
                if grid[r][c] == 1:
                    return -1
        
        return ans-1


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
