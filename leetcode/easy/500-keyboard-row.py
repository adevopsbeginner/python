"""
500. Keyboard Row
Easy
Topics
Companies
Given an array of strings words, return the words that can be typed using letters of the alphabet on only one row of American keyboard like the image below.

In the American keyboard:

the first row consists of the characters "qwertyuiop",
the second row consists of the characters "asdfghjkl", and
the third row consists of the characters "zxcvbnm".



Example 1:

Input: words = ["Hello","Alaska","Dad","Peace"]
Output: ["Alaska","Dad"]
Example 2:

Input: words = ["omk"]
Output: []
Example 3:

Input: words = ["adsdf","sfd"]
Output: ["adsdf","sfd"]


Constraints:

1 <= words.length <= 20
1 <= words[i].length <= 100
words[i] consists of English letters (both lowercase and uppercase).
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
    def leetcode(self, words: List[str]) -> List[str]:
        def charline(char: string) -> int:
            if char.lower() in "qwertyuiop":
                return 1
            elif char.lower() in "asdfghjkl":
                return 2
            elif char.lower() in "zxcvbnm":
                return 3
            return 0

        result = []
        for word in words:
            first = charline(word[0])
            insameline = 1
            for char in word:
                if charline(char) != first:
                    insameline = 0
                    break
            if insameline:
                result.append(word)

        return result

if __name__ == "__main__":
    app = Solution()
    a = 5
    b = [[1,2]]
    print(app.leetcode(a,b))
