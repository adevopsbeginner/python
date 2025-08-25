"""
2429. Minimize XOR
Solved
Medium
Topics
Companies
Hint
Given two positive integers num1 and num2, find the positive integer x such that:

x has the same number of set bits as num2, and
The value x XOR num1 is minimal.
Note that XOR is the bitwise XOR operation.

Return the integer x. The test cases are generated such that x is uniquely determined.

The number of set bits of an integer is the number of 1's in its binary representation.

 

Example 1:

Input: num1 = 3, num2 = 5
Output: 3
Explanation:
The binary representations of num1 and num2 are 0011 and 0101, respectively.
The integer 3 has the same number of set bits as num2, and the value 3 XOR 3 = 0 is minimal.
Example 2:

Input: num1 = 1, num2 = 12
Output: 3
Explanation:
The binary representations of num1 and num2 are 0001 and 1100, respectively.
The integer 3 has the same number of set bits as num2, and the value 3 XOR 1 = 2 is minimal.
 

Constraints:

1 <= num1, num2 <= 109
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
    def leetcode(self, num1: int, num2: int) -> int:
        count1 = 0
        count2 = 0
        for ii in range(32):
            if num1 & (1<<ii) > 0:
                count1 += 1
            if num2 & (1<<ii) > 0:
                count2 += 1
        
        #print(count1, count2)
        if count1 < count2:
            count = count2-count1
            while count:
                for ii in range(32):
                    #print(ii)
                    if num1 & (1<<ii) == 0:
                        num1 |= (1<<ii)
                        break
                count -= 1
            return num1

        if count1 > count2:
            count = count1-count2
            while count:
                for ii in range(32):
                    if num1 & (1<<ii) > 0:
                        num1 ^= (1<<ii)
                        break
                count -= 1

            return num1

        return num1


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
