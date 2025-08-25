'''

Code
Testcase
Test Result
Test Result
217. Contains Duplicate
Solved
Easy
Topics
Companies
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
 

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
'''

import string
from typing import List
from collections import defaultdict

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def leetcode(self, nums: List[int]) -> bool:
        ll = len(nums)
        myset = set(nums)
        llset = len(myset)
        if ll == llset:
            return False
        else:
            return True

        nums.sort()
        for ii in range(ll-1):
            if nums[ii] in nums[ii+1:]:
                return True
        return False

if __name__ == "__main__":
    app = Solution()
    a = 2
    print(app.leetcode(a))
