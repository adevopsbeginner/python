"""
2658. Maximum Number of Fish in a Grid
Medium
Topics
Companies
Hint
You are given a 0-indexed 2D matrix grid of size m x n, where (r, c) represents:

A land cell if grid[r][c] = 0, or
A water cell containing grid[r][c] fish, if grid[r][c] > 0.
A fisher can start at any water cell (r, c) and can do the following operations any number of times:

Catch all the fish at cell (r, c), or
Move to any adjacent water cell.
Return the maximum number of fish the fisher can catch if he chooses his starting cell optimally, or 0 if no water cell exists.

An adjacent cell of the cell (r, c), is one of the cells (r, c + 1), (r, c - 1), (r + 1, c) or (r - 1, c) if it exists.

 

Example 1:


Input: grid = [[0,2,1,0],[4,0,0,3],[1,0,0,4],[0,3,2,0]]
Output: 7
Explanation: The fisher can start at cell (1,3) and collect 3 fish, then move to cell (2,3) and collect 4 fish.
Example 2:


Input: grid = [[1,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,1]]
Output: 1
Explanation: The fisher can start at cells (0,0) or (3,3) and collect a single fish. 
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 10
0 <= grid[i][j] <= 10
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
        def dfs(r: int, c: int) -> int:
            result = grid[r][c]
            visited[r*n+c] = 1

            if r > 0 and visited[(r-1)*n+(c)] == 0 and grid[r-1][c] > 0:
                result += dfs(r-1,c)
            if r < m-1 and visited[(r+1)*n+(c)] == 0 and grid[r+1][c] > 0:
                result += dfs(r+1,c)
            if c > 0 and visited[(r)*n+(c-1)] == 0 and grid[r][c-1] > 0:
                result += dfs(r,c-1)
            if c < n-1 and visited[(r)*n+(c+1)] == 0 and grid[r][c+1] > 0:
                result += dfs(r,c+1)

            return result

        m = len(grid)
        n = len(grid[0])
        visited = [0]*m*n
        result = 0
        for rr in range(m):
            for cc in range(n):
                if grid[rr][cc] == 0:
                    continue
                if visited[rr*n+cc] > 0:
                    continue
                visited[rr*n+cc] = 1
                result = max(result, dfs(rr,cc))

        return result


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
