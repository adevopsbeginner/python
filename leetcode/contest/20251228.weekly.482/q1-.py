"""
Q1. Maximum Score of a Split
Medium
4 pt.
You are given an integer array nums of length n.

Choose an index i such that 0 <= i < n - 1.

For a chosen split index i:

Let prefixSum(i) be the sum of nums[0] + nums[1] + ... + nums[i].
Let suffixMin(i) be the minimum value among nums[i + 1], nums[i + 2], ..., nums[n - 1].
The score of a split at index i is defined as:

score(i) = prefixSum(i) - suffixMin(i)

Return an integer denoting the maximum score over all valid split indices.

 

Example 1:

Input: nums = [10,-1,3,-4,-5]

Output: 17

Explanation:

The optimal split is at i = 2, score(2) = prefixSum(2) - suffixMin(2) = (10 + (-1) + 3) - (-5) = 17.

Example 2:

Input: nums = [-7,-5,3]

Output: -2

Explanation:

The optimal split is at i = 0, score(0) = prefixSum(0) - suffixMin(0) = (-7) - (-5) = -2.

Example 3:

Input: nums = [1,1]

Output: 0

Explanation:

The only valid split is at i = 0, score(0) = prefixSum(0) - suffixMin(0) = 1 - 1 = 0.

 

Constraints:

2 <= nums.length <= 105
-109​​​​​​​ <= nums[i] <= 109
"""

from typing import List
from collections import defaultdict

class Solution:
    def leetcode(self, nums: List[int]) -> int:
        ll = len(nums)
        sum_nums = sum(nums)-nums[-1]
        result = sum_nums-nums[-1]
        heap = [nums[-1]]
        for ii in range(ll-2,-1,-1):
            #print(ii,sum_nums, heap[0])
            result = max(result, sum_nums-heap[0])
            heapq.heappush(heap, nums[ii])
            sum_nums -= nums[ii]
        
        return result
