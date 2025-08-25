"""
1568. Minimum Number of Days to Disconnect Island
Hard
Topics
Companies
Hint
You are given an m x n binary grid grid where 1 represents land and 0 represents water. An island is a maximal 4-directionally (horizontal or vertical) connected group of 1's.

The grid is said to be connected if we have exactly one island, otherwise is said disconnected.

In one day, we are allowed to change any single land cell (1) into a water cell (0).

Return the minimum number of days to disconnect the grid.



Example 1:


Input: grid = [[0,1,1,0],[0,1,1,0],[0,0,0,0]]

Output: 2
Explanation: We need at least 2 days to get a disconnected grid.
Change land grid[1][1] and grid[0][2] to water and get 2 disconnected island.
Example 2:


Input: grid = [[1,1]]
Output: 2
Explanation: Grid of full water is also disconnected ([[1,1]] -> [[0,0]]), 0 islands.


Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 30
grid[i][j] is either 0 or 1.
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
        ### chatgpt
        def count_islands(grid):
            m, n = len(grid), len(grid[0])
            visited = [[False] * n for _ in range(m)]
            island_count = 0

            def bfs(x, y):
                queue = deque([(x, y)])
                directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                while queue:
                    cx, cy = queue.popleft()
                    for dx, dy in directions:
                        nx, ny = cx + dx, cy + dy
                        if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1 and not visited[nx][ny]:
                            visited[nx][ny] = True
                            queue.append((nx, ny))

            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 1 and not visited[i][j]:
                        visited[i][j] = True
                        bfs(i, j)
                        island_count += 1
            return island_count

        # Check initial number of islands
        initial_islands = count_islands(grid)
        if initial_islands != 1:
            return 0  # Already disconnected

        m, n = len(grid), len(grid[0])

        # Check if any single removal results in disconnection
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    if count_islands(grid) != 1:
                        return 1
                    grid[i][j] = 1  # Restore the cell

        # If no single cell removal works, it will take at least 2 days
        return 2


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
