"""
1248. Count Number of Nice Subarrays
Medium
Topics
Companies
Hint
Given an array of integers nums and an integer k. A continuous subarray is called nice if there are k odd numbers on it.

Return the number of nice sub-arrays.

 

Example 1:

Input: nums = [1,1,2,1,1], k = 3
Output: 2
Explanation: The only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].
Example 2:

Input: nums = [2,4,6], k = 1
Output: 0
Explanation: There are no odd numbers in the array.
Example 3:

Input: nums = [2,2,2,1,2,2,1,2,2,2], k = 2
Output: 16
 

Constraints:

1 <= nums.length <= 50000
1 <= nums[i] <= 10^5
1 <= k <= nums.length
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
        def atMost(k):
            count = 0
            left = 0
            odd_count = 0
            
            for right in range(len(nums)):
                if nums[right] % 2 == 1:
                    odd_count += 1
                
                while odd_count > k:
                    if nums[left] % 2 == 1:
                        odd_count -= 1
                    left += 1
                
                count += right - left + 1
            
            return count
        return atMost(k) - atMost(k - 1)

if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    a = [0,2,2]
    #a = [3,2,1,2,1,7]
    b = [5]
    k = 2
    w = 0
    profits = [1,2,3]
    capital = [0,1,2]
    print(app.leetcode(k,w,profits,capital))
