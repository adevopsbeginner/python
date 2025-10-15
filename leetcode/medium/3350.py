"""
3350. Adjacent Increasing Subarrays Detection II
Attempted
Medium
Topics
premium lock icon
Companies
Hint
Given an array nums of n integers, your task is to find the maximum value of k for which there exist two adjacent subarrays of length k each, such that both subarrays are strictly increasing. Specifically, check if there are two subarrays of length k starting at indices a and b (a < b), where:

Both subarrays nums[a..a + k - 1] and nums[b..b + k - 1] are strictly increasing.
The subarrays must be adjacent, meaning b = a + k.
Return the maximum possible value of k.

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [2,5,7,8,9,2,3,4,3,1]

Output: 3

Explanation:

The subarray starting at index 2 is [7, 8, 9], which is strictly increasing.
The subarray starting at index 5 is [2, 3, 4], which is also strictly increasing.
These two subarrays are adjacent, and 3 is the maximum possible value of k for which two such adjacent strictly increasing subarrays exist.
Example 2:

Input: nums = [1,2,3,4,4,4,4,5,6,7]

Output: 2

Explanation:

The subarray starting at index 0 is [1, 2], which is strictly increasing.
The subarray starting at index 2 is [3, 4], which is also strictly increasing.
These two subarrays are adjacent, and 2 is the maximum possible value of k for which two such adjacent strictly increasing subarrays exist.
 

Constraints:

2 <= nums.length <= 2 * 105
-109 <= nums[i] <= 109
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
        k_a = 0
        k_b = 1
        k = 1
        a = 0
        for ii in range(1, ll):
            #print(ii, nums[ii], nums[ii-1], k_a, k_b, k)
            if nums[ii] > nums[ii-1]:
                k_b = ii-a+1
                k = max(k, k_b//2, min(k_a, k_b))
                if ii == ll-1:
                    return k
            else:
                k = max(k, k_b//2, min(k_a, k_b))
                k_a = k_b
                k_b = 1
                a = ii


        return k


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
