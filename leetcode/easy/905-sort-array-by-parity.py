"""
905. Sort Array By Parity
Solved
Easy
Topics
Companies
Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.

Return any array that satisfies this condition.



Example 1:

Input: nums = [3,1,2,4]
Output: [2,4,3,1]
Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
Example 2:

Input: nums = [0]
Output: [0]


Constraints:

1 <= nums.length <= 5000
0 <= nums[i] <= 5000
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
        copy = [each for each in nums]
        index = 0
        for each in copy:
            if each%2 == 0:
                nums[index] = each
                index += 1
        for each in copy:
            if each%2 == 1:
                nums[index] = each
                index += 1

        return nums


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
