"""
976. Largest Perimeter Triangle
Easy
Topics
Companies
Given an integer array nums, return the largest perimeter of a triangle with a non-zero area, formed from three of these lengths. If it is impossible to form any triangle of a non-zero area, return 0.



Example 1:

Input: nums = [2,1,2]
Output: 5
Explanation: You can form a triangle with three side lengths: 1, 2, and 2.
Example 2:

Input: nums = [1,2,1,10]
Output: 0
Explanation:
You cannot use the side lengths 1, 1, and 2 to form a triangle.
You cannot use the side lengths 1, 1, and 10 to form a triangle.
You cannot use the side lengths 1, 2, and 10 to form a triangle.
As we cannot use any three side lengths to form a triangle of non-zero area, we return 0.


Constraints:

3 <= nums.length <= 104
1 <= nums[i] <= 106
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
        nums.sort(reverse=True)
        # print(nums)
        for ii in range(ll - 2):
            if nums[ii] * 3 < result:
                break
            for jj in range(ii + 1, ll - 1):
                if nums[jj] * 2 < nums[ii]:
                    break
                if (nums[ii] + nums[jj]) * 2 < result:
                    break
                for kk in range(jj + 1, ll):
                    if nums[ii] < nums[jj] + nums[kk]:
                        # print(ii,jj,kk,nums[ii], nums[jj], nums[kk], result, nums[ii] + nums[jj] + nums[kk])
                        result = max(result, nums[ii] + nums[jj] + nums[kk])
                        break

        return result


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
