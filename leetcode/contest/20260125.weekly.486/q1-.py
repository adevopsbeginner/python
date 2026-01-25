"""
Q1. Minimum Prefix Removal to Make Array Strictly Increasing
Medium
4 pt.
You are given an integer array nums.

You need to remove exactly one prefix (possibly empty) from nums.

Return an integer denoting the minimum length of the removed prefix such that the remaining array is strictly increasing.

 

Example 1:

Input: nums = [1,-1,2,3,3,4,5]

Output: 4

Explanation:

Removing the prefix = [1, -1, 2, 3] leaves the remaining array [3, 4, 5] which is strictly increasing.

Example 2:

Input: nums = [4,3,-2,-5]

Output: 3

Explanation:

Removing the prefix = [4, 3, -2] leaves the remaining array [-5] which is strictly increasing.

Example 3:

Input: nums = [1,2,3,4]

Output: 0

Explanation:

The array nums = [1, 2, 3, 4] is already strictly increasing so removing an empty prefix is sufficient.

 

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
"""

from typing import List
from collections import defaultdict

class Solution:
    def leetcode(self, nums: List[int]) -> int:
        ll = len(nums)
        for ii in range(ll-2,-1,-1):
            if nums[ii] >= nums[ii+1]:
                return ii+1

        return 0