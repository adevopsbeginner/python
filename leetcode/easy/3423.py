"""
3423. Maximum Difference Between Adjacent Elements in a Circular Array
Easy
Topics
premium lock icon
Companies
Hint
Given a circular array nums, find the maximum absolute difference between adjacent elements.

Note: In a circular array, the first and last elements are adjacent.

 

Example 1:

Input: nums = [1,2,4]

Output: 3

Explanation:

Because nums is circular, nums[0] and nums[2] are adjacent. They have the maximum absolute difference of |4 - 1| = 3.

Example 2:

Input: nums = [-5,-10,-5]

Output: 5

Explanation:

The adjacent elements nums[0] and nums[1] have the maximum absolute difference of |-5 - (-10)| = 5.

 

Constraints:

2 <= nums.length <= 100
-100 <= nums[i] <= 100
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
    def leetcode(self, nums: List[int]) -> int:
        result = abs(nums[-1]-nums[0])
        ll = len(nums)
        for ii in range(1,ll):
            result = max(result, abs(nums[ii]-nums[ii-1]))
        return result


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
