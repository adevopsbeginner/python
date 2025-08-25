"""
717. 1-bit and 2-bit Characters
Easy
Topics
Companies
Hint
We have two special characters:

The first character can be represented by one bit 0.
The second character can be represented by two bits (10 or 11).
Given a binary array bits that ends with 0, return true if the last character must be a one-bit character.



Example 1:

Input: bits = [1,0,0]
Output: true
Explanation: The only way to decode it is two-bit character and one-bit character.
So the last character is one-bit character.
Example 2:

Input: bits = [1,1,1,0]
Output: false
Explanation: The only way to decode it is two-bit character and two-bit character.
So the last character is not one-bit character.


Constraints:

1 <= bits.length <= 1000
bits[i] is either 0 or 1.
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
    def leetcode(self, bits: List[int]) -> bool:
        ll = len(bits)

        if bits[-1] == 1:
            return False

        if ll == 1:
            return True

        for ii in range(ll-2,-1,-1):
            if bits[ii] == 0:
                sum1 = sum(bits[ii:])
                print(ii,sum1)
                if sum1 % 2 == 1:
                    return False
                return True

        if sum(bits) % 2 == 1:
            return False
        return True


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
