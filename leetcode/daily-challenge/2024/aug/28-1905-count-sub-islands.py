"""
1905. Count Sub Islands
Medium
Topics
Companies
Hint
You are given two m x n binary matrices grid1 and grid2 containing only 0's (representing water) and 1's (representing land). An island is a group of 1's connected 4-directionally (horizontal or vertical). Any cells outside of the grid are considered water cells.

An island in grid2 is considered a sub-island if there is an island in grid1 that contains all the cells that make up this island in grid2.

Return the number of islands in grid2 that are considered sub-islands.



Example 1:


Input: grid1 = [[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]], grid2 = [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]
Output: 3
Explanation: In the picture above, the grid on the left is grid1 and the grid on the right is grid2.
The 1s colored red in grid2 are those considered to be part of a sub-island. There are three sub-islands.
Example 2:


Input: grid1 = [[1,0,1,0,1],[1,1,1,1,1],[0,0,0,0,0],[1,1,1,1,1],[1,0,1,0,1]], grid2 = [[0,0,0,0,0],[1,1,1,1,1],[0,1,0,1,0],[0,1,0,1,0],[1,0,0,0,1]]
Output: 2
Explanation: In the picture above, the grid on the left is grid1 and the grid on the right is grid2.
The 1s colored red in grid2 are those considered to be part of a sub-island. There are two sub-islands.


Constraints:

m == grid1.length == grid2.length
n == grid1[i].length == grid2[i].length
1 <= m, n <= 500
grid1[i][j] and grid2[i][j] are either 0 or 1.
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
    def leetcode(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        def bfs(mm: int, nn: int):
            grid2[mm][nn] = island
            if mm > 0:
                if grid2[mm-1][nn] == 1:
                    bfs(mm-1,nn)
            if mm < m-1:
                if grid2[mm+1][nn] == 1:
                    bfs(mm+1,nn)
            if nn > 0:
                if grid2[mm][nn-1] == 1:
                    bfs(mm,nn-1)
            if nn < n-1:
                if grid2[mm][nn+1] == 1:
                    bfs(mm,nn+1)

        m = len(grid1)
        n = len(grid1[0])
        island = 10
        matrix = [[0 for _ in range(n)] for _ in range(m)]
        for mm in range(m):
            for nn in range(n):
                if grid2[mm][nn] == 0:
                    continue
                if matrix[mm][nn] == 1:
                    continue
                if grid2[mm][nn] == 1:
                    bfs(mm,nn)
                    island += 1
        lisland = [1]*island
        for ii in range(10):
            lisland[ii] = 0
        for mm in range(m):
            for nn in range(n):
                if grid2[mm][nn] == 0:
                    continue
                if grid1[mm][nn] == 0:
                    lisland[grid2[mm][nn]] = 0

        return sum(lisland)


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
