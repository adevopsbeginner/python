"""
1749. Maximum Absolute Sum of Any Subarray
Medium
Topics
Companies
Hint
You are given an integer array nums. The absolute sum of a subarray [numsl, numsl+1, ..., numsr-1, numsr] is abs(numsl + numsl+1 + ... + numsr-1 + numsr).

Return the maximum absolute sum of any (possibly empty) subarray of nums.

Note that abs(x) is defined as follows:

If x is a negative integer, then abs(x) = -x.
If x is a non-negative integer, then abs(x) = x.
 

Example 1:

Input: nums = [1,-3,2,3,-4]
Output: 5
Explanation: The subarray [2,3] has absolute sum = abs(2+3) = abs(5) = 5.
Example 2:

Input: nums = [2,-5,1,-4,3,-2]
Output: 8
Explanation: The subarray [-5,1,-4] has absolute sum = abs(-5+1-4) = abs(-8) = 8.
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
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
        ### kadane's algorithm
        max_sum = 0
        min_sum = 0
        max_so_far = 0
        min_so_far = 0
        
        for num in nums:
            max_so_far = max(num, max_so_far+num)
            min_so_far = min(num, min_so_far+num)
            max_sum = max(max_sum, max_so_far)
            min_sum = min(min_sum, min_so_far)
        return max(max_sum, abs(min_sum))

        ### time limit exceeded
        sum_nums = sum(nums)
        if min(nums) >=0 :
            return sum_nums
        if max(nums) <= 0:
            return -sum_nums

        result = 0
        ll = len(nums)

        ### merge neighour positives or negatives
        for ii in range(ll-1):
            if nums[ii] == 0:
                continue
            if nums[ii+1] == 0:
                nums[ii], nums[ii+1] = 0, nums[ii]
            elif nums[ii] < 0 and nums[ii+1] < 0 or nums[ii] > 0 and nums[ii+1] > 0:
                nums[ii+1] += nums[ii]
                nums[ii] = 0
            
        for ii in range(ll):
            if nums[ii] == 0:
                continue
            sub_sum = 0
            for jj in range(ii, ll):
                if nums[jj] == 0:
                    continue
                sub_sum += nums[jj]
                result = max(result, abs(sub_sum))

        return result


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
