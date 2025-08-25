"""
1653. Minimum Deletions to Make String Balanced
Attempted
Medium
Topics
Companies
Hint
You are given a string s consisting only of characters 'a' and 'b'​​​​.

You can delete any number of characters in s to make s balanced. s is balanced if there is no pair of indices (i,j) such that i < j and s[i] = 'b' and s[j]= 'a'.

Return the minimum number of deletions needed to make s balanced.



Example 1:

Input: s = "aababbab"
Output: 2
Explanation: You can either:
Delete the characters at 0-indexed positions 2 and 6 ("aababbab" -> "aaabbb"), or
Delete the characters at 0-indexed positions 3 and 6 ("aababbab" -> "aabbbb").
Example 2:

Input: s = "bbaaaaabb"
Output: 2
Explanation: The only solution is to delete the first two characters.


Constraints:

1 <= s.length <= 105
s[i] is 'a' or 'b'​​.
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
        firstb = -1
        lasta = -1
        for ii in range(ll):
            if s[ii] == 'a':
                lasta = ii
            elif firstb < 0:
                firstb = ii

        if firstb < 0 or lasta < 0:
            return 0

        print(firstb,lasta)

        counta = 0
        for ii in range(firstb,lasta+1):
            if s[ii] == 'a':
                counta += 1
        result = min(counta, lasta+1-firstb-counta)

        countinga = 0
        countingb = 0
        for ii in range(firstb,lasta+1):
            if s[ii] == 'a':
                countinga += 1
            else:
                countingb += 1
            result = min(result,countingb+counta-countinga)

        return result


if __name__ == "__main__":
    app = Solution()
    a = "bbbbbbbaabbbbbaaabbbabbbbaabbbbbbaabbaaabaabbbaaaabaaababbbabbabbaaaabbbabbbbbaabbababbbaaaaaababaaababaabbabbbaaaabbbbbabbabaaaabbbaba"
    print(app.leetcode(a))
