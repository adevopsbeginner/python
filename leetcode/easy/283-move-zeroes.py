"""
283. Move Zeroes
Solved
Easy
Topics
Companies
Hint
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.



Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]


Constraints:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1


Follow up: Could you minimize the total number of operations done?
"""

import string
from typing import List
from collections import defaultdict

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def leetcode(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ll = len(nums)
        index0 = 0
        index1 = 0
        for ii in range(ll):
            if nums[ii] == 0:
                index0 = ii
                break
        for ii in range(index0+1, ll):
            if nums[ii]:
                index1 = ii
                break
            if ii == ll-1:
                return

        for ii in range(index0,ll-1):
            if nums[ii]:
                continue
            else:
                nums[ii],nums[index1] = nums[index1],nums[ii]

            while index1 < ll and nums[index1] == 0:
                index1 += 1

            if index1 == ll:
                return

        return


if __name__ == "__main__":
    app = Solution()
    a = [1,0,0]
    print(app.leetcode(a))
