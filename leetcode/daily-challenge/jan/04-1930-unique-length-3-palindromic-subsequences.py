"""
1930. Unique Length-3 Palindromic Subsequences
Solved
Medium
Topics
Companies
Hint
Given a string s, return the number of unique palindromes of length three that are a subsequence of s.

Note that even if there are multiple ways to obtain the same subsequence, it is still only counted once.

A palindrome is a string that reads the same forwards and backwards.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
 

Example 1:

Input: s = "aabca"
Output: 3
Explanation: The 3 palindromic subsequences of length 3 are:
- "aba" (subsequence of "aabca")
- "aaa" (subsequence of "aabca")
- "aca" (subsequence of "aabca")
Example 2:

Input: s = "adc"
Output: 0
Explanation: There are no palindromic subsequences of length 3 in "adc".
Example 3:

Input: s = "bbcbaba"
Output: 4
Explanation: The 4 palindromic subsequences of length 3 are:
- "bbb" (subsequence of "bbcbaba")
- "bcb" (subsequence of "bbcbaba")
- "bab" (subsequence of "bbcbaba")
- "aba" (subsequence of "bbcbaba")
 

Constraints:

3 <= s.length <= 105
s consists of only lowercase English letters.
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
        az = "abcdefghijklmnopqrstuvwxyz"
        ddfirst = defaultdict(int)
        ddlast = defaultdict(int)
        ddcount = defaultdict(int)
        ll = len(s)
        for ii in range(ll):
            ddcount[s[ii]] += 1
            ddlast[s[ii]] = ii
            if ddfirst[s[ii]] == 0:
                ddfirst[s[ii]] = ii
        ddfirst[s[0]] = 0
        #for each in az:
        #    print(ddcount[each], ddfirst[each], ddlast[each])

        result = 0
        for first in az:
            if ddcount[first] < 2:
                continue
            flag = [0]*26
            for ii in range(ddfirst[first]+1,ddlast[first]):
                flag[ord(s[ii])-ord("a")] = 1
            result += sum(flag)
            #print(first,flag)

        return result


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
