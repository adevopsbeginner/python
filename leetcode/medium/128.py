"""
128. Longest Consecutive Sequence
Medium
Topics
premium lock icon
Companies
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
Example 3:

Input: nums = [1,0,1,2]
Output: 3
 

Constraints:

0 <= nums.length <= 105
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
        ### hash set
        num_set = set(nums)
        result = 0
        for num in num_set:
            if num-1 in num_set:
                continue
            increase = 1
            while num+increase in num_set:
                increase += 1
            result = max(result, increase)
        return result

        ### sorting, O(nlogn)
        ll = len(nums)
        if ll == 0:
            return 0
        nums.sort()
        result = 0
        current = 1
        for ii in range(1,ll):
            if nums[ii] == nums[ii-1]:
                continue
            elif nums[ii] == nums[ii-1]+1:
                current += 1
            else:
                result = max(result, current)
                current = 1
        result = max(result, current)

        return result


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
