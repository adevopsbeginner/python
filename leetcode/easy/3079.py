"""
3079. Find the Sum of Encrypted Integers
Easy
Topics
premium lock icon
Companies
Hint
You are given an integer array nums containing positive integers. We define a function encrypt such that encrypt(x) replaces every digit in x with the largest digit in x. For example, encrypt(523) = 555 and encrypt(213) = 333.

Return the sum of encrypted elements.

 

Example 1:

Input: nums = [1,2,3]

Output: 6

Explanation: The encrypted elements are [1,2,3]. The sum of encrypted elements is 1 + 2 + 3 == 6.

Example 2:

Input: nums = [10,21,31]

Output: 66

Explanation: The encrypted elements are [11,22,33]. The sum of encrypted elements is 11 + 22 + 33 == 66.

 

Constraints:

1 <= nums.length <= 50
1 <= nums[i] <= 1000
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
        def encrypt(num):
            listnum = list(str(num))
            ll = len(listnum)
            for ii in range(ll):
                listnum[ii] = int(listnum[ii])
            maxdigit = max(listnum)
            result = 0
            for ii in range(ll):
                result = result*10+maxdigit

            return result
        
        ll = len(nums)
        for ii in range(ll):
            nums[ii] = encrypt(nums[ii])
        return sum(nums)


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
