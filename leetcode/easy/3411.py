"""
3411. Maximum Subarray With Equal Products
Easy
Topics
premium lock icon
Companies
Hint
You are given an array of positive integers nums.

An array arr is called product equivalent if prod(arr) == lcm(arr) * gcd(arr), where:

prod(arr) is the product of all elements of arr.
gcd(arr) is the GCD of all elements of arr.
lcm(arr) is the LCM of all elements of arr.
Return the length of the longest product equivalent subarray of nums.

 

Example 1:

Input: nums = [1,2,1,2,1,1,1]

Output: 5

Explanation: 

The longest product equivalent subarray is [1, 2, 1, 1, 1], where prod([1, 2, 1, 1, 1]) = 2, gcd([1, 2, 1, 1, 1]) = 1, and lcm([1, 2, 1, 1, 1]) = 2.

Example 2:

Input: nums = [2,3,4,5,6]

Output: 3

Explanation: 

The longest product equivalent subarray is [3, 4, 5].

Example 3:

Input: nums = [1,2,3,1,4,5,1]

Output: 5

 

Constraints:

2 <= nums.length <= 100
1 <= nums[i] <= 10
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
        def gcd(nums):
            result = 1
            for ii in range(1,min(10, min(nums))+1):
                flag = 0
                for num in nums:
                    if num%ii > 0:
                        flag = 1
                        break
                if flag == 1:
                    continue
                result = max(result,ii)

            return result

        def lcm(nums):
            result = max(nums)

            while True:
                no_flag = 0
                for num in nums:
                    if result%num > 0:
                        no_flag = 1
                        break
                if no_flag == 0:
                    break
                result += 1

            return result

        ll = len(nums)
        result = 1
        for ii in range(ll):
            product = nums[ii]
            for jj in range(ii+1,ll):
                product *= nums[jj]
                if product > 1*2*3*4*5*6*7*8*9*10*10:
                    break
                if product == gcd(nums[ii:jj+1])*lcm(nums[ii:jj+1]):
                    result = max(result, jj-ii+1)

        return result


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
