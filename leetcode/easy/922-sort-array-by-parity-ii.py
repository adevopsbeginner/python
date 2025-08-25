"""
922. Sort Array By Parity II
Easy
Topics
Companies
Given an array of integers nums, half of the integers in nums are odd, and the other half are even.

Sort the array so that whenever nums[i] is odd, i is odd, and whenever nums[i] is even, i is even.

Return any answer array that satisfies this condition.



Example 1:

Input: nums = [4,2,5,7]
Output: [4,5,2,7]
Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.
Example 2:

Input: nums = [2,3]
Output: [2,3]


Constraints:

2 <= nums.length <= 2 * 104
nums.length is even.
Half of the integers in nums are even.
0 <= nums[i] <= 1000


Follow Up: Could you solve it in-place?
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
        i0 = 0
        i1 = 1
        for ii in range(ll):
            #print(ii,i0,i1,nums)
            if ii%2 == 1:
                if nums[ii]%2 == 0:
                    while nums[i0]%2 == 0:
                        i0 += 2
                    nums[ii],nums[i0] = nums[i0],nums[ii]
            else:
                if nums[ii]%2 == 1:
                    while nums[i1]%2 == 1:
                        i1 += 2
                    nums[ii],nums[i1] = nums[i1],nums[ii]

        return nums


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
