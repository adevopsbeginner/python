"""
1671. Minimum Number of Removals to Make Mountain Array
Hard
Topics
Companies
Hint
You may recall that an array arr is a mountain array if and only if:

arr.length >= 3
There exists some index i (0-indexed) with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
Given an integer array nums​​​, return the minimum number of elements to remove to make nums​​​ a mountain array.

 

Example 1:

Input: nums = [1,3,1]
Output: 0
Explanation: The array itself is a mountain array so we do not need to remove any elements.
Example 2:

Input: nums = [2,1,1,5,6,2,3,1]
Output: 3
Explanation: One solution is to remove the elements at indices 0, 1, and 5, making the array nums = [1,5,6,3,1].
 

Constraints:

3 <= nums.length <= 1000
1 <= nums[i] <= 109
It is guaranteed that you can make a mountain array out of nums.
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
        ### chatgpt, hard
        n = len(nums)
    
        # Step 1: Calculate LIS from the left up to each index
        LIS = [1] * n
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    LIS[i] = max(LIS[i], LIS[j] + 1)
        
        # Step 2: Calculate LDS from the right up to each index
        LDS = [1] * n
        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                if nums[i] > nums[j]:
                    LDS[i] = max(LDS[i], LDS[j] + 1)
        
        # Step 3: Find the maximum length of a mountain array
        max_mountain_length = 0
        for i in range(1, n - 1):
            if LIS[i] > 1 and LDS[i] > 1:  # valid mountain peak
                max_mountain_length = max(max_mountain_length, LIS[i] + LDS[i] - 1)
        
        # Step 4: Minimum removals to make mountain array
        return n - max_mountain_length


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
