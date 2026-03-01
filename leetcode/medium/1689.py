"""
1689. Partitioning Into Minimum Number Of Deci-Binary Numbers
Solved
Medium
Topics
premium lock icon
Companies
Hint
A decimal number is called deci-binary if each of its digits is either 0 or 1 without any leading zeros. For example, 101 and 1100 are deci-binary, while 112 and 3001 are not.

Given a string n that represents a positive decimal integer, return the minimum number of positive deci-binary numbers needed so that they sum up to n.

 

Example 1:

Input: n = "32"
Output: 3
Explanation: 10 + 11 + 11 = 32
Example 2:

Input: n = "82734"
Output: 8
Example 3:

Input: n = "27346209830709182346"
Output: 9
 

Constraints:

1 <= n.length <= 105
n consists of only digits.
n does not contain any leading zeros and represents a positive integer.
"""

import string
import heapq
from typing import List
from collections import defaultdict

class Solution:
    def leetcode(self, n: str) -> int:
        n: str) -> int:
        for num in "987654321":
            if num in str(n):
                return int(num)

        digit = []
        for each in n:
            digit.append(each)
        #digit = n.split('')
        digit.sort()
        return int(digit[-1])

        x = 0
        while n:
            x = max(x,int(n)%10)
            n //= 10
        return x
        
        d = [987654321]
        s = "{}".format(n)
        for ii in range(9):
            if d[ii] in s:
                return d[ii]
