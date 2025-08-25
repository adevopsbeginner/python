'''

Code
Testcase
Test Result
Test Result
168. Excel Sheet Column Title
Solved
Easy
Topics
Companies
Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.

For example:

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
...
 

Example 1:

Input: columnNumber = 1
Output: "A"
Example 2:

Input: columnNumber = 28
Output: "AB"
Example 3:

Input: columnNumber = 701
Output: "ZY"
 

Constraints:

1 <= columnNumber <= 231 - 1
'''

import string
from typing import List
from collections import defaultdict

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def leetcode(self, columnNumber: int) -> str:
        result = ""
        level = 26
        capital_letters = list(string.ascii_uppercase)

        while level < columnNumber:
            columnNumber -= level
            level *= 26

        while level > 26:
            level //= 26
            n = columnNumber // level
            columnNumber %= level
            if n == 0 and columnNumber == 0:
                result += 'Z'
            elif columnNumber == 0:
                result += capital_letters[n-1]
            elif n == 0:
                result += 'A'
            else:
                result += capital_letters[n]

        if columnNumber == 0:
            result += 'Z'
        else:
            result += capital_letters[columnNumber-1]

        return result

if __name__ == "__main__":
    app = Solution()
    a = [1,1,2,3,3]
    a = 701
    print(app.leetcode(a))
