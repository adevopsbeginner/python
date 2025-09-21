"""
2970. Count the Number of Incremovable Subarrays I
Easy
Topics
premium lock icon
Companies
Hint
You are given a 0-indexed array of positive integers nums.

A subarray of nums is called incremovable if nums becomes strictly increasing on removing the subarray. For example, the subarray [3, 4] is an incremovable subarray of [5, 3, 4, 6, 7] because removing this subarray changes the array [5, 3, 4, 6, 7] to [5, 6, 7] which is strictly increasing.

Return the total number of incremovable subarrays of nums.

Note that an empty array is considered strictly increasing.

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [1,2,3,4]
Output: 10
Explanation: The 10 incremovable subarrays are: [1], [2], [3], [4], [1,2], [2,3], [3,4], [1,2,3], [2,3,4], and [1,2,3,4], because on removing any one of these subarrays nums becomes strictly increasing. Note that you cannot select an empty subarray.
Example 2:

Input: nums = [6,5,7,8]
Output: 7
Explanation: The 7 incremovable subarrays are: [5], [6], [5,7], [6,5], [5,7,8], [6,5,7] and [6,5,7,8].
It can be shown that there are only 7 incremovable subarrays in nums.
Example 3:

Input: nums = [8,7,6,6]
Output: 3
Explanation: The 3 incremovable subarrays are: [8,7,6], [7,6,6], and [8,7,6,6]. Note that [8,7] is not an incremovable subarray because after removing [8,7] nums becomes [6,6], which is sorted in ascending order but not strictly increasing.
 

Constraints:

1 <= nums.length <= 50
1 <= nums[i] <= 50
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
        result = 0
        ll = len(nums)

        if ll == 1:
            return 1

        prefix_max = -1
        for ii in range(ll):
            increasing_flag = 1
            
            ### front subarray are increasing
            if ii > 0:
                if ii > 1:
                    if nums[ii-1] <= nums[ii-2]:
                        break
                prefix_max = nums[ii-1]

            result += 1

            ### behind subarray
            suffix_min = 51
            for jj in range(ll-1, ii, -1):
                if nums[jj] >= suffix_min:
                    increasing_flag = 0
                    break
                suffix_min = nums[jj]

                if prefix_max >= suffix_min:
                    increasing_flag = 0
                    break

                if increasing_flag:
                    #print(ii,jj, nums[ii:jj])
                    result += 1

        return result


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
