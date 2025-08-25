"""
693. Binary Number with Alternating Bits
Easy
Topics
Companies
Given a positive integer, check whether it has alternating bits: namely, if two adjacent bits will always have different values.



Example 1:

Input: n = 5
Output: true
Explanation: The binary representation of 5 is: 101
Example 2:

Input: n = 7
Output: false
Explanation: The binary representation of 7 is: 111.
Example 3:

Input: n = 11
Output: false
Explanation: The binary representation of 11 is: 1011.


Constraints:

1 <= n <= 231 - 1
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
    def leetcode(self, n: int) -> bool:
        first1flag = 0
        for ii in range(31,-1,-1):
            if first1flag:
                if ii == 31:
                    continue
                if (n&(1<<ii))<<1 == n&(1<<(ii+1)):
                    return False

            if n&(1<<ii):
                first1flag = 1

        return True


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
