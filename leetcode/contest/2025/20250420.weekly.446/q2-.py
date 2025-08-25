"""
Q2. Make Array Non-decreasing
Medium
4 pt.
You are given an integer array nums. In one operation, you can select a subarray and replace it with a single element equal to its maximum value.

Return the maximum possible size of the array after performing zero or more operations such that the resulting array is non-decreasing.

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [4,2,5,3,5]

Output: 3

Explanation:

One way to achieve the maximum size is:

Replace subarray nums[1..2] = [2, 5] with 5 → [4, 5, 3, 5].
Replace subarray nums[2..3] = [3, 5] with 5 → [4, 5, 5].
The final array [4, 5, 5] is non-decreasing with size 3.

Example 2:

Input: nums = [1,2,3]

Output: 3

Explanation:

No operation is needed as the array [1,2,3] is already non-decreasing.

 

Constraints:

1 <= nums.length <= 2 * 105
1 <= nums[i] <= 2 * 105
"""

from typing import List
from collections import defaultdict

class Solution:
    def leetcode(self, nums: List[int]) -> int:
        result = 1
        ll = len(nums)
        peak = nums[0]
        for ii in range(1,ll):
            if nums[ii] < peak:
                continue
            peak = nums[ii]
            result += 1
        return result

if __name__ == "__main__":
    app = Solution()
    a = [1,4,3,3,2]
    b = 2
    print(app.leetcode(a))
