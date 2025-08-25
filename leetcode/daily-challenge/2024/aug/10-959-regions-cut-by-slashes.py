"""

Code
Testcase
Test Result
Test Result
959. Regions Cut By Slashes
Medium
Topics
Companies
An n x n grid is composed of 1 x 1 squares where each 1 x 1 square consists of a '/', '\', or blank space ' '. These characters divide the square into contiguous regions.

Given the grid grid represented as a string array, return the number of regions.

Note that backslash characters are escaped, so a '\' is represented as '\\'.



Example 1:


Input: grid = [" /","/ "]
Output: 2
Example 2:


Input: grid = [" /","  "]
Output: 1
Example 3:


Input: grid = ["/\\","\\/"]
Output: 5
Explanation: Recall that because \ characters are escaped, "\\/" refers to \/, and "/\\" refers to /\.


Constraints:

n == grid.length == grid[i].length
1 <= n <= 30
grid[i][j] is either '/', '\', or ' '.
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
    def leetcode(self, grid: List[str]) -> int:
        def bfs(r: int, c: int, updown: str):
            if updown == "up":
                #1 up
                if r > 0:
                    if dn[r-1][c] == 0:
                        dn[r-1][c] = 1
                        bfs(r-1,c,"down")
                #2 down
                if matrix[r][c] == 0:
                    if dn[r][c] == 0:
                        dn[r][c] = 1
                        bfs(r, c, "down")
                if matrix[r][c] >= 0:
                    if c > 0:
                        # 3 left up
                        if matrix[r][c-1] == 1:
                            if dn[r][c-1] == 0:
                                dn[r][c-1] = 1
                                bfs(r, c-1, "down")
                        #4 left down
                        else:
                            if up[r][c-1] == 0:
                                up[r][c-1] = 1
                                bfs(r, c-1, "up")
                if matrix[r][c] <= 0:
                    if c < n-1:
                        # 5 right up
                        if matrix[r][c+1] == 1:
                            if up[r][c+1] == 0:
                                up[r][c+1] = 1
                                bfs(r, c+1, "up")
                        #6 right down
                        else:
                            if dn[r][c+1] == 0:
                                dn[r][c + 1] = 1
                                bfs(r, c+1, "down")
            else:
                # 1 down
                if r < n-1:
                    if up[r+1][c] == 0:
                        up[r+1][c] = 1
                        bfs(r+1, c, "up")
                # 2 up
                if matrix[r][c] == 0:
                    if up[r][c] == 0:
                        up[r][c] = 1
                        bfs(r, c, "up")
                if matrix[r][c] <= 0:
                    if c > 0:
                        # 3 left up
                        if matrix[r][c-1] == 1:
                            if dn[r][c-1] == 0:
                                dn[r][c-1] = 1
                                bfs(r, c-1, "down")
                        # 4 left down
                        else:
                            if up[r][c-1] == 0:
                                up[r][c-1] = 1
                                bfs(r, c-1, "up")
                if matrix[r][c] >= 0:
                    if c < n - 1:
                        # 5 right up
                        if matrix[r][c+1] == 1:
                            if up[r][c+1] == 0:
                                up[r][c+1] = 1
                                bfs(r, c+1, "up")
                        # 6 right down
                        else:
                            if dn[r][c+1] == 0:
                                dn[r][c+1] = 1
                                bfs(r, c+1, "down")

        n = len(grid)
        if n == 0:
            return 0
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        print(grid)
        for rr in range(n):
            toy = 0
            escaped = 0
            for cc in range(n):
                if grid[rr][cc] == " ":
                    matrix[rr][cc] = 0
                elif grid[rr][cc] == "/":
                    matrix[rr][cc] = 1
                else:
                    print("not here")
                    matrix[rr][cc] = -1
                    if escaped == 0:
                        toy += 1
                    escaped ^= 1
        print(matrix)

        up = [[0 for _ in range(n)] for _ in range(n)]
        dn = [[0 for _ in range(n)] for _ in range(n)]
        result = 0

        for rr in range(n):
            for cc in range(n):
                if up[rr][cc] == 0:
                    up[rr][cc] = 1
                    result += 1
                    bfs(rr,cc,"up")
                    print(result)
                    print(up)
                    print(dn)

                if dn[rr][cc] == 0:
                    dn[rr][cc] = 1
                    result += 1
                    bfs(rr,cc,"down")
                    print(result)
                    print(up)
                    print(dn)

        return result


if __name__ == "__main__":
    app = Solution()
    a = [" /", "/ "]
    print(app.leetcode(a))
