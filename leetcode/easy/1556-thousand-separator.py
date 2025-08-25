"""
1556. Thousand Separator
Solved
Easy
Topics
Companies
Hint
Given an integer n, add a dot (".") as the thousands separator and return it in string format.

 

Example 1:

Input: n = 987
Output: "987"
Example 2:

Input: n = 1234
Output: "1.234"
 

Constraints:

0 <= n <= 231 - 1
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
    def leetcode(self, n: int) -> str:
        if n == 0:
            return "0"

        result = ""
        while n > 0:
            n1000 = n%1000
            result = str(n1000) + result
            n //= 1000
            if n > 0:
                if n1000 < 100:
                    result = "0" + result
                    if n1000 < 10:
                        result = "0" + result

                result = "." + result

        return result


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
