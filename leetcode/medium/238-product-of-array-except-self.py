"""
238. Product of Array Except Self
Solved
Medium
Topics
Companies
Hint
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer.
 

Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)
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
    def leetcode(self, nums: List[int]) -> List[int]:
        ll = len(nums)
        product = 1
        count0 = 0
        product_no_0 = 1
        for each in nums:
            product *= each
            if each == 0:
                count0 += 1
            else:
                product_no_0 *= each

        #print(product, product_no_0)

        for ii in range(ll):
            if nums[ii] == 0:
                if count0 > 1:
                    nums[ii] = 0
                elif count0 == 1:
                    nums[ii] = product_no_0
            else:
                if count0 > 0:
                    nums[ii] = 0
                else:
                    nums[ii] = product//nums[ii]

        return nums


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
