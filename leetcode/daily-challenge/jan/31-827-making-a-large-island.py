"""
827. Making A Large Island
Solved
Hard
Topics
Companies
You are given an n x n binary matrix grid. You are allowed to change at most one 0 to be 1.

Return the size of the largest island in grid after applying this operation.

An island is a 4-directionally connected group of 1s.

 

Example 1:

Input: grid = [[1,0],[0,1]]
Output: 3
Explanation: Change one 0 to 1 and connect two 1s, then we get an island with area = 3.
Example 2:

Input: grid = [[1,1],[1,0]]
Output: 4
Explanation: Change the 0 to 1 and make the island bigger, only one island with area = 4.
Example 3:

Input: grid = [[1,1],[1,1]]
Output: 4
Explanation: Can't change any 0 to 1, only one island with area = 4.
 

Constraints:

n == grid.length
n == grid[i].length
1 <= n <= 500
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
        def dfs(r: int, c: int, island: List[List[int]]) -> int:
            matrix[r][c] = islandno
            if r > 0:
                if grid[r-1][c] > 0 and matrix[r-1][c] == 0:
                    island.append([r-1, c])
                    dfs(r-1, c, island)
            if r < ll-1:
                if grid[r+1][c] > 0 and matrix[r+1][c] == 0:
                    island.append([r+1, c])
                    dfs(r+1, c, island)
            if c > 0:
                if grid[r][c-1] > 0 and matrix[r][c-1] == 0:
                    island.append([r, c-1])
                    dfs(r, c-1, island)
            if c < ll-1:
                if grid[r][c+1] > 0 and matrix[r][c+1] == 0:
                    island.append([r, c+1])
                    dfs(r, c+1, island)

            return len(island)

        ll = len(grid)
        matrix = [[0 for _ in range(ll)] for _ in range(ll)]
        islands = []
        islandno = 0
        result = 0
        for rr in range(ll):
            for cc in range(ll):
                if grid[rr][cc] == 0:
                    continue
                if matrix[rr][cc] > 0:
                    continue
                
                ### another new island
                island = [[rr, cc]]
                islandno += 1
                result = max(result, dfs(rr, cc, island))
                islands.append(island)
        
        for rr in range(ll):
            for cc in range(ll):
                if grid[rr][cc] == 1:
                    continue
                newisland = 1
                connected_island = []
                if rr > 0:
                    if grid[rr-1][cc] == 1:
                        if matrix[rr-1][cc] not in connected_island:
                            connected_island.append(matrix[rr-1][cc])
                if rr < ll-1:
                    if grid[rr+1][cc] == 1:
                        if matrix[rr+1][cc] not in connected_island:
                            connected_island.append(matrix[rr+1][cc])
                if cc > 0:
                    if grid[rr][cc-1] == 1:
                        if matrix[rr][cc-1] not in connected_island:
                            connected_island.append(matrix[rr][cc-1])
                if cc < ll-1:
                    if grid[rr][cc+1] == 1:
                        if matrix[rr][cc+1] not in connected_island:
                            connected_island.append(matrix[rr][cc+1])
                #print(connected_island, islands)
                for each in connected_island:
                    newisland += len(islands[each-1])
                result = max(result, newisland)
        return result


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
