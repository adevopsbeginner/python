"""

Code
Testcase
Test Result
Test Result
214. Shortest Palindrome
Hard
Topics
Companies
You are given a string s. You can convert s to a
palindrome
 by adding characters in front of it.

Return the shortest palindrome you can find by performing this transformation.



Example 1:

Input: s = "aacecaaa"
Output: "aaacecaaa"
Example 2:

Input: s = "abcd"
Output: "dcbabcd"


Constraints:

0 <= s.length <= 5 * 104
s consists of lowercase English letters only.
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
        for ii in range(ll):
            if s[ll-1-ii] == s[0]:
                llsub = ll-ii
                ll2 = llsub//2
                #print(ii,llsub,ll2,llsub%2,s[0:ll2][::-1],s[(ll2+llsub%2):(ll-ii)])
                if s[0:ll2][::-1] == s[(ll2+llsub%2):(ll-ii)]:
                    return s[ll-ii:][::-1] + s
        return s[1:][::-1] + s


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
