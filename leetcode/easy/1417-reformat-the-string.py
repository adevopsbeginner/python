"""
1417. Reformat The String
Easy
Topics
Companies
Hint
You are given an alphanumeric string s. (Alphanumeric string is a string consisting of lowercase English letters and digits).

You have to find a permutation of the string where no letter is followed by another letter and no digit is followed by another digit. That is, no two adjacent characters have the same type.

Return the reformatted string or return an empty string if it is impossible to reformat the string.

 

Example 1:

Input: s = "a0b1c2"
Output: "0a1b2c"
Explanation: No two adjacent characters have the same type in "0a1b2c". "a0b1c2", "0a1b2c", "0c2a1b" are also valid permutations.
Example 2:

Input: s = "leetcode"
Output: ""
Explanation: "leetcode" has only characters so we cannot separate them by digits.
Example 3:

Input: s = "1229857369"
Output: ""
Explanation: "1229857369" has only digits so we cannot separate them by characters.
 

Constraints:

1 <= s.length <= 500
s consists of only lowercase English letters and/or digits.
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
        count_alpha = 0
        count_numeric = 0
        result = ""
        for each in s:
            if each in "0123456789":
                count_numeric += 1
            else:
                count_alpha += 1
        if abs(count_alpha - count_numeric) > 1:
            return ""
        index_alpha = 0
        index_numeric = 0
        while index_alpha < ll and index_numeric < ll:
            while index_alpha < ll:
                if s[index_alpha] in "0123456789":
                    index_alpha += 1
                else:
                    break
            while index_numeric < ll:
                if s[index_numeric] not in "0123456789":
                    index_numeric += 1
                else:
                    break
            #print(result, index_alpha, index_numeric)
            if index_alpha < ll and index_numeric < ll:
                result += s[index_alpha] + s[index_numeric]
                index_alpha += 1
                index_numeric += 1
            else:
                if index_alpha < ll:
                    result += s[index_alpha]
                    index_alpha += 1
                if index_numeric < ll:
                    result = s[index_numeric] + result
                    index_numeric += 1
            #print(result, index_alpha, index_numeric)

        while index_alpha < ll:
            #print("alpha", index_alpha)
            if s[index_alpha] in "0123456789":
                index_alpha += 1
            if index_alpha < ll:
                result += s[index_alpha]
                break
        while index_numeric < ll:
            #print("numberic", index_numeric)
            if s[index_numeric] not in "0123456789":
                index_numeric += 1
            if index_numeric < ll:
                result = s[index_numeric] + result
                break

        return result


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
