"""
387. First Unique Character in a String
Solved
Easy
Topics
Companies
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

 

Example 1:

Input: s = "leetcode"
Output: 0
Example 2:

Input: s = "loveleetcode"
Output: 2
Example 3:

Input: s = "aabb"
Output: -1
 

Constraints:

1 <= s.length <= 105
s consists of only lowercase English letters.
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
    def leetcode(self, ransomNote: str, magazine: str) -> bool:
        ddr = defaultdict(int)
        ddm = defaultdict(int)
        for each in ransomNote:
            ddr[each] += 1
        for each in magazine:
            ddm[each] += 1
        for each in ddr:
            if ddm[each] < ddr[each]:
                return False
        return True

if __name__ == "__main__":
    app = Solution()
    a = "hello"
    a = " "
    a = [4, 9, 5]
    b = [9, 4, 9, 8, 4]
    print(app.leetcode(a,b))
