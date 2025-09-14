"""
966. Vowel Spellchecker
Medium
Topics
premium lock icon
Companies
Given a wordlist, we want to implement a spellchecker that converts a query word into a correct word.

For a given query word, the spell checker handles two categories of spelling mistakes:

Capitalization: If the query matches a word in the wordlist (case-insensitive), then the query word is returned with the same case as the case in the wordlist.
Example: wordlist = ["yellow"], query = "YellOw": correct = "yellow"
Example: wordlist = ["Yellow"], query = "yellow": correct = "Yellow"
Example: wordlist = ["yellow"], query = "yellow": correct = "yellow"
Vowel Errors: If after replacing the vowels ('a', 'e', 'i', 'o', 'u') of the query word with any vowel individually, it matches a word in the wordlist (case-insensitive), then the query word is returned with the same case as the match in the wordlist.
Example: wordlist = ["YellOw"], query = "yollow": correct = "YellOw"
Example: wordlist = ["YellOw"], query = "yeellow": correct = "" (no match)
Example: wordlist = ["YellOw"], query = "yllw": correct = "" (no match)
In addition, the spell checker operates under the following precedence rules:

When the query exactly matches a word in the wordlist (case-sensitive), you should return the same word back.
When the query matches a word up to capitlization, you should return the first such match in the wordlist.
When the query matches a word up to vowel errors, you should return the first such match in the wordlist.
If the query has no matches in the wordlist, you should return the empty string.
Given some queries, return a list of words answer, where answer[i] is the correct word for query = queries[i].

 

Example 1:

Input: wordlist = ["KiTe","kite","hare","Hare"], queries = ["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"]
Output: ["kite","KiTe","KiTe","Hare","hare","","","KiTe","","KiTe"]
Example 2:

Input: wordlist = ["yellow"], queries = ["YellOw"]
Output: ["yellow"]
 

Constraints:

1 <= wordlist.length, queries.length <= 5000
1 <= wordlist[i].length, queries[i].length <= 7
wordlist[i] and queries[i] consist only of only English letters.
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
    def leetcode(self, wordlist: List[str], queries: List[str]) -> List[str]:
        def no_vowels(word):
            result = ""
            list_word = list(word)
            ll = len(list_word)
            for ii in range(ll):
                if list_word[ii] in "aeiou":
                    list_word[ii] = "-"
            result = "".join(list_word)
            
            return result

        ll = len(wordlist)
        # wordlower = [word.lower() for word in wordlist]
        # wordnovowel = [no_vowels(word) for word in wordlower]

        wordlower = {}
        wordnovowel = {}

        for word in wordlist:
            if word.lower() not in wordlower:
                wordlower[word.lower()] = word
            if no_vowels(word.lower()) not in wordnovowel:
                wordnovowel[no_vowels(word.lower())] = word

        #print(wordlower, wordnovowel)

        llq = len(queries)
        result = [""] * llq

        wordlist_set = set(wordlist)

        for ii in range(llq):
            if queries[ii] in wordlist_set:
                result[ii] = queries[ii]
            elif queries[ii].lower() in wordlower:
                result[ii] = wordlower[queries[ii].lower()]
            elif no_vowels(queries[ii].lower()) in wordnovowel:
                result[ii] = wordnovowel[no_vowels(queries[ii].lower())]

        return result


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
