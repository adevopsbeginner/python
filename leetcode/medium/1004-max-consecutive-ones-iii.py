"""
1004. Max Consecutive Ones III
Medium
Topics
Companies
Hint
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

 

Example 1:

Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
Example 2:

Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
 

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
0 <= k <= nums.length
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
    def leetcode(self, nums: List[int], k: int) -> int:
        count0 = 0
        result = k
        ll = len(nums)
        if ll-sum(nums) <= k:
            return ll

        ### two pointers
        index1 = 0
        index2 = 0
        while index1 < ll and index2 < ll:
            ### count 0 until the number of 0 grater than k
            if nums[index2] == 0:
                count0 += 1
            if count0 > k:
                result = max(result, index2-index1)
                while index1 < index2 and nums[index1] == 1:
                    index1 += 1
                index1 += 1
                count0 -= 1
            index2 += 1

        result = max(result, index2-index1)

        return result


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
