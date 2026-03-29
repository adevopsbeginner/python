"""
Q1. Minimum Absolute Difference Between Two Values
Easy
3 pt.
You are given an integer array nums consisting only of 0, 1, and 2.

A pair of indices (i, j) is called valid if nums[i] == 1 and nums[j] == 2.

Return the minimum absolute difference between i and j among all valid pairs. If no valid pair exists, return -1.

The absolute difference between indices i and j is defined as abs(i - j).

 

Example 1:

Input: nums = [1,0,0,2,0,1]

Output: 2

Explanation:

The valid pairs are:

(0, 3) which has absolute difference of abs(0 - 3) = 3.
(5, 3) which has absolute difference of abs(5 - 3) = 2.
Thus, the answer is 2.

Example 2:

Input: nums = [1,0,1,0]

Output: -1

Explanation:

There are no valid pairs in the array, thus the answer is -1.

 

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 2
"""

from typing import List
from collections import defaultdict

class Solution:
    def leetcode(self, nums: list[int]) -> int:
        ll = len(nums)
        result = ll+1
        index1 = -1
        index2 = -1
        for ii in range(ll):
            if nums[ii] == 1:
                if index2 >= 0:
                    result = min(ii-index2, result)
                index1 = ii
                
            elif nums[ii] == 2:
                if index1 >= 0:
                    result = min(ii-index1, result)
                index2 = ii

        if index1 >= 0 and index2 >= 0:
            result = min(result, abs(index1-index2))
        
        if result > ll:
            return -1
        return result
