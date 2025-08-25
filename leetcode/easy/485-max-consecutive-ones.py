"""
485. Max Consecutive Ones
Easy
Topics
Companies
Hint
Given a binary array nums, return the maximum number of consecutive 1's in the array.



Example 1:

Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
Example 2:

Input: nums = [1,0,1,1,0,1]
Output: 2


Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
"""

import string
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
        maxnow = 0
        for each in nums:
            if each:
                maxnow += 1
            else:
                result = max(result, maxnow)
                maxnow = 0
        result = max(result, maxnow)
        return result

if __name__ == "__main__":
    app = Solution()
    a = 5
    b = [[1,2]]
    print(app.leetcode(a,b))
