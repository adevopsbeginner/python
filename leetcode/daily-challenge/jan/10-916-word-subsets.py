"""
916. Word Subsets
Solved
Medium
Topics
Companies
You are given two string arrays words1 and words2.

A string b is a subset of string a if every letter in b occurs in a including multiplicity.

For example, "wrr" is a subset of "warrior" but is not a subset of "world".
A string a from words1 is universal if for every string b in words2, b is a subset of a.

Return an array of all the universal strings in words1. You may return the answer in any order.

 

Example 1:

Input: words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["e","o"]
Output: ["facebook","google","leetcode"]
Example 2:

Input: words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["l","e"]
Output: ["apple","google","leetcode"]
 

Constraints:

1 <= words1.length, words2.length <= 104
1 <= words1[i].length, words2[i].length <= 10
words1[i] and words2[i] consist only of lowercase English letters.
All the strings of words1 are unique.
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
    def leetcode(self, words1: List[str], words2: List[str]) -> List[str]:
        dd2 = defaultdict(int)
        az = "abcdefghijklmnopqrstuvwxyz"
        for word in words2:
            dd = defaultdict(int)
            for each in word:
                dd[each] += 1
            
            for c in az:
                dd2[c] = max(dd2[c], dd[c])
        
        result = []
        for word in words1:
            dd = defaultdict(int)
            for each in word:
                dd[each] += 1
            
            universal_flag = 1
            for c in az:
                if dd[c] < dd2[c]:
                    universal_flag = 0
            if universal_flag == 1:
                result.append(word)

        return result


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
