"""
1160. Find Words That Can Be Formed by Characters
Easy
Topics
Companies
Hint
You are given an array of strings words and a string chars.

A string is good if it can be formed by characters from chars (each character can only be used once).

Return the sum of lengths of all good strings in words.

 

Example 1:

Input: words = ["cat","bt","hat","tree"], chars = "atach"
Output: 6
Explanation: The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.
Example 2:

Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
Output: 10
Explanation: The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.
 

Constraints:

1 <= words.length <= 1000
1 <= words[i].length, chars.length <= 100
words[i] and chars consist of lowercase English letters.
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
    def leetcode(self, words: List[str], chars: str) -> int:
        dd = defaultdict(int)
        for each in chars:
            dd[each] += 1

        result = 0
        for word in words:
            goodstring = 1
            ddword = defaultdict(int)
            for each in word:
                ddword[each] += 1

            for each in ddword:
                if ddword[each] > dd[each]:
                    goodstring = 0

            if goodstring:
                result += len(word)

        return result


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
