"""
Q2. Count Special Triplets
Medium
4 pt.
You are given an integer array nums.

A special triplet is defined as a triplet of indices (i, j, k) such that:

0 <= i < j < k < n, where n = nums.length
nums[i] == nums[j] * 2
nums[k] == nums[j] * 2
Return the total number of special triplets in the array.

Since the answer may be large, return it modulo 109 + 7.

 

Example 1:

Input: nums = [6,3,6]

Output: 1

Explanation:

The only special triplet is (i, j, k) = (0, 1, 2), where:

nums[0] = 6, nums[1] = 3, nums[2] = 6
nums[0] = nums[1] * 2 = 3 * 2 = 6
nums[2] = nums[1] * 2 = 3 * 2 = 6
Example 2:

Input: nums = [0,1,0,0]

Output: 1

Explanation:

The only special triplet is (i, j, k) = (0, 2, 3), where:

nums[0] = 0, nums[2] = 0, nums[3] = 0
nums[0] = nums[2] * 2 = 0 * 2 = 0
nums[3] = nums[2] * 2 = 0 * 2 = 0
Example 3:

Input: nums = [8,4,2,8,4]

Output: 2

Explanation:

There are exactly two special triplets:

(i, j, k) = (0, 1, 3)
nums[0] = 8, nums[1] = 4, nums[3] = 8
nums[0] = nums[1] * 2 = 4 * 2 = 8
nums[3] = nums[1] * 2 = 4 * 2 = 8
(i, j, k) = (1, 2, 4)
nums[1] = 4, nums[2] = 2, nums[4] = 4
nums[1] = nums[2] * 2 = 2 * 2 = 4
nums[4] = nums[2] * 2 = 2 * 2 = 4
 

Constraints:

3 <= n == nums.length <= 105
0 <= nums[i] <= 105
"""

from typing import List
from collections import defaultdict

class Solution:
    def leetcode(self, nums: List[int]) -> int:
        ll = len(nums)
        dd = defaultdict(int)
        for each in nums:
            dd[each] += 1
                
        result = 0
        if dd[0] > 2:
            result = (dd[0]-1)*(dd[0]-2)//2

        lastjj = 0
        for jj in range(1,ll-1):
            if nums[jj] == 0:
                continue
            if dd[2*nums[jj]] < 2:
                continue
            if nums[jj] == nums[jj-1]:
                result += lastjj
                continue
            count = 0
            for ii in range(jj):
                if nums[ii] == 2*nums[jj]:
                    count += 1
            #print(count)
            lastjj = count*(dd[2*nums[jj]] - count)
            result += lastjj
        
        # for ii in range(ll-2):
        #     if nums[ii] == 0:
        #         continue
        #     if nums[ii] % 2 > 0:
        #         continue
        #     for jj in range(ii+1, ll-1):
        #         if nums[jj] == 0:
        #             continue
        #         if nums[ii] == nums[jj] * 2:
        #             for kk in range(jj+1, ll):
        #                 if nums[kk] == 0:
        #                     continue
        #                 if nums[kk] == nums[ii]:
        #                     result += 1
        
        return result%1000000007

if __name__ == "__main__":
    app = Solution()
    a = [1,4,3,3,2]
    b = 2
    print(app.leetcode(a))
