"""
2423. Remove Letter To Equalize Frequency
Solved
Easy
Topics
Companies
Hint
You are given a 0-indexed string word, consisting of lowercase English letters. You need to select one index and remove the letter at that index from word so that the frequency of every letter present in word is equal.

Return true if it is possible to remove one letter so that the frequency of all letters in word are equal, and false otherwise.

Note:

The frequency of a letter x is the number of times it occurs in the string.
You must remove exactly one letter and cannot choose to do nothing.
 

Example 1:

Input: word = "abcc"
Output: true
Explanation: Select index 3 and delete it: word becomes "abc" and each character has a frequency of 1.
Example 2:

Input: word = "aazz"
Output: false
Explanation: We must delete a character, so either the frequency of "a" is 1 and the frequency of "z" is 2, or vice versa. It is impossible to make all present letters have equal frequency.
 

Constraints:

2 <= word.length <= 100
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
    def leetcode(self, word):
        """
        :type word: str
        :rtype: bool
        """
        dd = defaultdict(int)
        for each in word:
            dd[each] += 1
        ll = list(dd.values())
        #print(ll)
        ll.sort()
        # "zz"
        if len(ll) == 1:
            return True
        
        # "aaa"
        if ll[0] == 1 and ll[-1] == 1:
            return True

        # "cccd"
        if ll[0] == 1 and len(ll) == 2:
            return True
        if ll[0] == 1 and ll[1] == ll[-1]:
            return True
        
        # "aazz"
        if ll[-1] == ll[0]:
            return False
        if ll[-1] - ll[0] > 1:
            return False
        if ll[-1]-ll[-2] == 1:
            return True
        
        # aaabbbcc
        # if ll[0]+1 == ll[1]:
        #     return True
        

        return False


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
