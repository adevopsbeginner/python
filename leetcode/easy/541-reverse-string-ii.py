"""
541. Reverse String II
Easy
Topics
Companies
Given a string s and an integer k, reverse the first k characters for every 2k characters counting from the start of the string.

If there are fewer than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and leave the other as original.



Example 1:

Input: s = "abcdefg", k = 2
Output: "bacdfeg"
Example 2:

Input: s = "abcd", k = 2
Output: "bacd"


Constraints:

1 <= s.length <= 104
s consists of only lowercase English letters.
1 <= k <= 104
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
    def leetcode(self, s: str, k: int) -> str:
        ll = len(s)
        result = ""
        flag = 1
        index = 0
        while index < ll:
            if flag:
                if index == 0:
                    result += s[min(ll,index+k)-1::-1]
                else:
                    result += s[min(ll,index+k)-1:index-1:-1]

            else:
                result += s[index:min(ll,index+k)]

            index += k
            flag ^= 1

        return result


if __name__ == "__main__":
    app = Solution()
    a = "abcdefg"
    b = 2
    print(app.leetcode(a,2))
