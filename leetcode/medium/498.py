"""
498. Diagonal Traverse
Solved
Medium
Topics
￼
Companies
Given an m x n matrix mat, return an array of all the elements of the array in a diagonal order.

 

Example 1:

￼
Input: mat = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,4,7,5,3,6,8,9]
Example 2:

Input: mat = [[1,2],[3,4]]
Output: [1,2,3,4]
 

Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 104
1 <= m * n <= 104
-105 <= mat[i][j] <= 105
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
    def leetcode(self, mat: List[List[int]]) -> List[int]:
        m = len(mat)
        n = len(mat[0])
        
        if m == 1:
            return mat[0]

        if n == 1:
            return [each[0] for each in mat]

        result = [0]*(m*n)
        result[-1] = mat[m-1][n-1]
        rr = 0
        cc = 0
        upward = 1
        for ii in range(m*n):
            result[ii] = mat[rr][cc]
            if upward:
                ### top edge
                if rr == 0:
                    upward = 0
                    ### top right cornor
                    if cc == n-1:
                        rr = 1
                    else:
                        cc += 1
                ### right edge
                elif cc == n-1:
                    upward = 0
                    ### end of mat
                    if rr == m-1:
                        break
                    else:
                        rr += 1
                else:
                    rr -= 1
                    cc += 1
            else:
                if rr == m-1:
                    upward = 1
                    cc += 1
                ### left edge
                elif cc == 0:
                    upward = 1
                    rr += 1
                else:
                    rr += 1
                    cc -= 1

            if rr >= m or cc >= n:
                break

        return result


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
