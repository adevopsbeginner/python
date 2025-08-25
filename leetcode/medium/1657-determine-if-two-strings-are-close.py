"""
1657. Determine if Two Strings Are Close
Solved
Medium
Topics
Companies
Hint
Two strings are considered close if you can attain one from the other using the following operations:

Operation 1: Swap any two existing characters.
For example, abcde -> aecdb
Operation 2: Transform every occurrence of one existing character into another existing character, and do the same with the other character.
For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)
You can use the operations on either string as many times as necessary.

Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.

 

Example 1:

Input: word1 = "abc", word2 = "bca"
Output: true
Explanation: You can attain word2 from word1 in 2 operations.
Apply Operation 1: "abc" -> "acb"
Apply Operation 1: "acb" -> "bca"
Example 2:

Input: word1 = "a", word2 = "aa"
Output: false
Explanation: It is impossible to attain word2 from word1, or vice versa, in any number of operations.
Example 3:

Input: word1 = "cabbba", word2 = "abbccc"
Output: true
Explanation: You can attain word2 from word1 in 3 operations.
Apply Operation 1: "cabbba" -> "caabbb"
Apply Operation 2: "caabbb" -> "baaccc"
Apply Operation 2: "baaccc" -> "abbccc"
 

Constraints:

1 <= word1.length, word2.length <= 105
word1 and word2 contain only lowercase English letters.
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
    def leetcode(self, word1: str, word2: str) -> bool:
        ll = len(word1)
        if ll != len(word2):
            return False
        if sorted(word1) == sorted(word2):
            return True
        dd1 = defaultdict(int)
        dd2 = defaultdict(int)
        for each in word1:
            dd1[each] += 1
        for each in word2:
            dd2[each] += 1
        
        ### "abbzzca" vs. "babzzcz"
        if sorted(list(dd1.values())) != sorted(list(dd2.values())):
            return False
        az = "abcdefghijklmnopqrstuvwxyz"
        for each in az:
            if dd1[each] == dd2[each]:
                continue
            if dd1[each] == 0:
                return False
            if dd2[each] == 0:
                return False

        return True


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
