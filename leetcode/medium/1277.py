"""
1277. Count Square Submatrices with All Ones
Solved
Medium
Topics
premium lock icon
Companies
Hint
Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.

 

Example 1:

Input: matrix =
[
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]
Output: 15
Explanation: 
There are 10 squares of side 1.
There are 4 squares of side 2.
There is  1 square of side 3.
Total number of squares = 10 + 4 + 1 = 15.
Example 2:

Input: matrix = 
[
  [1,0,1],
  [1,1,0],
  [1,1,0]
]
Output: 7
Explanation: 
There are 6 squares of side 1.  
There is 1 square of side 2. 
Total number of squares = 6 + 1 = 7.
 

Constraints:

1 <= arr.length <= 300
1 <= arr[0].length <= 300
0 <= arr[i][j] <= 1
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
    def leetcode(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        result = 0

        ### 3. counting how many 1's to the right and to the bottom
        for rr in range(m-1,-1,-1):
            for cc in range(n-1,-1,-1):
                if matrix[rr][cc] == 0:
                    matrix[rr][cc] = [0,0,0]
                    continue

                down1 = 0
                if rr < m-1:
                    down1 = matrix[rr+1][cc][2]
                    if cc < n-1:
                        down1 = min(down1, matrix[rr+1][cc+1][2])
                right1 = 0
                if cc < n-1:
                    right1 = matrix[rr][cc+1][1]
                    if rr < m-1:
                        right1 = min(right1, matrix[rr+1][cc+1][1])
                
                
                matrix[rr][cc] = [1, right1+1, down1+1]

        #print(matrix)

        ### 1. the loop
        for rr in range(m):
            for cc in range(n):
                ### 2. counting squares start from this element
                #print(matrix[rr][cc][1], matrix[rr][cc][2])
                result += min(matrix[rr][cc][1], matrix[rr][cc][2])

        return result


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
