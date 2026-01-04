"""
1390. Four Divisors
Medium
Topics
premium lock icon
Companies
Hint
Given an integer array nums, return the sum of divisors of the integers in that array that have exactly four divisors. If there is no such integer in the array, return 0.

 

Example 1:

Input: nums = [21,4,7]
Output: 32
Explanation: 
21 has 4 divisors: 1, 3, 7, 21
4 has 3 divisors: 1, 2, 4
7 has 2 divisors: 1, 7
The answer is the sum of divisors of 21 only.
Example 2:

Input: nums = [21,21]
Output: 64
Example 3:

Input: nums = [1,2,3,4,5]
Output: 0
 

Constraints:

1 <= nums.length <= 104
1 <= nums[i] <= 105
"""

import string
import heapq
from typing import List
from collections import defaultdict

class Solution:
    def leetcode(self, nums: List[int]) -> int:
        def is_prime(num):
            if num <= 1:
                return False
            if num <= 3:
                return True
            if num%2 == 0:
                return False
            if num%3 == 0:
                return False

            i = 5
            while i*i <= num:
                if num%i == 0:
                    return False
                if num%(i+2) == 0:
                    return False
                i += 6

            return True
        
        #nums.sort()
        prime_nums = []
        for ii in range(max(nums)):
            if ii*ii > max(nums):
                break
            if is_prime(ii):
                prime_nums.append(ii)

        result = 0
        #print(prime_nums)
        ll = len(prime_nums)
        for num in nums:
            for ii in range(ll):
                #print(num,ii,prime_nums[ii])
                if prime_nums[ii]*prime_nums[ii] >= num:
                    break
                if prime_nums[ii]*prime_nums[ii]*prime_nums[ii] == num:
                    result += 1+prime_nums[ii]+prime_nums[ii]*prime_nums[ii]+num
                    break
                if num%prime_nums[ii] != 0:
                    continue
                
                prime2 = num//prime_nums[ii]
                #print(prime_nums[ii], prime2)
                if not is_prime(prime2):
                    continue

                result += 1+prime_nums[ii]+prime2+num
                break

        return result
