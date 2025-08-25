"""
1576. Replace All ?'s to Avoid Consecutive Repeating Characters
Solved
Easy
Topics
Companies
Hint
Given a string s containing only lowercase English letters and the '?' character, convert all the '?' characters into lowercase letters such that the final string does not contain any consecutive repeating characters. You cannot modify the non '?' characters.

It is guaranteed that there are no consecutive repeating characters in the given string except for '?'.

Return the final string after all the conversions (possibly zero) have been made. If there is more than one solution, return any of them. It can be shown that an answer is always possible with the given constraints.

 

Example 1:

Input: s = "?zs"
Output: "azs"
Explanation: There are 25 solutions for this problem. From "azs" to "yzs", all are valid. Only "z" is an invalid modification as the string will consist of consecutive repeating characters in "zzs".
Example 2:

Input: s = "ubv?w"
Output: "ubvaw"
Explanation: There are 24 solutions for this problem. Only "v" and "w" are invalid modifications as the strings will consist of consecutive repeating characters in "ubvvw" and "ubvww".
 

Constraints:

1 <= s.length <= 100
s consist of lowercase English letters and '?'.
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
        result = ""
        az = "abcdefghijklmnopqrstuvwxyz"
        cindex = 0
        for ii in range(ll):
            if s[ii] == "?":
                if ii == 0 and ii == ll-1:
                    return "a"
                if ii > 0:
                    while az[cindex] == result[-1]:
                        cindex = (cindex+1)%26
                if ii < ll-1:
                    while az[cindex] == s[ii+1]:
                        cindex = (cindex+1)%26
                ### "b?a"
                if ii > 0:
                    while az[cindex] == result[-1]:
                        cindex = (cindex+1)%26

                result += az[cindex]
            else:
                result += s[ii]

        return result


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
