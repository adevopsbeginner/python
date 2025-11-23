"""
1262. Greatest Sum Divisible by Three
Medium
Topics
premium lock icon
Companies
Hint
Given an integer array nums, return the maximum possible sum of elements of the array such that it is divisible by three.

 

Example 1:

Input: nums = [3,6,5,1,8]
Output: 18
Explanation: Pick numbers 3, 6, 1 and 8 their sum is 18 (maximum sum divisible by 3).
Example 2:

Input: nums = [4]
Output: 0
Explanation: Since 4 is not divisible by 3, do not pick any number.
Example 3:

Input: nums = [1,2,3,4,4]
Output: 12
Explanation: Pick numbers 1, 3, 4 and 4 their sum is 12 (maximum sum divisible by 3).
 

Constraints:

1 <= nums.length <= 4 * 104
1 <= nums[i] <= 104
"""

import string
import heapq
from typing import List
from collections import defaultdict

class Solution:
    def leetcode(self, nums: List[int]) -> int:
        m11 = m12 = m13 = 0
        m21 = m22 = m23 = 0
        nums.sort(reverse=True)
        
        total = sum(nums)
        if total%3 == 0:
            return total
        
        for num in nums:
            if num%3 == 1:
                m11, m12, m13 = m12, m13, num
            elif num%3 == 2:
                m21, m22, m23 = m22, m23, num

        
        total -= m11+m12+m13+m21+m22+m23
        result = []

        if (total+m21)%3 == 0:
            result.append(total+m21)
        if (total+m21+m22)%3 == 0:
            result.append(total+m21+m22)
        if (total+m21+m22+m23)%3 == 0:
            result.append(total+m21+m22+m23)

        if (total+m11+m21)%3 == 0:
            result.append(total+m11+m21)
        if (total+m11+m21+m22)%3 == 0:
            result.append(total+m11+m21+m22)
        if (total+m11+m21+m22+m23)%3 == 0:
            result.append(total+m11+m21+m22+m23)

        if (total+m11+m12+m21)%3 == 0:
            result.append(total+m11+m12+m21)
        if (total+m11+m12+m21+m22)%3 == 0:
            result.append(total+m11+m12+m21+m22)
        if (total+m11+m12+m21+m22+m23)%3 == 0:
            result.append(total+m11+m12+m21+m22+m23)

        if (total+m11+m12+m13+m21)%3 == 0:
            result.append(total+m11+m12+m13+m21)
        if (total+m11+m12+m13+m21+m22)%3 == 0:
            result.append(total+m11+m12+m13+m21+m22)
        if (total+m11+m12+m13+m21+m22+m23)%3 == 0:
            result.append(total+m11+m12+m13+m21+m22+m23)

        return max(result)