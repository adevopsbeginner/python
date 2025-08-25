"""
2661. First Completely Painted Row or Column
Solved
Medium
Topics
Companies
Hint
You are given a 0-indexed integer array arr, and an m x n integer matrix mat. arr and mat both contain all the integers in the range [1, m * n].

Go through each index i in arr starting from index 0 and paint the cell in mat containing the integer arr[i].

Return the smallest index i at which either a row or a column will be completely painted in mat.

 

Example 1:

image explanation for example 1
Input: arr = [1,3,4,2], mat = [[1,4],[2,3]]
Output: 2
Explanation: The moves are shown in order, and both the first row and second column of the matrix become fully painted at arr[2].
Example 2:

image explanation for example 2
Input: arr = [2,8,7,4,1,3,5,6,9], mat = [[3,2,5],[1,4,6],[8,7,9]]
Output: 3
Explanation: The second column becomes fully painted at arr[3].
 

Constraints:

m == mat.length
n = mat[i].length
arr.length == m * n
1 <= m, n <= 105
1 <= m * n <= 105
1 <= arr[i], mat[r][c] <= m * n
All the integers of arr are unique.
All the integers of mat are unique.
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
    def leetcode(self, arr: List[int], mat: List[List[int]]) -> int:
        m,n = len(mat), len(mat[0])
        ddr = defaultdict(int)
        ddc = defaultdict(int)
        for r in range(m):
            for c in range(n):
                ddr[mat[r][c]] = r
                ddc[mat[r][c]] = c
        
        ll = len(arr)
        rsum = [0]*m
        csum = [0]*n
        for ii in range(ll):
            rsum[ddr[arr[ii]]] += 1
            csum[ddc[arr[ii]]] += 1

            if rsum[ddr[arr[ii]]] == n:
                return ii
            if csum[ddc[arr[ii]]] == m:
                return ii

        return ll-1


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
