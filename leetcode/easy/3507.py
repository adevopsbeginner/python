"""
3507. Minimum Pair Removal to Sort Array I
Easy
Topics
premium lock icon
Companies
Hint
Given an array nums, you can perform the following operation any number of times:

Select the adjacent pair with the minimum sum in nums. If multiple such pairs exist, choose the leftmost one.
Replace the pair with their sum.
Return the minimum number of operations needed to make the array non-decreasing.

An array is said to be non-decreasing if each element is greater than or equal to its previous element (if it exists).

 

Example 1:

Input: nums = [5,2,3,1]

Output: 2

Explanation:

The pair (3,1) has the minimum sum of 4. After replacement, nums = [5,2,4].
The pair (2,4) has the minimum sum of 6. After replacement, nums = [5,6].
The array nums became non-decreasing in two operations.

Example 2:

Input: nums = [1,2,2]

Output: 0

Explanation:

The array nums is already sorted.

 

Constraints:

1 <= nums.length <= 50
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
        def is_non_decreasing(nums):
            ll = len(nums)
            for ii in range(1,ll):
                if nums[ii] < nums[ii-1]:
                    return False
            return True

        result = 0
        while not is_non_decreasing(nums):
            #print(result, nums)
            result += 1
            ll = len(nums)
            pair_sum = [0]*(ll-1)
            for ii in range(ll-1):
                pair_sum[ii] = nums[ii]+nums[ii+1]

            min_sum = min(pair_sum)
            index = 0
            for ii in range(ll-1):
                if pair_sum[ii] == min_sum:
                    index = ii
                    break
            #print(min_sum, index)
            nums[index] = pair_sum[index]
            nums.pop(index+1)
        return result


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
