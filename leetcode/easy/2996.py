"""
2996. Smallest Missing Integer Greater Than Sequential Prefix Sum
Easy
Topics
premium lock icon
Companies
Hint
You are given a 0-indexed array of integers nums.

A prefix nums[0..i] is sequential if, for all 1 <= j <= i, nums[j] = nums[j - 1] + 1. In particular, the prefix consisting only of nums[0] is sequential.

Return the smallest integer x missing from nums such that x is greater than or equal to the sum of the longest sequential prefix.

 

Example 1:

Input: nums = [1,2,3,2,5]
Output: 6
Explanation: The longest sequential prefix of nums is [1,2,3] with a sum of 6. 6 is not in the array, therefore 6 is the smallest missing integer greater than or equal to the sum of the longest sequential prefix.
Example 2:

Input: nums = [3,4,5,1,12,14,13]
Output: 15
Explanation: The longest sequential prefix of nums is [3,4,5] with a sum of 12. 12, 13, and 14 belong to the array while 15 does not. Therefore 15 is the smallest missing integer greater than or equal to the sum of the longest sequential prefix.
 

Constraints:

1 <= nums.length <= 50
1 <= nums[i] <= 50
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
        result = nums[0]
        for ii in range(1, ll):
            if nums[ii] == nums[ii-1]+1:
                result += nums[ii]
            else:
                break
        while result in nums:
            result += 1
        return result
        
        ### wrong answer, we are looking for PREFIX not any subarray
        ll = len(nums)
        result = max(nums)
        index0 = 0
        index1 = 1
        longest = 0
        subsum = nums[index0]
        while index0 < ll and index1 < ll:
            print(index0,index1,subsum,longest, result)
            if nums[index1] == nums[index1-1]+1:
                subsum += nums[index1]
                if index1-index0 == longest:
                    result = max(result, subsum)
                elif index1-index0 > longest:
                    result = subsum
                    
                longest += 1
                index1 += 1
            else:
                index0 = index1
                index1 = index0+1
                subsum = nums[index0]

        while result in nums:
            result += 1

        return result


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
