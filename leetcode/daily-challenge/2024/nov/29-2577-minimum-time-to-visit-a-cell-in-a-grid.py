"""
2577. Minimum Time to Visit a Cell In a Grid
Solved
Hard
Topics
Companies
Hint
You are given a m x n matrix grid consisting of non-negative integers where grid[row][col] represents the minimum time required to be able to visit the cell (row, col), which means you can visit the cell (row, col) only when the time you visit it is greater than or equal to grid[row][col].

You are standing in the top-left cell of the matrix in the 0th second, and you must move to any adjacent cell in the four directions: up, down, left, and right. Each move you make takes 1 second.

Return the minimum time required in which you can visit the bottom-right cell of the matrix. If you cannot visit the bottom-right cell, then return -1.

 

Example 1:



Input: grid = [[0,1,3,2],[5,1,2,5],[4,3,8,6]]
Output: 7
Explanation: One of the paths that we can take is the following:
- at t = 0, we are on the cell (0,0).
- at t = 1, we move to the cell (0,1). It is possible because grid[0][1] <= 1.
- at t = 2, we move to the cell (1,1). It is possible because grid[1][1] <= 2.
- at t = 3, we move to the cell (1,2). It is possible because grid[1][2] <= 3.
- at t = 4, we move to the cell (1,1). It is possible because grid[1][1] <= 4.
- at t = 5, we move to the cell (1,2). It is possible because grid[1][2] <= 5.
- at t = 6, we move to the cell (1,3). It is possible because grid[1][3] <= 6.
- at t = 7, we move to the cell (2,3). It is possible because grid[2][3] <= 7.
The final time is 7. It can be shown that it is the minimum time possible.
Example 2:



Input: grid = [[0,2,4],[3,2,1],[1,0,4]]
Output: -1
Explanation: There is no path from the top left to the bottom-right cell.
 

Constraints:

m == grid.length
n == grid[i].length
2 <= m, n <= 1000
4 <= m * n <= 105
0 <= grid[i][j] <= 105
grid[0][0] == 0
 
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
        m, n = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        # Early exit if the grid start or end is impossible to access
        if grid[0][1] > 1 and grid[1][0] > 1:
            return -1
        
        # Priority queue for BFS with minimum time
        pq = [(0, 0, 0)]  # (time, row, col)
        visited = set()
        
        while pq:
            time, row, col = heappop(pq)
            
            if (row, col) in visited:
                continue
            visited.add((row, col))
            
            # If we've reached the bottom-right corner
            if row == m - 1 and col == n - 1:
                return time
            
            for dr, dc in directions:
                next_row, next_col = row + dr, col + dc
                if 0 <= next_row < m and 0 <= next_col < n:
                    wait_time = max(grid[next_row][next_col] - (time + 1), 0)
                    # Adjust to even parity if necessary
                    if (wait_time % 2) != 0:
                        wait_time += 1
                    next_time = time + 1 + wait_time
                    
                    if (next_row, next_col) not in visited:
                        heappush(pq, (next_time, next_row, next_col))
        
        return -1  # If no path exists


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
