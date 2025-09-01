"""
1318. Minimum Flips to Make a OR b Equal to c
Medium
Topics
premium lock icon
Companies
Hint
Given 3 positives numbers a, b and c. Return the minimum flips required in some bits of a and b to make ( a OR b == c ). (bitwise OR operation).
Flip operation consists of change any single bit 1 to 0 or change the bit 0 to 1 in their binary representation.

 

Example 1:



Input: a = 2, b = 6, c = 5
Output: 3
Explanation: After flips a = 1 , b = 4 , c = 5 such that (a OR b == c)
Example 2:

Input: a = 4, b = 2, c = 7
Output: 1
Example 3:

Input: a = 1, b = 2, c = 3
Output: 0
 

Constraints:

1 <= a <= 10^9
1 <= b <= 10^9
1 <= c <= 10^9
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
    def leetcode(self, a: int, b: int, c: int) -> int:
        result = 0
        for ii in range(32):
            abit = a&(1<<ii)
            bbit = b&(1<<ii)
            cbit = c&(1<<ii)

            if cbit > 0:
                if abit == 0 and bbit == 0:
                    result += 1
            else:
                if abit == 0 and bbit > 0:
                    result += 1
                elif abit > 0 and bbit == 0:
                    result += 1
                elif abit > 0 and bbit > 0:
                    result += 2
        
        return result


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
