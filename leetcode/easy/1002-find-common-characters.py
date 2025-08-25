"""
1002. Find Common Characters
Solved
Easy
Topics
Companies
Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). You may return the answer in any order.



Example 1:

Input: words = ["bella","label","roller"]
Output: ["e","l","l"]
Example 2:

Input: words = ["cool","lock","cook"]
Output: ["c","o"]


Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 100
words[i] consists of lowercase English letters.
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
    def leetcode(self, words: List[str]) -> List[str]:
        result = []
        total = 0
        ll = len(words)

        ldd = [defaultdict(int) for ii in range(ll)]
        for ii in range(ll):
            for char in words[ii]:
                ldd[ii][char] += 1

        for ii in range(26):
            count = [each[chr(ii+97)] for each in ldd]
            if min(count):
                # print(len(ldd),chr(ii+97), count)
                total += min(count)
                result += [chr(ii + 97) for jj in range(min(count))]

        return result


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
