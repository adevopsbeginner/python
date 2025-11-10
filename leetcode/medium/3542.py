"""
3542. Minimum Operations to Convert All Elements to Zero
Medium
Topics
premium lock icon
Companies
Hint
You are given an array nums of size n, consisting of non-negative integers. Your task is to apply some (possibly zero) operations on the array so that all elements become 0.

In one operation, you can select a subarray [i, j] (where 0 <= i <= j < n) and set all occurrences of the minimum non-negative integer in that subarray to 0.

Return the minimum number of operations required to make all elements in the array 0.

 

Example 1:

Input: nums = [0,2]

Output: 1

Explanation:

Select the subarray [1,1] (which is [2]), where the minimum non-negative integer is 2. Setting all occurrences of 2 to 0 results in [0,0].
Thus, the minimum number of operations required is 1.
Example 2:

Input: nums = [3,1,2,1]

Output: 3

Explanation:

Select subarray [1,3] (which is [1,2,1]), where the minimum non-negative integer is 1. Setting all occurrences of 1 to 0 results in [3,0,2,0].
Select subarray [2,2] (which is [2]), where the minimum non-negative integer is 2. Setting all occurrences of 2 to 0 results in [3,0,0,0].
Select subarray [0,0] (which is [3]), where the minimum non-negative integer is 3. Setting all occurrences of 3 to 0 results in [0,0,0,0].
Thus, the minimum number of operations required is 3.
Example 3:

Input: nums = [1,2,1,2,1,2]

Output: 4

Explanation:

Select subarray [0,5] (which is [1,2,1,2,1,2]), where the minimum non-negative integer is 1. Setting all occurrences of 1 to 0 results in [0,2,0,2,0,2].
Select subarray [1,1] (which is [2]), where the minimum non-negative integer is 2. Setting all occurrences of 2 to 0 results in [0,0,0,2,0,2].
Select subarray [3,3] (which is [2]), where the minimum non-negative integer is 2. Setting all occurrences of 2 to 0 results in [0,0,0,0,0,2].
Select subarray [5,5] (which is [2]), where the minimum non-negative integer is 2. Setting all occurrences of 2 to 0 results in [0,0,0,0,0,0].
Thus, the minimum number of operations required is 4.
 

Constraints:

1 <= n == nums.length <= 105
0 <= nums[i] <= 105
"""

import string
import heapq
from typing import List
from collections import defaultdict

class Solution:
    def leetcode(self, nums: List[int]) -> int:
        result = 0
        q = [0]  # sentinel 0 to simplify logic

        for num in nums:
            # pop while the top > current num
            while q and q[-1] > num:
                q.pop()
            # if stack empty (shouldn't happen if sentinel) or top < num → new layer
            if not q or q[-1] < num:
                result += 1
                q.append(num)
            # else q[-1] == num → same layer, do nothing
        return result
        
        ### recursive, mle=954/968
        ll = len(nums)

        if ll == 1:
            if nums[0] > 0:
                return 1
            return 0

        result = 0
        min_num = min(nums)
        if min_num > 0:
            result += 1

        prev = 0
        for ii in range(ll):
            #print(ii, min_num, result)
            if nums[ii] == min_num:
                if ii == prev:
                    pass
                elif ii == prev+1:
                    result += 1
                else:
                    result += self.minOperations(nums[prev:ii])
                prev = ii+1
                #print(5, ii, prev,result)
            else:
                if ii == ll-1:
                    result += self.minOperations(nums[prev:ll])
                #print(6, ii, prev, result)

        return result
