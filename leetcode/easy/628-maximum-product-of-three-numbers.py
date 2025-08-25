"""

Code
Testcase
Test Result
Test Result
628. Maximum Product of Three Numbers
Easy
Topics
Companies
Given an integer array nums, find three numbers whose product is maximum and return the maximum product.



Example 1:

Input: nums = [1,2,3]
Output: 6
Example 2:

Input: nums = [1,2,3,4]
Output: 24
Example 3:

Input: nums = [-1,-2,-3]
Output: -6


Constraints:

3 <= nums.length <= 104
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
    def leetcode(self, nums: List[int]) -> int:
        nums.sort()
        result = nums[-1]*nums[-2]*nums[-3]
        r1 = nums[0]*nums[1]*nums[2]
        r2 = nums[0]*nums[1]*nums[-1]
        r3 = nums[0]*nums[-2]*nums[-1]
        result = max(result, r1, r2, r3)
        return result


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
