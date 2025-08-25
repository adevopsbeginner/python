"""
260. Single Number III
Solved
Medium
Topics
Companies
Given an integer array nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once. You can return the answer in any order.

You must write an algorithm that runs in linear runtime complexity and uses only constant extra space.



Example 1:

Input: nums = [1,2,1,3,2,5]
Output: [3,5]
Explanation:  [5, 3] is also a valid answer.
Example 2:

Input: nums = [-1,0]
Output: [-1,0]
Example 3:

Input: nums = [0,1]
Output: [1,0]


Constraints:

2 <= nums.length <= 3 * 104
-231 <= nums[i] <= 231 - 1
Each integer in nums will appear twice, only two integers will appear once.
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
    def leetcode(self, arr: List[int]) -> int:
        ll = len(arr)
        arr.sort()
        a = arr[0]
        b = arr[1]
        for ii in range(0,ll,2):
            if arr[ii] - arr[ii+1]:
                a = arr[ii]
                for jj in range(ii+1,ll,2):
                    if jj == ll-1:
                        b = arr[jj]
                        return [a,b]
                    if arr[jj] - arr[jj+1]:
                        b = arr[jj]
                        return [a,b]

        return [a,b]

if __name__ == "__main__":
    app = Solution()
    a = [1,2,1,3,2,5]
    print(app.leetcode(a))
