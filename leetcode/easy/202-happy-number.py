'''
202. Happy Number
Solved
Easy
Topics
Companies
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.

 

Example 1:

Input: n = 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
Example 2:

Input: n = 2
Output: false
 

Constraints:

1 <= n <= 231 - 1
'''

import string
from typing import List
from collections import defaultdict

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def leetcode(self, n: int) -> int:
        loop = []
        squaressum = 0
        while n not in loop:
            loop.append(n)
            while n:
                remainder = n % 10
                squaressum += remainder * remainder
                n //= 10
                # print(remainder,squaressum,n)
                
            if squaressum == 1:
                return True

            n = squaressum
            squaressum = 0
            # print(n,loop)

        return False

if __name__ == "__main__":
    app = Solution()
    a = 2
    print(app.leetcode(a))
