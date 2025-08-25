"""
342. Power of Four
Solved
Easy
Topics
Companies
Given an integer n, return true if it is a power of four. Otherwise, return false.

An integer n is a power of four, if there exists an integer x such that n == 4x.



Example 1:

Input: n = 16
Output: true
Example 2:

Input: n = 5
Output: false
Example 3:

Input: n = 1
Output: true


Constraints:

-2^31 <= n <= 2^31 - 1


Follow up: Could you solve it without loops/recursion?
"""

import string
from typing import List
from collections import defaultdict

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def leetcode(self, n: int) -> bool:
        for ii in range(16):
            if n == 1 << (2 * ii):
                return True
        return False

        if n in [1, 4, 16, 64, 256, 1024, 4096, 16384, 65536, 262144, 1048576, 4194304, 16777216, 67108864, 268435456,
                 1073741824, 4294967296]:
            return True
        return False


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)

if __name__ == "__main__":
    app = Solution()
    a = 25
    print(app.leetcode(a))
