"""
3637. Trionic Array I
Solved
Easy
premium lock icon
Companies
Hint
You are given an integer array nums of length n.

An array is trionic if there exist indices 0 < p < q < n − 1 such that:

nums[0...p] is strictly increasing,
nums[p...q] is strictly decreasing,
nums[q...n − 1] is strictly increasing.
Return true if nums is trionic, otherwise return false.

 

Example 1:

Input: nums = [1,3,5,4,2,6]

Output: true

Explanation:

Pick p = 2, q = 4:

nums[0...2] = [1, 3, 5] is strictly increasing (1 < 3 < 5).
nums[2...4] = [5, 4, 2] is strictly decreasing (5 > 4 > 2).
nums[4...5] = [2, 6] is strictly increasing (2 < 6).
Example 2:

Input: nums = [2,1,3]

Output: false

Explanation:

There is no way to pick p and q to form the required three segments.

 

Constraints:

3 <= n <= 100
-1000 <= nums[i] <= 1000
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
    def leetcode(self, nums: List[int]) -> bool:
        ll = len(nums)
        if nums[1] <= nums[0]:
            return False
        if nums[-1] <= nums[-2]:
            return False

        point1_flag = 0
        point2_flag = 0

        for ii in range(2, ll-1):
            if nums[ii] == nums[ii-1]:
                return False
            if point1_flag == 0:
                if nums[ii] < nums[ii-1]:
                    point1_flag = 1
            else:
                if point2_flag == 0:
                    if nums[ii] > nums[ii-1]:
                        point2_flag = 1
                else:
                    if nums[ii] < nums[ii-1]:
                        return False
        if point1_flag == 0:
            return False
            
        return True


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
