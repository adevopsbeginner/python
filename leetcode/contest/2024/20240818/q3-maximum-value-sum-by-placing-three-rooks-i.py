"""
Q3. Maximum Value Sum by Placing Three Rooks I
Hard
6 pt.
You are given a m x n 2D array board representing a chessboard, where board[i][j] represents the value of the cell (i, j).

Rooks in the same row or column attack each other. You need to place three rooks on the chessboard such that the rooks do not attack each other.

Return the maximum sum of the cell values on which the rooks are placed.



Example 1:

Input: board = [[-3,1,1,1],[-3,1,-3,1],[-3,2,1,1]]

Output: 4

Explanation:



We can place the rooks in the cells (0, 2), (1, 3), and (2, 1) for a sum of 1 + 1 + 2 = 4.

Example 2:

Input: board = [[1,2,3],[4,5,6],[7,8,9]]

Output: 15

Explanation:

We can place the rooks in the cells (0, 0), (1, 1), and (2, 2) for a sum of 1 + 5 + 9 = 15.

Example 3:

Input: board = [[1,1,1],[1,1,1],[1,1,1]]

Output: 3

Explanation:

We can place the rooks in the cells (0, 2), (1, 1), and (2, 0) for a sum of 1 + 1 + 1 = 3.



Constraints:

3 <= m == board.length <= 100
3 <= n == board[i].length <= 100
-109 <= board[i][j] <= 109
"""

from typing import List
from collections import defaultdict

class Solution:
    def leetcode(self, board: List[List[int]]) -> int:
        m, n = len(board), len(board[0])
        dp = board[0]
        for r in range(1,m):
            print(dp)
            # Left to right pass
            left_to_right = [0] * n
            left_to_right[0] = dp[0]
            for c in range(1, n):
                left_to_right[c] = max(left_to_right[c - 1] - 1, dp[c])

            # Right to left pass
            right_to_left = [0] * n
            right_to_left[n - 1] = dp[n - 1]
            for c in range(n - 2, -1, -1):
                right_to_left[c] = max(right_to_left[c + 1] - 1, dp[c])

            # Update dp with max of left_to_right and right_to_left plus points in current row
            for c in range(n):
                dp[c] = board[r][c] + max(left_to_right[c], right_to_left[c])
            print(dp)

        return max(dp)

if __name__ == "__main__":
    app = Solution()
    a = [1,4,3,3,2]
    b = 2
    print(app.leetcode(a))
