"""
3242. Design Neighbor Sum Service
Solved
Easy
Companies
Hint
You are given a n x n 2D array grid containing distinct elements in the range [0, n2 - 1].

Implement the neighborSum class:

neighborSum(int [][]grid) initializes the object.
int adjacentSum(int value) returns the sum of elements which are adjacent neighbors of value, that is either to the top, left, right, or bottom of value in grid.
int diagonalSum(int value) returns the sum of elements which are diagonal neighbors of value, that is either to the top-left, top-right, bottom-left, or bottom-right of value in grid.




Example 1:

Input:

["neighborSum", "adjacentSum", "adjacentSum", "diagonalSum", "diagonalSum"]

[[[[0, 1, 2], [3, 4, 5], [6, 7, 8]]], [1], [4], [4], [8]]

Output: [null, 6, 16, 16, 4]

Explanation:



The adjacent neighbors of 1 are 0, 2, and 4.
The adjacent neighbors of 4 are 1, 3, 5, and 7.
The diagonal neighbors of 4 are 0, 2, 6, and 8.
The diagonal neighbor of 8 is 4.
Example 2:

Input:

["neighborSum", "adjacentSum", "diagonalSum"]

[[[[1, 2, 0, 3], [4, 7, 15, 6], [8, 9, 10, 11], [12, 13, 14, 5]]], [15], [9]]

Output: [null, 23, 45]

Explanation:



The adjacent neighbors of 15 are 0, 10, 7, and 6.
The diagonal neighbors of 9 are 4, 12, 14, and 15.


Constraints:

3 <= n == grid.length == grid[0].length <= 10
0 <= grid[i][j] <= n2 - 1
All grid[i][j] are distinct.
value in adjacentSum and diagonalSum will be in the range [0, n2 - 1].
At most 2 * n2 calls will be made to adjacentSum and diagonalSum.
"""

from typing import List
from collections import defaultdict


class neighborSum:

    def __init__(self, grid: List[List[int]]):
        n = len(grid)
        self.grid = [[grid[ii][jj] for jj in range(n)] for ii in range(n)]
        self.adjacent = [[0 for _ in range(n)] for _ in range(n)]
        self.diagonal = [[0 for _ in range(n)] for _ in range(n)]
        for ii in range(n):
            for jj in range(n):
                a = b = c = d = e = f = g = h = 0
                if ii > 0:
                    a = self.grid[ii - 1][jj]
                if ii < n - 1:
                    b = self.grid[ii + 1][jj]
                if jj > 0:
                    c = self.grid[ii][jj - 1]
                if jj < n - 1:
                    d = self.grid[ii][jj + 1]
                if ii > 0 and jj > 0:
                    e = self.grid[ii - 1][jj - 1]
                if ii > 0 and jj < n - 1:
                    f = self.grid[ii - 1][jj + 1]
                if ii < n - 1 and jj > 0:
                    # print(111)
                    g = self.grid[ii + 1][jj - 1]
                if ii < n - 1 and jj < n - 1:
                    print(222)
                    h = self.grid[ii + 1][jj + 1]
                # if ii == 1 and jj == 1:
                #    print(a,b,c,d,e,f,g,self.grid[2][0],h, self.grid[2][2])
                self.adjacent[ii][jj] = a + b + c + d
                self.diagonal[ii][jj] = e + f + g + h
        # print(self.diagonal)

    def adjacentSum(self, value: int) -> int:
        n = len(self.grid)
        for ii in range(n):
            for jj in range(n):
                if self.grid[ii][jj] == value:
                    return self.adjacent[ii][jj]

    def diagonalSum(self, value: int) -> int:
        n = len(self.grid)
        for ii in range(n):
            for jj in range(n):
                if self.grid[ii][jj] == value:
                    return self.diagonal[ii][jj]


# Your neighborSum object will be instantiated and called as such:
# obj = neighborSum(grid)
# param_1 = obj.adjacentSum(value)
# param_2 = obj.diagonalSum(value)

if __name__ == "__main__":
    app = Solution()
    a = [1,4,3,3,2]
    b = 2
    print(app.leetcode(a))
