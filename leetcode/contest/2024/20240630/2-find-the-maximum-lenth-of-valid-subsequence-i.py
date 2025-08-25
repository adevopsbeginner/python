"""
100357. Find the Maximum Length of Valid Subsequence I
User Accepted:3580
User Tried:6656
Total Accepted:3628
Total Submissions:10996
Difficulty:Medium
You are given an integer array nums.
A subsequence sub of nums with length x is called valid if it satisfies:

(sub[0] + sub[1]) % 2 == (sub[1] + sub[2]) % 2 == ... == (sub[x - 2] + sub[x - 1]) % 2.
Return the length of the longest valid subsequence of nums.

A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.



Example 1:

Input: nums = [1,2,3,4]

Output: 4

Explanation:

The longest valid subsequence is [1, 2, 3, 4].

Example 2:

Input: nums = [1,2,1,1,2,1,2]

Output: 6

Explanation:

The longest valid subsequence is [1, 2, 1, 2, 1, 2].

Example 3:

Input: nums = [1,3]

Output: 2

Explanation:

The longest valid subsequence is [1, 3].



Constraints:

2 <= nums.length <= 2 * 105
1 <= nums[i] <= 107
"""

from typing import List
from collections import defaultdict

class Solution:
    def leetcode(self, nums: List[int]) -> int:
        ll = len(nums)
        result = 0
        for ii in range(ll):
            nums[ii] &= 1
        all1 = sum(nums)
        max00 = 0
        now00 = 0
        max01 = 0
        now01 = 0
        max11 = 0
        now11 = 0
        for ii in range(ll):
            if nums[ii] == 0:
                now00 += 1
                max00 = max(max00,now00)

                now11 = 0

                if ii and nums[ii-1] == 0:
                    now01 = 0
                else:
                    now01 += 1
                    max01 = max(max01, now01)
            else:
                now00 = 0

                now11 += 1
                max11 = max(max11, now11)

                if ii and nums[ii-1] == 1:
                    now01 = 0
                else:
                    now01 += 1
                    max01 = max(max01, now01)

        result = max(max00,max01,max11)
        if result <= 1:
            return 0
        return result

if __name__ == "__main__":
    app = Solution()
    a = [1,4,3,3,2]
    b = 2
    print(app.leetcode(a))
