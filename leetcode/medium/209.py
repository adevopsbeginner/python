"""
209. Minimum Size Subarray Sum
Medium
Topics
￼
Companies
Given an array of positive integers nums and a positive integer target, return the minimal length of a ￼subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

 

Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1
Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
 

Constraints:

1 <= target <= 109
1 <= nums.length <= 105
1 <= nums[i] <= 104
 

Follow up: If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log(n)).
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
    def leetcode(self, target: int, nums: List[int]) -> int:
        if max(nums) >= target:
            return 1
        if sum(nums) < target:
            return 0

        ll = len(nums)
        result = ll
        left = 0
        right = 0
        subsum = nums[0]

        while left < ll:
            #print(left,right, subsum, result)
            if subsum < target:
                if right >= ll-1:
                    break
                right += 1
                subsum += nums[right]
            else:
                if left >= right:
                    break
                subsum -= nums[left]
                left += 1

            if subsum >= target:
                result = min(result, right-left+1)

        return result


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
