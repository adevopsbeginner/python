"""
953. Verifying an Alien Dictionary
Easy
Topics
Companies
In an alien language, surprisingly, they also use English lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographically in this alien language.



Example 1:

Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
Example 2:

Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.
Example 3:

Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).


Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 20
order.length == 26
All characters in words[i] and order are English lowercase letters.
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
    def leetcode(self, words: List[str], order: str) -> bool:
        def alien_order(a: str, b: str) -> int:
            if a == b:
                return 0
            lla = len(a)
            llb = len(b)
            for ii in range(min(lla,llb)):
                if a[ii] == b[ii]:
                    continue
                elif dd[a[ii]] < dd[b[ii]]:
                    return -1
                else:
                    return 1

            if lla < llb:
                return -1
            return 1

        ll = len(words)
        dd = defaultdict(int)
        for ii in range(26):
            dd[order[ii]] = ii
        for ii in range(1,ll):
            print(alien_order(words[ii], words[ii-1]))
            if alien_order(words[ii], words[ii-1]) < 0:
                return False

        return True


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
