"""
Q1. Smallest Pair With Different Frequencies
Easy
3 pt.
You are given an integer array nums.

Consider all pairs of distinct values x and y from nums such that:

x < y
x and y have different frequencies in nums.
Among all such pairs:

Choose the pair with the smallest possible value of x.
If multiple pairs have the same x, choose the one with the smallest possible value of y.
Return an integer array [x, y]. If no valid pair exists, return [-1, -1].

The frequency of a value x is the number of times it occurs in the array.

 

Example 1:

Input: nums = [1,1,2,2,3,4]

Output: [1,3]

Explanation:

The smallest value is 1 with a frequency of 2, and the smallest value greater than 1 that has a different frequency from 1 is 3 with a frequency of 1. Thus, the answer is [1, 3].

Example 2:

Input: nums = [1,5]

Output: [-1,-1]

Explanation:

Both values have the same frequency, so no valid pair exists. Return [-1, -1].

Example 3:

Input: nums = [7]

Output: [-1,-1]

Explanation:

There is only one value in the array, so no valid pair exists. Return [-1, -1].

 

Constraints:

1 <= nums.length <= 100
1 <= nums[i] <= 100
"""

from typing import List
from collections import defaultdict

class Solution:
    def leetcode(self, nums: list[int]) -> list[int]:
        nums.sort()
        dd = defaultdict(int)
        x = nums[0]
        y = -1
        for num in nums:
            dd[num] += 1

        for each in dd:
            if each == nums[0]:
                continue
            elif dd[each] == dd[nums[0]]:
                continue
            else:
                y = each
                break
        
        if y == -1:
            x = -1
            
        return [x,y]
