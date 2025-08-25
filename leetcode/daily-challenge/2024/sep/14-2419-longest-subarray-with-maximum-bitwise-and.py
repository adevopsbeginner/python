"""
2419. Longest Subarray With Maximum Bitwise AND
Medium
Topics
Companies
Hint
You are given an integer array nums of size n.

Consider a non-empty subarray from nums that has the maximum possible bitwise AND.

In other words, let k be the maximum value of the bitwise AND of any subarray of nums. Then, only subarrays with a bitwise AND equal to k should be considered.
Return the length of the longest such subarray.

The bitwise AND of an array is the bitwise AND of all the numbers in it.

A subarray is a contiguous sequence of elements within an array.



Example 1:

Input: nums = [1,2,3,3,2,2]
Output: 2
Explanation:
The maximum possible bitwise AND of a subarray is 3.
The longest subarray with that value is [3,3], so we return 2.
Example 2:

Input: nums = [1,2,3,4]
Output: 1
Explanation:
The maximum possible bitwise AND of a subarray is 4.
The longest subarray with that value is [4], so we return 1.


Constraints:

1 <= nums.length <= 105
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
        ll = len(nums)
        maxnum = max(nums)

        result = 0
        start = -1
        end = -1
        for ii in range(ll):
            if nums[ii] == maxnum:
                end = ii
                if start < 0:
                    start = ii
            else:
                if end >= 0:
                    result = max(result, end-start+1)
                start = -1
                end = -1
        if end >= 0:
            result = max(result, end-start+1)

        return result


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
