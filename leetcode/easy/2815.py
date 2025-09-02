"""
2815. Max Pair Sum in an Array
Easy
Topics
premium lock icon
Companies
Hint
You are given an integer array nums. You have to find the maximum sum of a pair of numbers from nums such that the largest digit in both numbers is equal.

For example, 2373 is made up of three distinct digits: 2, 3, and 7, where 7 is the largest among them.

Return the maximum sum or -1 if no such pair exists.

 

Example 1:

Input: nums = [112,131,411]

Output: -1

Explanation:

Each numbers largest digit in order is [2,3,4].

Example 2:

Input: nums = [2536,1613,3366,162]

Output: 5902

Explanation:

All the numbers have 6 as their largest digit, so the answer is 2536 + 3366 = 5902.

Example 3:

Input: nums = [51,71,17,24,42]

Output: 88

Explanation:

Each number's largest digit in order is [5,7,7,4,4].

So we have only two possible pairs, 71 + 17 = 88 and 24 + 42 = 66.

 

Constraints:

2 <= nums.length <= 100
1 <= nums[i] <= 104
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
        def max_digit(num):
            result = 0
            while num:
                result = max(result, num%10)
                num //= 10
            return result

        ll = len(nums)
        for ii in range(ll):
            nums[ii] = [max_digit(nums[ii]), nums[ii]]
        nums.sort(reverse=True)

        #print(nums)

        result = -1
        for ii in range(1,ll):
            if nums[ii][0] == nums[ii-1][0]:
                result = max(result, nums[ii][1] + nums[ii-1][1])
        return result


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
