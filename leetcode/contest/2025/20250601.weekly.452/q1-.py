"""
Q1. Partition Array into Two Equal Product Subsets
Medium
4 pt.
You are given an integer array nums containing distinct positive integers and an integer target.

Determine if you can partition nums into two non-empty disjoint subsets, with each element belonging to exactly one subset, such that the product of the elements in each subset is equal to target.

Return true if such a partition exists and false otherwise.

A subset of an array is a selection of elements of the array.
 

Example 1:

Input: nums = [3,1,6,8,4], target = 24

Output: true

Explanation: The subsets [3, 8] and [1, 6, 4] each have a product of 24. Hence, the output is true.

Example 2:

Input: nums = [2,5,3,7], target = 15

Output: false

Explanation: There is no way to partition nums into two non-empty disjoint subsets such that both subsets have a product of 15. Hence, the output is false.

 

Constraints:

3 <= nums.length <= 12
1 <= target <= 1015
1 <= nums[i] <= 100
All elements of nums are distinct.
"""

from typing import List
from collections import defaultdict

class Solution:
    def leetcode(self, nums: List[int], target: int) -> bool:
        ### bitmask
        product = 1
        for each in nums:
            product *= each
        if product != target*target:
            return False
        if target == 1:
            return True

        nums.sort()
        while nums[0] == 1:
            nums.pop(0)
        ll = len(nums)
        for ii in range(1, 2**ll-1):
            product = 1
            #print(ll, ii, product)
            for jj in range(ll):
                if ii & (1<<jj):
                    product *= nums[jj]
            if product == target:
                return True
        return False

if __name__ == "__main__":
    app = Solution()
    a = [1,4,3,3,2]
    b = 2
    print(app.leetcode(a))
