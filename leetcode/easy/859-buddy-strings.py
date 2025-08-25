"""
859. Buddy Strings
Solved
Easy
Topics
Companies
Given two strings s and goal, return true if you can swap two letters in s so the result is equal to goal, otherwise, return false.

Swapping letters is defined as taking two indices i and j (0-indexed) such that i != j and swapping the characters at s[i] and s[j].

For example, swapping at indices 0 and 2 in "abcd" results in "cbad".


Example 1:

Input: s = "ab", goal = "ba"
Output: true
Explanation: You can swap s[0] = 'a' and s[1] = 'b' to get "ba", which is equal to goal.
Example 2:

Input: s = "ab", goal = "ab"
Output: false
Explanation: The only letters you can swap are s[0] = 'a' and s[1] = 'b', which results in "ba" != goal.
Example 3:

Input: s = "aa", goal = "aa"
Output: true
Explanation: You can swap s[0] = 'a' and s[1] = 'a' to get "aa", which is equal to goal.


Constraints:

1 <= s.length, goal.length <= 2 * 104
s and goal consist of lowercase letters.
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
    def leetcode(self, s: str, goal: str) -> bool:
        t= goal
        lls = len(s)
        llt = len(t)

        if lls-llt:
            return False
        if lls == 1:
            return False

        count = 0
        dds = defaultdict(int)
        firsts = -1
        firstt = -1
        count2flag = 0
        for ii in range(lls):
            dds[s[ii]] += 1
            if s[ii] != t[ii]:
                count += 1

                if count == 1:
                    firsts = ii
                    firstt = ii
                elif count == 2:
                    if s[firsts] == t[ii] and t[firstt] == s[ii]:
                        count2flag = 1
                else:
                    return False


        if count == 0:
            for each in dds:
                if dds[each] >= 2:
                    return True
        elif count == 2:
            if count2flag:
                return True

        return False


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
