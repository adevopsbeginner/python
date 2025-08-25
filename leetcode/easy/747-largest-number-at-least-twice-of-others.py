"""
747. Largest Number At Least Twice of Others
Easy
Topics
Companies
Hint
You are given an integer array nums where the largest integer is unique.

Determine whether the largest element in the array is at least twice as much as every other number in the array. If it is, return the index of the largest element, or return -1 otherwise.



Example 1:

Input: nums = [3,6,1,0]
Output: 1
Explanation: 6 is the largest integer.
For every other number in the array x, 6 is at least twice as big as x.
The index of value 6 is 1, so we return 1.
Example 2:

Input: nums = [1,2,3,4]
Output: -1
Explanation: 4 is less than twice the value of 3, so we return -1.


Constraints:

2 <= nums.length <= 50
0 <= nums[i] <= 100
The largest element in nums is unique.
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
        ll = len(nums)
        result = -1
        ifirst = 0
        first = nums[ifirst]
        isecond = 1
        second = nums[isecond]
        if nums[isecond] > first:
            ifirst = 1
            first = nums[ifirst]
            isecond = 0
            second = nums[isecond]

        for ii in range(2,ll):
            if nums[ii] >= first:
                isecond = ifirst
                second = first
                ifirst = ii
                first = nums[ii]
            elif nums[ii] > second:
                isecond = ii
                second = nums[ii]

        if first >= second*2:
            return ifirst

        return result


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
