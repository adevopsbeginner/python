"""
Q1. Smallest Number With All Set Bits
Easy
3 pt.
You are given a positive number n.

Return the smallest number x greater than or equal to n, such that the binary representation of x contains only set bits.

A set bit refers to a bit in the binary representation of a number that has a value of 1.

 

Example 1:

Input: n = 5

Output: 7

Explanation:

The binary representation of 7 is "111".

Example 2:

Input: n = 10

Output: 15

Explanation:

The binary representation of 15 is "1111".

Example 3:

Input: n = 3

Output: 3

Explanation:

The binary representation of 3 is "11".

 

Constraints:

1 <= n <= 1000
"""

from typing import List
from collections import defaultdict

class Solution:
    def leetcode(self, n: int) -> int:
        for ii in range(1,32):
            if 1<<ii > n:
                return (1<<ii)-1

        return n

if __name__ == "__main__":
    app = Solution()
    a = [1,4,3,3,2]
    b = 2
    print(app.leetcode(a))
