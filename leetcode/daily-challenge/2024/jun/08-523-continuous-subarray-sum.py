"""

Code
Testcase
Test Result
Test Result
523. Continuous Subarray Sum
Medium
Topics
Companies
Given an integer array nums and an integer k, return true if nums has a good subarray or false otherwise.

A good subarray is a subarray where:

its length is at least two, and
the sum of the elements of the subarray is a multiple of k.
Note that:

A subarray is a contiguous part of the array.
An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k.


Example 1:

Input: nums = [23,2,4,6,7], k = 6
Output: true
Explanation: [2, 4] is a continuous subarray of size 2 whose elements sum up to 6.
Example 2:

Input: nums = [23,2,6,4,7], k = 6
Output: true
Explanation: [23, 2, 6, 4, 7] is an continuous subarray of size 5 whose elements sum up to 42.
42 is a multiple of 6 because 42 = 7 * 6 and 7 is an integer.
Example 3:

Input: nums = [23,2,6,4,7], k = 13
Output: false


Constraints:

1 <= nums.length <= 105
0 <= nums[i] <= 109
0 <= sum(nums[i]) <= 231 - 1
1 <= k <= 231 - 1
"""

import string
from typing import List
from collections import defaultdict

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def leetcode(self, nums: List[int], k: int) -> bool:
        remainder_index = {}
        current_sum = 0

        for i, num in enumerate(nums):
            current_sum += num
            remainder = current_sum % k

            if remainder < 0:  # Ensure the remainder is non-negative
                remainder += k

            # Check if we have a good subarray
            if remainder == 0 and i >= 1:
                return True

            if remainder in remainder_index:
                if i - remainder_index[remainder] >= 2:
                    return True
            else:
                remainder_index[remainder] = i

        return False

        ll = len(nums)
        for ii in range(ll-1):
            total = nums[ii]
            for jj in range(ii+1,ll):
                total += nums[jj]
                # print(ii,jj,total)
                if total % k == 0:
                    return True
        return False

if __name__ == "__main__":
    app = Solution()
    a = [23,2,6,4,7]
    b = 13
    print(app.leetcode(a,b))
