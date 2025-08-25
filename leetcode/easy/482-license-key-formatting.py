"""
482. License Key Formatting
Easy
Topics
Companies
You are given a license key represented as a string s that consists of only alphanumeric characters and dashes. The string is separated into n + 1 groups by n dashes. You are also given an integer k.

We want to reformat the string s such that each group contains exactly k characters, except for the first group, which could be shorter than k but still must contain at least one character. Furthermore, there must be a dash inserted between two groups, and you should convert all lowercase letters to uppercase.

Return the reformatted license key.



Example 1:

Input: s = "5F3Z-2e-9-w", k = 4
Output: "5F3Z-2E9W"
Explanation: The string s has been split into two parts, each part has 4 characters.
Note that the two extra dashes are not needed and can be removed.
Example 2:

Input: s = "2-5g-3-J", k = 2
Output: "2-5G-3J"
Explanation: The string s has been split into three parts, each part has 2 characters except the first part as it could be shorter as mentioned above.


Constraints:

1 <= s.length <= 105
s consists of English letters, digits, and dashes '-'.
1 <= k <= 104
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
    def leetcode(self, s: str, k: int) -> str:
        ls = []
        for each in s:
            if each == "-":
                continue
            elif each in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
                ls.append(each)
            else:
                ls.append(each.upper())

        ll = len(ls)
        ll1 = ll % k
        result = []
        if ll1:
            result.append("".join(ls[0:ll1]))
        for ii in range(ll // k):
            result.append("".join(ls[ll1 + ii * k:ll1 + ii * k + k]))

        return "-".join(result)

if __name__ == "__main__":
    app = Solution()
    a = 5
    b = [[1,2]]
    print(app.leetcode(a,b))
