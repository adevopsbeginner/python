"""
2326. Spiral Matrix IV
Solved
Medium
Topics
Companies
Hint
You are given two integers m and n, which represent the dimensions of a matrix.

You are also given the head of a linked list of integers.

Generate an m x n matrix that contains the integers in the linked list presented in spiral order (clockwise), starting from the top-left of the matrix. If there are remaining empty spaces, fill them with -1.

Return the generated matrix.



Example 1:


Input: m = 3, n = 5, head = [3,0,2,6,8,1,7,9,4,2,5,5,0]
Output: [[3,0,2,6,8],[5,0,-1,-1,1],[5,2,4,9,7]]
Explanation: The diagram above shows how the values are printed in the matrix.
Note that the remaining spaces in the matrix are filled with -1.
Example 2:


Input: m = 1, n = 4, head = [0,1,2]
Output: [[0,1,2,-1]]
Explanation: The diagram above shows how the values are printed from left to right in the matrix.
The last space in the matrix is set to -1.


Constraints:

1 <= m, n <= 105
1 <= m * n <= 105
The number of nodes in the list is in the range [1, m * n].
0 <= Node.val <= 1000
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
    def leetcode(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        matrix = [[0 for _ in range(n)] for _ in range(m)]
        result = [[-1 for _ in range(n)] for _ in range(m)]
        r = 0
        c = 0
        d = 1
        while head:
            #print(m,n,r,c,d, matrix)
            if matrix[r][c] == 0:
                result[r][c] = head.val
                matrix[r][c] = 1
                head = head.next
            if d == 0:
                if r > 0 and matrix[r-1][c] == 0:
                    r -= 1
                else:
                    d = 1
                    if c < n-1 and matrix[r][c+1] == 0:
                        c += 1
            elif d == 1:
                if c < n-1 and matrix[r][c+1] == 0:
                    c += 1
                else:
                    d = 2
                    if r < m-1 and matrix[r+1][c] == 0:
                        r += 1
            elif d == 2:
                if r < m-1 and matrix[r+1][c] == 0:
                    r += 1
                else:
                    d = 3
                    if r > 0 and matrix[r][c-1] == 0:
                        c -= 1
            elif d == 3:
                if c > 0 and matrix[r][c-1] == 0:
                    c -= 1
                else:
                    d = 0
                    if r > 0 and matrix[r-1][c] == 0:
                        r -= 1
            #print(r,c,d)


        return result



if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
