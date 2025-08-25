"""
448. Find All Numbers Disappeared in an Array
Easy
Topics
Companies
Hint
Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.



Example 1:

Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]
Example 2:

Input: nums = [1,1]
Output: [2]


Constraints:

n == nums.length
1 <= n <= 105
1 <= nums[i] <= n


Follow up: Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.
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
    def leetcode(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = []
        nums.sort()

        index = 0
        for ii in range(1,n+1):
            if index == n:
                for jj in range(ii,n+1):
                    result.append(jj)
                return result

            if nums[index] == ii:
                index += 1
            elif nums[index] < ii:
                # print(ii, index, nums[index], nums)
                while nums[index] < ii:
                    if index == n-1:
                        for jj in range(ii,n+1):
                            result.append(jj)
                        return result
                    index += 1
                    if nums[index] > ii:
                        result.append(ii)
            else:
                result.append(ii)

        return result

if __name__ == "__main__":
    app = Solution()
    a = "hello"
    a = " "
    a = [4, 9, 5]
    b = [9, 4, 9, 8, 4]
    a = [4,3,2,7,8,2,3,1]
    print(app.leetcode(a))
