"""
1763. Longest Nice Substring
Easy
Topics
Companies
Hint
A string s is nice if, for every letter of the alphabet that s contains, it appears both in uppercase and lowercase. For example, "abABB" is nice because 'A' and 'a' appear, and 'B' and 'b' appear. However, "abA" is not because 'b' appears, but 'B' does not.

Given a string s, return the longest substring of s that is nice. If there are multiple, return the substring of the earliest occurrence. If there are none, return an empty string.

 

Example 1:

Input: s = "YazaAay"
Output: "aAa"
Explanation: "aAa" is a nice string because 'A/a' is the only letter of the alphabet in s, and both 'A' and 'a' appear.
"aAa" is the longest nice substring.
Example 2:

Input: s = "Bb"
Output: "Bb"
Explanation: "Bb" is a nice string because both 'B' and 'b' appear. The whole string is a substring.
Example 3:

Input: s = "c"
Output: ""
Explanation: There are no nice substrings.
 

Constraints:

1 <= s.length <= 100
s consists of uppercase and lowercase English letters.
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
        print(s)
        ll = len(s)
        if ll < 2:
            return ""
        if ll == 2:
            if abs(ord(s[0])-ord(s[1])) == abs(ord("A")-ord("a")):
                return s
            else:
                return ""

        azlower = "abcdefghijklmnopqrstuvwxyz"
        azupper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for ii in range(ll):
            if s[ii] in azlower:
                if chr(ord("A")+(ord(s[ii])-ord("a"))) not in s:
                    left_s = ""
                    if ii > 1:
                        left_s = self.longestNiceSubstring(s[:ii])

                    right_s = ""
                    if ii < ll-1:
                        right_s = self.longestNiceSubstring(s[ii+1:])

                    if len(left_s) < len(right_s):
                        return right_s
                    return left_s
            if s[ii] in azupper:
                if chr(ord("a")+(ord(s[ii])-ord("A"))) not in s:
                    left_s = ""
                    if ii > 1:
                        left_s = self.longestNiceSubstring(s[:ii])

                    right_s = ""
                    if ii < ll-1:
                        right_s = self.longestNiceSubstring(s[ii+1:])

                    if len(left_s) < len(right_s):
                        return right_s
                    return left_s
        return s

        ### wrong answer, non incursive solution but debug needed
        ll = len(s)
        azlower = "abcdefghijklmnopqrstuvwxyz"
        azupper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        llower = [0]*26
        lupper = [0]*26
        for each in s:
            if each in azlower:
                llower[ord(each)-ord("a")] += 1
            if each in azupper:
                lupper[ord(each)-ord("A")] += 1

        result = 1
        for ii in range(ll):
            llower_copy = llower.copy()
            lupper_copy = lupper.copy()
            print(llower_copy, lupper_copy)
            for jj in range(ll-1, ii, -1):
                flag = 0
                for kk in range(26):
                    if llower_copy[kk] == 0 and lupper_copy[kk] > 0:
                        flag = 1
                        break
                    if llower_copy[kk] > 0 and lupper_copy[kk] == 0:
                        flag = 1
                        break
                if flag == 0:
                    result = max(result, jj-ii)

                if s[jj] in azlower:
                    llower_copy[ord(s[jj])-ord("a")] -= 1
                if s[jj] in azupper:
                    lupper_copy[ord(s[jj])-ord("A")] -= 1

            if s[ii] in azlower:
                llower[ord(s[ii])-ord("a")] -= 1
            if s[ii] in azupper:
                lupper[ord(s[ii])-ord("A")] -= 1

        return result


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
