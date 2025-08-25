"""
1961. Check If String Is a Prefix of Array
Solved
Easy
Topics
Companies
Hint
Given a string s and an array of strings words, determine whether s is a prefix string of words.

A string s is a prefix string of words if s can be made by concatenating the first k strings in words for some positive k no larger than words.length.

Return true if s is a prefix string of words, or false otherwise.

 

Example 1:

Input: s = "iloveleetcode", words = ["i","love","leetcode","apples"]
Output: true
Explanation:
s can be made by concatenating "i", "love", and "leetcode" together.
Example 2:

Input: s = "iloveleetcode", words = ["apples","i","love","leetcode"]
Output: false
Explanation:
It is impossible to make s using a prefix of arr.
 

Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 20
1 <= s.length <= 1000
words[i] and s consist of only lowercase English letters.
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
    def leetcode(self, s: str, words: List[str]) -> bool:
        ll = len(s)
        index = 0
        while index < ll:
            print(index, words)
            if len(words) > 0:
                word = words.pop(0)
                llw = len(word)
                if index + llw > ll:
                    return False
                if word == s[index:index+llw]:
                    index += llw
                else:
                    return False
            else:
                return False

        if index != ll:
            return False
        return True


        ### wrong answer due to "a", ["aa"]
        wordstr = "".join(words)
        if wordstr.startswith(s):
            return True
        return False


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
