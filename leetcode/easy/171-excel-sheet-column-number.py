'''
171. Excel Sheet Column Number
Solved
Easy
Topics
Companies
Given a string columnTitle that represents the column title as appears in an Excel sheet, return its corresponding column number.

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

Input: columnTitle = "A"
Output: 1
Example 2:

Input: columnTitle = "AB"
Output: 28
Example 3:

Input: columnTitle = "ZY"
Output: 701
 

Constraints:

1 <= columnTitle.length <= 7
columnTitle consists only of uppercase English letters.
columnTitle is in the range ["A", "FXSHRXW"].
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
    def leetcode(self, columnTitle: str) -> int:
        result = 0
        ll = len(columnTitle)
        c7 = [1,26, 26*26, 26*26*26, 26*26*26*26, 26*26*26*26*26, 26*26*26*26*26*26, 26*26*26*26*26*26*26]

        for ii in range(ll):
            result += c7[ii]

        alphabet_dict = {chr(i): i - 65 for i in range(65, 91)}
        high = 0
        for ii in range(ll):
            high *= 26
            # print(columnTitle[ii])
            high += alphabet_dict[columnTitle[ii]]
            # print(high)

        return result+high

if __name__ == "__main__":
    app = Solution()
    a = 'AAA'
    print(app.leetcode(a))
