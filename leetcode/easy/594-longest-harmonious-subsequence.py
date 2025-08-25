"""
594. Longest Harmonious Subsequence
Solved
Easy
Topics
Companies
We define a harmonious array as an array where the difference between its maximum value and its minimum value is exactly 1.

Given an integer array nums, return the length of its longest harmonious subsequence among all its possible subsequences.

A subsequence of array is a sequence that can be derived from the array by deleting some or no elements without changing the order of the remaining elements.



Example 1:

Input: nums = [1,3,2,2,5,2,3,7]
Output: 5
Explanation: The longest harmonious subsequence is [3,2,2,2,3].
Example 2:

Input: nums = [1,2,3,4]
Output: 2
Example 3:

Input: nums = [1,1,1,1]
Output: 0


Constraints:

1 <= nums.length <= 2 * 104
-109 <= nums[i] <= 109
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
        dd = defaultdict(int)
        for each in nums:
            dd[each] += 1

        result = 0
        for each in dd:
            eachm1 = 0
            eacha1 = 0
            if each-1 in dd or each+1 in dd:
                if each-1 in dd:
                    eachm1= dd[each-1]
                    result = max(result, dd[each]+eachm1)
                if each+1 in dd:
                    eacha1= dd[each+1]
                    result = max(result, dd[each]+eacha1)

        return result


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
