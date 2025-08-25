"""
1309. Decrypt String from Alphabet to Integer Mapping
Easy
Topics
Companies
Hint
You are given a string s formed by digits and '#'. We want to map s to English lowercase characters as follows:

Characters ('a' to 'i') are represented by ('1' to '9') respectively.
Characters ('j' to 'z') are represented by ('10#' to '26#') respectively.
Return the string formed after mapping.

The test cases are generated so that a unique mapping will always exist.

 

Example 1:

Input: s = "10#11#12"
Output: "jkab"
Explanation: "j" -> "10#" , "k" -> "11#" , "a" -> "1" , "b" -> "2".
Example 2:

Input: s = "1326#"
Output: "acz"
 

Constraints:

1 <= s.length <= 1000
s consists of digits and the '#' letter.
s will be a valid string such that mapping is always possible.
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
        result = ""
        ll = len(s)
        s += "11"
        abcdefghi = "0abcdefghi"
        jz = "0abcdefghijklmnopqrstuvwxyz"
        ten = 0
        for ii in range(ll):
            print(ii,result,s[ii],ten)
            if s[ii] == "#":
                result += jz[ten]
                ten = 0
            else:
                digit = int(s[ii])
                if s[ii+2] == "#" or s[ii+1] == "#":
                    ten = ten*10+digit
                else:
                    result += abcdefghi[digit]
                    ten = 0

        return result


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
