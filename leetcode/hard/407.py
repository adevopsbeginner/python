"""
407. Trapping Rain Water II
Solved
Hard
Topics
premium lock icon
Companies
Given an m x n integer matrix heightMap representing the height of each unit cell in a 2D elevation map, return the volume of water it can trap after raining.

 

Example 1:


Input: heightMap = [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]
Output: 4
Explanation: After the rain, water is trapped between the blocks.
We have two small ponds 1 and 3 units trapped.
The total volume of water trapped is 4.
Example 2:


Input: heightMap = [[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]]
Output: 10
 

Constraints:

m == heightMap.length
n == heightMap[i].length
1 <= m, n <= 200
0 <= heightMap[i][j] <= 2 * 104
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
    def leetcode(self, heightMap: List[List[int]]) -> int:
        m = len(heightMap)
        n = len(heightMap[0])

        result = 0
        visited = [[0]*n for _ in range(m)]
        boundary = []

        ### initial boundaries
        for ii in range(m):
            visited[ii][0] = 1
            heapq.heappush(boundary, (heightMap[ii][0], ii, 0))
            visited[ii][n-1] = 1
            heapq.heappush(boundary, (heightMap[ii][n-1], ii, n-1))

        for ii in range(n):
            visited[0][ii] = 1
            heapq.heappush(boundary, (heightMap[0][ii], 0, ii))
            visited[m-1][ii] = 1
            heapq.heappush(boundary, (heightMap[m-1][ii], m-1, ii))

        while boundary:
            h,r,c = heapq.heappop(boundary)
            
            if r > 0:
                if visited[r-1][c] == 0:
                    visited[r-1][c] = 1
                    if heightMap[r-1][c] < h:
                        result += h-heightMap[r-1][c]
                        heapq.heappush(boundary, (h, r-1, c))
                    else:
                        heapq.heappush(boundary, (heightMap[r-1][c], r-1, c))

            if r < m-1:
                if visited[r+1][c] == 0:
                    visited[r+1][c] = 1
                    if heightMap[r+1][c] < h:
                        result += h-heightMap[r+1][c]
                        heapq.heappush(boundary, (h, r+1, c))
                    else:
                        heapq.heappush(boundary, (heightMap[r+1][c], r+1, c))

            if c > 0:
                if visited[r][c-1] == 0:
                    visited[r][c-1] = 1
                    if heightMap[r][c-1] < h:
                        result += h-heightMap[r][c-1]
                        heapq.heappush(boundary, (h, r, c-1))
                    else:
                        heapq.heappush(boundary, (heightMap[r][c-1], r, c-1))

            if c < n-1:
                if visited[r][c+1] == 0:
                    visited[r][c+1] = 1
                    if heightMap[r][c+1] < h:
                        result += h - heightMap[r][c+1]
                        heapq.heappush(boundary, (h, r, c+1))
                    else:
                        heapq.heappush(boundary, (heightMap[r][c+1], r, c+1))


        return result

        ### chatgpt
        if not heightMap or not heightMap[0]:
            return 0

        m, n = len(heightMap), len(heightMap[0])
        visited = [[False] * n for _ in range(m)]
        heap = []

        # Push all boundary cells into heap
        for i in range(m):
            for j in range(n):
                if i == 0 or i == m-1 or j == 0 or j == n-1:
                    heapq.heappush(heap, (heightMap[i][j], i, j))
                    visited[i][j] = True

        trapped_water = 0
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        while heap:
            height, x, y = heapq.heappop(heap)

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                    visited[nx][ny] = True
                    trapped_water += max(0, height - heightMap[nx][ny])
                    heapq.heappush(heap, (max(heightMap[nx][ny], height), nx, ny))

        return trapped_water


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
