"""
696. Count Binary Substrings
Easy
Topics
Companies
Hint
Given a binary string s, return the number of non-empty substrings that have the same number of 0's and 1's, and all the 0's and all the 1's in these substrings are grouped consecutively.

Substrings that occur multiple times are counted the number of times they occur.



Example 1:

Input: s = "00110011"
Output: 6
Explanation: There are 6 substrings that have equal number of consecutive 1's and 0's: "0011", "01", "1100", "10", "0011", and "01".
Notice that some of these substrings repeat and are counted the number of times they occur.
Also, "00110011" is not a valid substring because all the 0's (and 1's) are not grouped together.
Example 2:

Input: s = "10101"
Output: 4
Explanation: There are 4 substrings: "10", "01", "10", "01" that have equal number of consecutive 1's and 0's.


Constraints:

1 <= s.length <= 105
s[i] is either '0' or '1'.
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
    def leetcode(self, s: str) -> int:
        ll = len(s)
        count0 = 0
        count1 = 0
        if s[0] == "0":
            count0 = 1
        else:
            count1 = 1

        result = 0
        for ii in range(1,ll):
            if s[ii] == s[ii-1]:
                if s[ii] == "0":
                    count0 += 1
                else:
                    count1 += 1
            else:
                result += min(count0, count1)
                if s[ii] == "0":
                    count0 = 1
                else:
                    count1 = 1
        result += min(count0, count1)

        return result


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
