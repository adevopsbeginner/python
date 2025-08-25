"""
1765. Map of Highest Peak
Medium
Topics
Companies
Hint
You are given an integer matrix isWater of size m x n that represents a map of land and water cells.

If isWater[i][j] == 0, cell (i, j) is a land cell.
If isWater[i][j] == 1, cell (i, j) is a water cell.
You must assign each cell a height in a way that follows these rules:

The height of each cell must be non-negative.
If the cell is a water cell, its height must be 0.
Any two adjacent cells must have an absolute height difference of at most 1. A cell is adjacent to another cell if the former is directly north, east, south, or west of the latter (i.e., their sides are touching).
Find an assignment of heights such that the maximum height in the matrix is maximized.

Return an integer matrix height of size m x n where height[i][j] is cell (i, j)'s height. If there are multiple solutions, return any of them.

 

Example 1:



Input: isWater = [[0,1],[0,0]]
Output: [[1,0],[2,1]]
Explanation: The image shows the assigned heights of each cell.
The blue cell is the water cell, and the green cells are the land cells.
Example 2:



Input: isWater = [[0,0,1],[1,0,0],[0,0,0]]
Output: [[1,1,0],[0,1,1],[1,2,2]]
Explanation: A height of 2 is the maximum possible height of any assignment.
Any height assignment that has a maximum height of 2 while still meeting the rules will also be accepted.
 

Constraints:

m == isWater.length
n == isWater[i].length
1 <= m, n <= 1000
isWater[i][j] is 0 or 1.
There is at least one water cell.
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
    def leetcode(self, isWater: List[List[int]]) -> List[List[int]]:
        def isSurrounded(r: int, c: int) -> bool:
            ### r-1,c
            if not isAssigned(r-1,c):
                return False
            ### r+1,c
            if not isAssigned(r+1,c):
                return False
            ### r,c-1
            if not isAssigned(r,c-1):
                return False
            ### r,c+1
            if not isAssigned(r,c+1):
                return False

            return True
        
        def isAssigned(r: int, c: int) -> bool:
            if r < 0 or c < 0 or r >= m or c >= n:
                return True
            if result[r][c] > 0:
                return True
            if isWater[r][c] == 1:
                return True
            return False

        def assign(r: int, c: int, h: int, count: int) -> int:
            if r < 0 or c < 0 or r >= m or c >= n:
                return count
            result[r][c] = h
            q.append([r,c,h])
            count += 1
            
            return count

        m,n = len(isWater), len(isWater[0])
        result = [[0 for _ in range(n)] for _ in range(m)]
        q = []
        count = 0
        for ii in range(m):
            for jj in range(n):
                if isWater[ii][jj] == 1:
                    q.append([ii,jj,0])
                    count += 1
        while q and count < m*n:
            r,c,h = q.pop(0)

            if isSurrounded(r,c):
                continue

            if not isAssigned(r-1,c):
                count = assign(r-1,c,h+1, count)
            if not isAssigned(r+1,c):
                count = assign(r+1,c,h+1, count)
            if not isAssigned(r,c-1):
                count = assign(r,c-1,h+1, count)
            if not isAssigned(r,c+1):
                count = assign(r,c+1,h+1, count)

        return result


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
