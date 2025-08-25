"""

Code
Testcase
Test Result
Test Result
Q1. Minimum Adjacent Swaps to Alternate Parity
Medium
4 pt.
You are given an array nums of distinct integers.

In one operation, you can swap any two adjacent elements in the array.

An arrangement of the array is considered valid if the parity of adjacent elements alternates, meaning every pair of neighboring elements consists of one even and one odd number.

Return the minimum number of adjacent swaps required to transform nums into any valid arrangement.

If it is impossible to rearrange nums such that no two adjacent elements have the same parity, return -1.

 

Example 1:

Input: nums = [2,4,6,5,7]

Output: 3

Explanation:

Swapping 5 and 6, the array becomes [2,4,5,6,7]

Swapping 5 and 4, the array becomes [2,5,4,6,7]

Swapping 6 and 7, the array becomes [2,5,4,7,6]. The array is now a valid arrangement. Thus, the answer is 3.

Example 2:

Input: nums = [2,4,5,7]

Output: 1

Explanation:

By swapping 4 and 5, the array becomes [2,5,4,7], which is a valid arrangement. Thus, the answer is 1.

Example 3:

Input: nums = [1,2,3]

Output: 0

Explanation:

The array is already a valid arrangement. Thus, no operations are needed.

Example 4:

Input: nums = [4,5,6,8]

Output: -1

Explanation:

No valid arrangement is possible. Thus, the answer is -1.

 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 109
All elements in nums are distinct.
"""

from typing import List
from collections import defaultdict

class Solution:
    def leetcode(self, nums: List[int]) -> int:
        n = len(nums)
        even_indices = [i for i, x in enumerate(nums) if x % 2 == 0]
        odd_indices = [i for i, x in enumerate(nums) if x % 2 == 1]

        if abs(len(even_indices) - len(odd_indices)) > 1:
            return -1

        def count_swaps(start_with_even):
            target_indices = []
            if start_with_even:
                even_target = list(range(0, n, 2))
                odd_target = list(range(1, n, 2))
            else:
                odd_target = list(range(0, n, 2))
                even_target = list(range(1, n, 2))

            if len(even_indices) != len(even_target) or len(odd_indices) != len(odd_target):
                return float('inf')  # Invalid configuration

            even_swaps = sum(abs(e - t) for e, t in zip(even_indices, even_target))
            odd_swaps = sum(abs(o - t) for o, t in zip(odd_indices, odd_target))
            return min(even_swaps, odd_swaps)
        
        # Try both starting with even and starting with odd
        return min(count_swaps(True), count_swaps(False))

if __name__ == "__main__":
    app = Solution()
    a = [1,4,3,3,2]
    b = 2
    print(app.leetcode(a))
