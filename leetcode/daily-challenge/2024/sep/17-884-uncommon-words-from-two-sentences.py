"""
884. Uncommon Words from Two Sentences
Solved
Easy
Topics
Companies
A sentence is a string of single-space separated words where each word consists only of lowercase letters.

A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.

Given two sentences s1 and s2, return a list of all the uncommon words. You may return the answer in any order.



Example 1:

Input: s1 = "this apple is sweet", s2 = "this apple is sour"

Output: ["sweet","sour"]

Explanation:

The word "sweet" appears only in s1, while the word "sour" appears only in s2.

Example 2:

Input: s1 = "apple apple", s2 = "banana"

Output: ["banana"]



Constraints:

1 <= s1.length, s2.length <= 200
s1 and s2 consist of lowercase English letters and spaces.
s1 and s2 do not have leading or trailing spaces.
All the words in s1 and s2 are separated by a single space.
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
    def leetcode(self, s1: str, s2: str) -> List[str]:
        ls1 = s1.split()
        ls2 = s2.split()
        dd1 = defaultdict(int)
        for each in ls1:
            dd1[each] += 1
        dd2 = defaultdict(int)
        for each in ls2:
            dd2[each] += 1
        result = []
        for each in dd1:
            if dd1[each] == 1 and dd2[each] == 0:
                result.append(each)
        for each in dd2:
            if dd2[each] == 1 and dd1[each] == 0:
                result.append(each)

        return result


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
