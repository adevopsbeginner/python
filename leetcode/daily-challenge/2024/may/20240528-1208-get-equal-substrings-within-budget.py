"""
1208. Get Equal Substrings Within Budget
Medium
Topics
Companies
Hint
You are given two strings s and t of the same length and an integer maxCost.

You want to change s to t. Changing the ith character of s to ith character of t costs |s[i] - t[i]| (i.e., the absolute difference between the ASCII values of the characters).

Return the maximum length of a substring of s that can be changed to be the same as the corresponding substring of t with a cost less than or equal to maxCost. If there is no substring from s that can be changed to its corresponding substring from t, return 0.

 

Example 1:

Input: s = "abcd", t = "bcdf", maxCost = 3
Output: 3
Explanation: "abc" of s can change to "bcd".
That costs 3, so the maximum length is 3.
Example 2:

Input: s = "abcd", t = "cdef", maxCost = 3
Output: 1
Explanation: Each character in s costs 2 to change to character in t,  so the maximum length is 1.
Example 3:

Input: s = "abcd", t = "acde", maxCost = 0
Output: 1
Explanation: You cannot make any change, so the maximum length is 1.
 

Constraints:

1 <= s.length <= 105
t.length == s.length
0 <= maxCost <= 106
s and t consist of only lowercase English letters.
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
    def leetcode(self, s: str, t: str, maxCost: int) -> int:
        ll = len(s)
        st = []
        for ii in range(ll):
            st.append(abs(ord(s[ii])-ord(t[ii])))
        # print(st)
        result = 0
        subtotal = 0
        start = 0
        end = -1
        while start < ll:
            # print(result,start,end,subtotal)
            if end == ll-1:
                break

            if subtotal > maxCost:
                subtotal -= st[start]
                start += 1
                continue
            
            end += 1
            subtotal += st[end]
            if subtotal <= maxCost:
                result = max(result,end-start+1)

        return result

if __name__ == "__main__":
    app = Solution()
    a = 2
    s = "thjdoffka"
    t = "qhrnlntls"
    print(app.leetcode(s,t,11))
