"""
258. Add Digits
Solved
Easy
Topics
Companies
Hint
Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

 

Example 1:

Input: num = 38
Output: 2
Explanation: The process is
38 --> 3 + 8 --> 11
11 --> 1 + 1 --> 2 
Since 2 has only one digit, return it.
Example 2:

Input: num = 0
Output: 0
 

Constraints:

0 <= num <= 231 - 1
 

Follow up: Could you do it without any loop/recursion in O(1) runtime?
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
    def leetcode(self, num: int) -> int:
        result = num
        while result > 9:
            a = f"{result}"
            b = [x for x in a]
            result = sum([int(x) for x in b])
            #print(result, a, b)

        return result

if __name__ == "__main__":
    app = Solution()
    a = 38
    print(app.leetcode(a))
