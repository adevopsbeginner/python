"""
3090. Maximum Length Substring With Two Occurrences
Solved
Easy
Topics
premium lock icon
Companies
Hint
Given a string s, return the maximum length of a substring such that it contains at most two occurrences of each character.
 

Example 1:

Input: s = "bcbbbcba"

Output: 4

Explanation:

The following substring has a length of 4 and contains at most two occurrences of each character: "bcbbbcba".
Example 2:

Input: s = "aaaa"

Output: 2

Explanation:

The following substring has a length of 2 and contains at most two occurrences of each character: "aaaa".
 

Constraints:

2 <= s.length <= 100
s consists only of lowercase English letters.
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
        dd = defaultdict(int)
        dd[s[0]] += 1
        dd[s[1]] += 1
        index0 = 0
        index1 = 2
        ll = len(s)
        result = 2
        while index0 < ll and index1 < ll:
            #print(index0, index1)
            dd[s[index1]] += 1
            while dd[s[index1]] > 2:
                dd[s[index0]] -= 1
                index0 += 1
            index1 += 1
            result = max(result, index1-index0)
            
        return result


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
