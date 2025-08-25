"""
1937. Maximum Number of Points with Cost
Medium
Topics
Companies
Hint
You are given an m x n integer matrix points (0-indexed). Starting with 0 points, you want to maximize the number of points you can get from the matrix.

To gain points, you must pick one cell in each row. Picking the cell at coordinates (r, c) will add points[r][c] to your score.

However, you will lose points if you pick a cell too far from the cell that you picked in the previous row. For every two adjacent rows r and r + 1 (where 0 <= r < m - 1), picking cells at coordinates (r, c1) and (r + 1, c2) will subtract abs(c1 - c2) from your score.

Return the maximum number of points you can achieve.

abs(x) is defined as:

x for x >= 0.
-x for x < 0.


Example 1:


Input: points = [[1,2,3],[1,5,1],[3,1,1]]
Output: 9
Explanation:
The blue cells denote the optimal cells to pick, which have coordinates (0, 2), (1, 1), and (2, 0).
You add 3 + 5 + 3 = 11 to your score.
However, you must subtract abs(2 - 1) + abs(1 - 0) = 2 from your score.
Your final score is 11 - 2 = 9.
Example 2:


Input: points = [[1,5],[2,3],[4,2]]
Output: 11
Explanation:
The blue cells denote the optimal cells to pick, which have coordinates (0, 1), (1, 1), and (2, 0).
You add 5 + 3 + 4 = 12 to your score.
However, you must subtract abs(1 - 1) + abs(1 - 0) = 1 from your score.
Your final score is 12 - 1 = 11.


Constraints:

m == points.length
n == points[r].length
1 <= m, n <= 105
1 <= m * n <= 105
0 <= points[r][c] <= 105
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
    def leetcode(self, points: List[List[int]]) -> int:
        ### chatgpt
        m, n = len(points), len(points[0])

        # Initialize dp array as the first row of points
        dp = points[0]

        # Iterate through each row starting from the second row
        for r in range(1, m):
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
                dp[c] = points[r][c] + max(left_to_right[c], right_to_left[c])

        return max(dp)


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
