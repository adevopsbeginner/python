"""
2257. Count Unguarded Cells in the Grid
Solved
Medium
Topics
Companies
Hint
You are given two integers m and n representing a 0-indexed m x n grid. You are also given two 2D integer arrays guards and walls where guards[i] = [rowi, coli] and walls[j] = [rowj, colj] represent the positions of the ith guard and jth wall respectively.

A guard can see every cell in the four cardinal directions (north, east, south, or west) starting from their position unless obstructed by a wall or another guard. A cell is guarded if there is at least one guard that can see it.

Return the number of unoccupied cells that are not guarded.

 

Example 1:


Input: m = 4, n = 6, guards = [[0,0],[1,1],[2,3]], walls = [[0,1],[2,2],[1,4]]
Output: 7
Explanation: The guarded and unguarded cells are shown in red and green respectively in the above diagram.
There are a total of 7 unguarded cells, so we return 7.
Example 2:


Input: m = 3, n = 3, guards = [[1,1]], walls = [[0,1],[1,0],[2,1],[1,2]]
Output: 4
Explanation: The unguarded cells are shown in green in the above diagram.
There are a total of 4 unguarded cells, so we return 4.
 

Constraints:

1 <= m, n <= 105
2 <= m * n <= 105
1 <= guards.length, walls.length <= 5 * 104
2 <= guards.length + walls.length <= m * n
guards[i].length == walls[j].length == 2
0 <= rowi, rowj < m
0 <= coli, colj < n
All the positions in guards and walls are unique.
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
    def leetcode(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        matrix = [[0 for _ in range(n)] for _ in range(m)]
        for r,c in guards:
            matrix[r][c] = 2
        for r,c in walls:
            matrix[r][c] = 3
        for r,c in guards:
            if r > 0:
                index = r-1
                while index >= 0 and matrix[index][c] <= 0:
                    matrix[index][c] = -1
                    index -= 1
            if r < m-1:
                index = r+1
                while index < m and matrix[index][c] <= 0:
                    matrix[index][c] = -1
                    index += 1
            if c > 0:
                index = c-1
                while index >= 0 and matrix[r][index] <= 0:
                    matrix[r][index] = -1
                    index -= 1
            if c < n-1:
                index = c+1
                while index < n and matrix[r][index] <= 0:
                    matrix[r][index] = -1
                    index += 1
        result = 0
        print(matrix)
        for r in range(m):
            for c in range(n):
                if matrix[r][c] == 0:
                    result += 1

        return result


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
