"""
3216. Lexicographically Smallest String After a Swap
Easy
Topics
￼
Companies
Hint
Given a string s containing only digits, return the ￼lexicographically smallest string that can be obtained after swapping adjacent digits in s with the same parity at most once.

Digits have the same parity if both are odd or both are even. For example, 5 and 9, as well as 2 and 4, have the same parity, while 6 and 9 do not.

 

Example 1:

Input: s = "45320"

Output: "43520"

Explanation:

s[1] == '5' and s[2] == '3' both have the same parity, and swapping them results in the lexicographically smallest string.

Example 2:

Input: s = "001"

Output: "001"

Explanation:

There is no need to perform a swap because s is already the lexicographically smallest.

 

Constraints:

2 <= s.length <= 100
s consists only of digits.
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
    def leetcode(self, s: str) -> str:
        lists = list(s)
        ll = len(s)
        for ii in range(1, ll):
            if int(s[ii])%2 == int(s[ii-1])%2 and s[ii] < s[ii-1]:
                lists[ii], lists[ii-1] = lists[ii-1], lists[ii]
                break
        return "".join(lists)


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
