"""
2523. Closest Prime Numbers in Range
Medium
Topics
Companies
Hint
Given two positive integers left and right, find the two integers num1 and num2 such that:

left <= num1 < num2 <= right .
Both num1 and num2 are prime numbers.
num2 - num1 is the minimum amongst all other pairs satisfying the above conditions.
Return the positive integer array ans = [num1, num2]. If there are multiple pairs satisfying these conditions, return the one with the smallest num1 value. If no such numbers exist, return [-1, -1].

 

Example 1:

Input: left = 10, right = 19
Output: [11,13]
Explanation: The prime numbers between 10 and 19 are 11, 13, 17, and 19.
The closest gap between any pair is 2, which can be achieved by [11,13] or [17,19].
Since 11 is smaller than 17, we return the first pair.
Example 2:

Input: left = 4, right = 6
Output: [-1,-1]
Explanation: There exists only one prime number in the given range, so the conditions cannot be satisfied.
 

Constraints:

1 <= left <= right <= 106
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
    def closestPrimes(self, left: int, right: int) -> List[int]:
        # First, find all prime numbers in the range [left, right]
        def is_prime(n: int):
            if n <= 1:
                return False
            if n <= 3:
                return True
            if n%2 == 0 or n%3 == 0:
                return False
            index = 5
            while index**2 <= n:
                if n%index == 0 or n%(index+2) == 0:
                    return False
                index += 6
            return True
        
        primes = []
        for num in range(left, right+1):
            if is_prime(num):
                primes.append(num)
        #print(primes)

        ll = len(primes)
        result = [-1,-1]
        gap = right*2
        for ii in range(1, ll):
            if primes[ii]-primes[ii-1] < gap:
                result = [primes[ii-1], primes[ii]]
                gap = result[1]-result[0]
        return result


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
