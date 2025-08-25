"""

Code
Testcase
Test Result
Test Result
Q2. Minimum Number of Flips to Make Binary Grid Palindromic I
Medium
4 pt.
You are given an m x n binary matrix grid.

A row or column is considered palindromic if its values read the same forward and backward.

You can flip any number of cells in grid from 0 to 1, or from 1 to 0.

Return the minimum number of cells that need to be flipped to make either all rows palindromic or all columns palindromic.



Example 1:

Input: grid = [[1,0,0],[0,0,0],[0,0,1]]

Output: 2

Explanation:



Flipping the highlighted cells makes all the rows palindromic.

Example 2:

Input: grid = [[0,1],[0,1],[0,0]]

Output: 1

Explanation:



Flipping the highlighted cell makes all the columns palindromic.

Example 3:

Input: grid = [[1],[0]]

Output: 0

Explanation:

All rows are already palindromic.



Constraints:

m == grid.length
n == grid[i].length
1 <= m * n <= 2 * 105
0 <= grid[i][j] <= 1
"""

from typing import List
from collections import defaultdict

class Solution:
    def leetcode(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        mresult = 0
        for ii in range(m):
            half = n//2
            for jj in range(half):
                if grid[ii][jj] != grid[ii][n-1-jj]:
                    mresult += 1

        nresult = 0
        for ii in range(n):
            half = m//2
            for jj in range(half):
                if grid[jj][ii] != grid[m-1-jj][ii]:
                    nresult += 1

        return min(mresult, nresult)

if __name__ == "__main__":
    app = Solution()
    a = [1,4,3,3,2]
    b = 2
    print(app.leetcode(a))
