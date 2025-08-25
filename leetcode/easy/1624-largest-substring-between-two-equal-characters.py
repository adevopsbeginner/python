"""
1624. Largest Substring Between Two Equal Characters
Solved
Easy
Topics
Companies
Hint
Given a string s, return the length of the longest substring between two equal characters, excluding the two characters. If there is no such substring return -1.

A substring is a contiguous sequence of characters within a string.

 

Example 1:

Input: s = "aa"
Output: 0
Explanation: The optimal substring here is an empty substring between the two 'a's.
Example 2:

Input: s = "abca"
Output: 2
Explanation: The optimal substring here is "bc".
Example 3:

Input: s = "cbzxy"
Output: -1
Explanation: There are no characters that appear twice in s.
 

Constraints:

1 <= s.length <= 300
s contains only lowercase English letters.
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
        result = -1
        dd = defaultdict(int)
        ddfirst = defaultdict(int)
        ddlast = defaultdict(int)
        for ii in range(ll):
            dd[s[ii]] += 1
            if s[ii] not in ddfirst:
                ddfirst[s[ii]] = ii
            ddlast[s[ii]] = ii
        az = "abcdefghijklmnopqrstuvwxyz"
        for each in az:
            #print(each, dd[each], ddfirst[each], ddlast[each])
            if dd[each] < 2:
                continue
            result = max(result, ddlast[each]-ddfirst[each]-1)

        return result


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
