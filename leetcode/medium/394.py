"""
394. Decode String
Solved
Medium
Topics
￼
Companies
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].

The test cases are generated so that the length of the output will never exceed 105.

 

Example 1:

Input: s = "3[a]2[bc]"
Output: "aaabcbc"
Example 2:

Input: s = "3[a2[c]]"
Output: "accaccacc"
Example 3:

Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"
 

Constraints:

1 <= s.length <= 30
s consists of lowercase English letters, digits, and square brackets '[]'.
s is guaranteed to be a valid input.
All the integers in s are in the range [1, 300].
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
        ll = len(s)
        az = 'abcdefghijklmnopqrstuvwxyz'
        a10 = '1234567890'
        time = 0
        ld = []
        lsub = ['']
        subp = ''
        subc = ''
        for ii in range(ll):
            if s[ii] in az:
                subc += s[ii]
            elif s[ii] in a10:
                time *= 10
                time += int(s[ii])
            elif s[ii] == '[':
                ld.append(time)
                time = 0
                lsub.append(subc)
                subc = ''
            elif s[ii] == ']':
                time = ld.pop()
                subp = lsub.pop()
                subc = subp+subc*time
                time = 0
        return subc


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
