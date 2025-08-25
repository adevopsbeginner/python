"""

Code
Testcase
Test Result
Test Result
100359. Count Submatrices With Equal Frequency of X and Y
Medium
Given a 2D character matrix grid, where grid[i][j] is either 'X', 'Y', or '.', return the number of
submatrices
 that contains:

grid[0][0]
an equal frequency of 'X' and 'Y'.
at least one 'X'.


Example 1:

Input: grid = [["X","Y","."],["Y",".","."]]

Output: 3

Explanation:



Example 2:

Input: grid = [["X","X"],["X","Y"]]

Output: 0

Explanation:

No submatrix has an equal frequency of 'X' and 'Y'.

Example 3:

Input: grid = [[".","."],[".","."]]

Output: 0

Explanation:

No submatrix has at least one 'X'.



Constraints:

1 <= grid.length, grid[i].length <= 1000
grid[i][j] is either 'X', 'Y', or '.'.
"""

from typing import List
from collections import defaultdict

class Solution:
    def leetcode(self, grid: List[List[str]]) -> int:
        r = len(grid)
        c = len(grid[0])
        result = 0

        count = []
        for rr in range(r):
            count.append([])

        for rr in range(r):
            for cc in range(c):
                count[rr].append([0,0])

        if grid[0][0] == "X":
            count[0][0][0] = 1
        elif grid[0][0] == "Y":
            count[0][0][1] = 1

        for cc in range(1,c):
            count[0][cc][0] = count[0][cc-1][0]
            count[0][cc][1] = count[0][cc-1][1]
            if grid[0][cc] == "X":
                count[0][cc][0] += 1
            elif grid[0][cc] == "Y":
                count[0][cc][1] += 1

        for rr in range(1,r):
            linex = 0
            liney = 0
            for cc in range(c):
                if grid[rr][cc] == "X":
                    linex += 1
                elif grid[rr][cc] == "Y":
                    liney += 1
                count[rr][cc][0] = count[rr-1][cc][0]+linex
                count[rr][cc][1] = count[rr-1][cc][1]+liney


        for rr in range(r):
            for cc in range(c):
                if count[rr][cc][0] > 0 and count[rr][cc][0] == count[rr][cc][1]:
                    result += 1

        return result


if __name__ == "__main__":
    app = Solution()
    a = [["X","Y","."],["Y",".","."]]
    b = 2
    print(app.leetcode(a))
