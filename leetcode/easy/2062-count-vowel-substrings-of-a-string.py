"""
2062. Count Vowel Substrings of a String

A substring is a contiguous (non-empty) sequence of characters within a string.

A vowel substring is a substring that only consists of vowels ('a', 'e', 'i', 'o', and 'u') and has all five vowels present in it.

Given a string word, return the number of vowel substrings in word.

 

Example 1:

Input: word = "aeiouu"
Output: 2
Explanation: The vowel substrings of word are as follows (underlined):
- "aeiouu"
- "aeiouu"
Example 2:

Input: word = "unicornarihan"
Output: 0
Explanation: Not all 5 vowels are present, so there are no vowel substrings.
Example 3:

Input: word = "cuaieuouac"
Output: 7
Explanation: The vowel substrings of word are as follows (underlined):
- "cuaieuouac"
- "cuaieuouac"
- "cuaieuouac"
- "cuaieuouac"
- "cuaieuouac"
- "cuaieuouac"
- "cuaieuouac"
 

Constraints:

1 <= word.length <= 100
word consists of lowercase English letters only.
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
    def leetcode(self, word: str) -> int:
        count = {"a":0, "e":0, "i":0, "o":0, "u":0}
        word += "z"
        ll = len(word)
        result = 0
        vowel_len = 0
        for ii in range(ll):
            if word[ii] not in "aeiou":
                continue
            no_vowel_flag = 0
            vowel_len = 1
            count = {"a":0, "e":0, "i":0, "o":0, "u":0}
            count[word[ii]] += 1
            for jj in range(ii+1,ll):
                if word[jj] not in "aeiou":
                    no_vowel_flag = 1
                    break
                count[word[jj]] += 1
                if count["a"]*count["e"]*count["i"]*count["o"]*count["u"] > 0:
                    result += 1
            if no_vowel_flag > 0:
                continue

        return result


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
