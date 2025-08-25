"""

Code
Testcase
Test Result
Test Result
Q3. Minimum Number of Flips to Make Binary Grid Palindromic II
Medium
5 pt.
You are given an m x n binary matrix grid.

A row or column is considered palindromic if its values read the same forward and backward.

You can flip any number of cells in grid from 0 to 1, or from 1 to 0.

Return the minimum number of cells that need to be flipped to make all rows and columns palindromic, and the total number of 1's in grid divisible by 4.



Example 1:

Input: grid = [[1,0,0],[0,1,0],[0,0,1]]

Output: 3

Explanation:



Example 2:

Input: grid = [[0,1],[0,1],[0,0]]

Output: 2

Explanation:



Example 3:

Input: grid = [[1],[1]]

Output: 2

Explanation:





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
        ### not finishe, middle(s) has to be palindromic as well
        m = len(grid)
        n = len(grid[0])
        mhalf = m // 2
        nhalf = n // 2
        result = 0
        for ii in range(mhalf):
            for jj in range(nhalf):
                a = grid[ii][jj]
                b = grid[ii][n - 1 - jj]
                c = grid[m - 1 - ii][jj]
                d = grid[m - 1 - ii][n - 1 - jj]
                if a + b + c + d == 0:
                    pass
                elif a + b + c + d == 1:
                    result += 1
                elif a + b + c + d == 2:
                    result += 2
                elif a + b + c + d == 3:
                    result += 1
                elif a + b + c + d == 4:
                    pass
        middle1 = 0
        middle = 0
        if m % 2:
            middle += n
            for ii in range(n):
                middle1 += grid[mhalf][ii]
        if n % 2:
            middle += m
            for ii in range(m):
                middle1 += grid[ii][nhalf]
        if m % 2 and n % 2:
            middle1 -= grid[mhalf][nhalf]
            middle -= 1

        middle1 %= 4
        if middle < 4:
            return result + middle1

        return result + min(middle1, 4 - middle1)

if __name__ == "__main__":
    app = Solution()
    a = [1,4,3,3,2]
    b = 2
    print(app.leetcode(a))
