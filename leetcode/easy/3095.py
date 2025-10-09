"""
3095. Shortest Subarray With OR at Least K I
Easy
Topics
premium lock icon
Companies
Hint
You are given an array nums of non-negative integers and an integer k.

An array is called special if the bitwise OR of all of its elements is at least k.

Return the length of the shortest special non-empty subarray of nums, or return -1 if no special subarray exists.

 

Example 1:

Input: nums = [1,2,3], k = 2

Output: 1

Explanation:

The subarray [3] has OR value of 3. Hence, we return 1.

Note that [2] is also a special subarray.

Example 2:

Input: nums = [2,1,8], k = 10

Output: 3

Explanation:

The subarray [2,1,8] has OR value of 11. Hence, we return 3.

Example 3:

Input: nums = [1,2], k = 0

Output: 1

Explanation:

The subarray [1] has OR value of 1. Hence, we return 1.

 

Constraints:

1 <= nums.length <= 50
0 <= nums[i] <= 50
0 <= k < 64
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
    def leetcode(self, nums: List[int], k: int) -> int:
        def array_or(start, end):
            result = 0
            for ii in range(start, end+1):
                result |= nums[ii]
            return result

        ll = len(nums)
        result = ll
        if array_or(0,ll-1) < k:
            return -1
        
        for ii in range(ll):
            for jj in range(ii,ll):
                if array_or(ii,jj) >= k:
                    result = min(result, jj-ii+1)
                    break
        return result


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
