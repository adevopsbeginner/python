"""
409. Longest Palindrome
Solved
Easy
Topics
Companies
Given a string s which consists of lowercase or uppercase letters, return the length of the longest
palindrome
 that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome.



Example 1:

Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.
Example 2:

Input: s = "a"
Output: 1
Explanation: The longest palindrome that can be built is "a", whose length is 1.


Constraints:

1 <= s.length <= 2000
s consists of lowercase and/or uppercase English letters only.
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
    def leetcode(self, s: str) -> int:
        result = 0
        ll = len(s)
        dd = defaultdict(int)
        flag = 0
        for each in s:
            dd[each] += 1
        for each in dd:
            result += (dd[each] >> 1) << 1
            if dd[each]%2:
                flag = 1
        return result+flag

if __name__ == "__main__":
    app = Solution()
    a = "coaching"
    b = "coding"
    a = "abcde"
    b = "a"
    a = "z"
    b = "abcde"
    a = "a"
    b = "a"
    print(app.leetcode(a,b))
