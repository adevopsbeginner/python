"""
Q3. Reach End of Array With Max Score
Medium
5 pt.
You are given an integer array nums of length n.

Your goal is to start at index 0 and reach index n - 1. You can only jump to indices greater than your current index.

The score for a jump from index i to index j is calculated as (j - i) * nums[i].

Return the maximum possible total score by the time you reach the last index.



Example 1:

Input: nums = [1,3,1,5]

Output: 7

Explanation:

First, jump to index 1 and then jump to the last index. The final score is 1 * 1 + 2 * 3 = 7.

Example 2:

Input: nums = [4,3,1,3,2]

Output: 16

Explanation:

Jump directly to the last index. The final score is 4 * 4 = 16.



Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 105
"""

from typing import List
from collections import defaultdict

class Solution:
    def leetcode(self, nums: List[int]) -> int:
        ll = len(nums)
        result = 0
        iwas = 0
        imax = nums[0]
        nums[-1] = max(nums)+1
        for ii in range(1,ll):
            if nums[ii] > imax:
                result += (ii-iwas)*imax
                imax = nums[ii]
                iwas = ii

        return result

if __name__ == "__main__":
    app = Solution()
    a = [1,4,3,3,2]
    b = 2
    print(app.leetcode(a))
