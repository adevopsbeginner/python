"""
2047. Number of Valid Words in a Sentence

A sentence consists of lowercase letters ('a' to 'z'), digits ('0' to '9'), hyphens ('-'), punctuation marks ('!', '.', and ','), and spaces (' ') only. Each sentence can be broken down into one or more tokens separated by one or more spaces ' '.

A token is a valid word if all three of the following are true:

It only contains lowercase letters, hyphens, and/or punctuation (no digits).
There is at most one hyphen '-'. If present, it must be surrounded by lowercase characters ("a-b" is valid, but "-ab" and "ab-" are not valid).
There is at most one punctuation mark. If present, it must be at the end of the token ("ab,", "cd!", and "." are valid, but "a!b" and "c.," are not valid).
Examples of valid words include "a-b.", "afad", "ba-c", "a!", and "!".

Given a string sentence, return the number of valid words in sentence.

 

Example 1:

Input: sentence = "cat and  dog"
Output: 3
Explanation: The valid words in the sentence are "cat", "and", and "dog".
Example 2:

Input: sentence = "!this  1-s b8d!"
Output: 0
Explanation: There are no valid words in the sentence.
"!this" is invalid because it starts with a punctuation mark.
"1-s" and "b8d" are invalid because they contain digits.
Example 3:

Input: sentence = "alice and  bob are playing stone-game10"
Output: 5
Explanation: The valid words in the sentence are "alice", "and", "bob", "are", and "playing".
"stone-game10" is invalid because it contains digits.
 

Constraints:

1 <= sentence.length <= 1000
sentence only contains lowercase English letters, digits, ' ', '-', '!', '.', and ','.
There will be at least 1 token.
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
    def leetcode(self, sentence: str) -> int:
        result = 0
        words = sentence.split(" ")
        #print(words)
        az = "abcdefghijklmnopqrstuvwxyz"
        for word in words:
            if len(word) == 0:
                continue
            flag_hyphen = 0
            flag_puctuation = 0

            count_digit = 0
            count_hyphen = 0
            count_punctuation = 0

            ll = len(word)

            for ii in range(ll):
                if word[ii] in "0123456789":
                    count_digit += 1
                if word[ii] == "-":
                    if ii == 0:
                        flag_hyphen = 1
                        break
                    if ii == ll-1:
                        flag_hyphen = 1
                        break
                    if word[ii-1] not in az:
                        flag_hyphen = 1
                        break
                    if word[ii+1] not in az:
                        flag_hyphen = 1
                        break
                    count_hyphen += 1
                if word[ii] in "!., ":
                    if ii < ll-1:
                        flag_puctuation = 1
                        break
                    count_punctuation += 1
            
            if count_digit > 0:
                continue
            if count_hyphen > 1:
                continue
            if count_punctuation > 1:
                continue
            if flag_hyphen > 0:
                continue
            if flag_puctuation > 0:
                continue

            result += 1

        return result


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
