"""
1717. Maximum Score From Removing Substrings
Medium
Topics
Companies
Hint
You are given a string s and two integers x and y. You can perform two types of operations any number of times.

Remove substring "ab" and gain x points.
For example, when removing "ab" from "cabxbae" it becomes "cxbae".
Remove substring "ba" and gain y points.
For example, when removing "ba" from "cabxbae" it becomes "cabxe".
Return the maximum points you can gain after applying the above operations on s.



Example 1:

Input: s = "cdbcbbaaabab", x = 4, y = 5
Output: 19
Explanation:
- Remove the "ba" underlined in "cdbcbbaaabab". Now, s = "cdbcbbaaab" and 5 points are added to the score.
- Remove the "ab" underlined in "cdbcbbaaab". Now, s = "cdbcbbaa" and 4 points are added to the score.
- Remove the "ba" underlined in "cdbcbbaa". Now, s = "cdbcba" and 5 points are added to the score.
- Remove the "ba" underlined in "cdbcba". Now, s = "cdbc" and 5 points are added to the score.
Total score = 5 + 4 + 5 + 5 = 19.
Example 2:

Input: s = "aabbaaxybbaabb", x = 5, y = 4
Output: 20


Constraints:

1 <= s.length <= 105
1 <= x, y <= 104
s consists of lowercase English letters.
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
    def leetcode(self, s: str, x: int, y: int) -> int:
        def remove_substring(s, sub, points):
            stack = []
            total_points = 0
            for char in s:
                stack.append(char)
                if len(stack) >= 2 and stack[-2] + stack[-1] == sub:
                    stack.pop()
                    stack.pop()
                    total_points += points
            return ''.join(stack), total_points

        # Determine which order to prioritize
        if x > y:
            # Remove "ab" first, then "ba"
            s, points1 = remove_substring(s, "ab", x)
            _, points2 = remove_substring(s, "ba", y)
        else:
            # Remove "ba" first, then "ab"
            s, points1 = remove_substring(s, "ba", y)
            _, points2 = remove_substring(s, "ab", x)

        return points1 + points2


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
