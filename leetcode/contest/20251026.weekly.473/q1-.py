"""
Q1. Remove Zeros in Decimal Representation
Easy
3 pt.
You are given a positive integer n.

Return the integer obtained by removing all zeros from the decimal representation of n.

 

Example 1:

Input: n = 1020030

Output: 123

Explanation:

After removing all zeros from 1020030, we get 123.

Example 2:

Input: n = 1

Output: 1

Explanation:

1 has no zero in its decimal representation. Therefore, the answer is 1.

 

Constraints:

1 <= n <= 1015
"""

from typing import List
from collections import defaultdict

class Solution:
    def leetcode(self, n: int) -> int:
        result = ""
        for c in str(n):
            if c != "0":
                result += c

        return int(result)
