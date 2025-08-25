'''
28. Find the Index of the First Occurrence in a String
Solved
Easy
Topics
Companies
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

 

Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
 

Constraints:

1 <= haystack.length, needle.length <= 104
haystack and needle consist of only lowercase English characters.
'''

from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def leetcode(self, haystack: str, needle: str) -> int:
        result = -1
        ll = len(haystack)
        lln = len(needle)
        for ii in range(ll-lln+1):
            if haystack[ii:ii+lln] == needle:
                return ii
        return result
    
        ### 2
        return haystack.find(needle)

if __name__ == "__main__":
    app = Solution()
    test1 = "sadbutsad"
    test2 = "sad"
    print(app.leetcode(test1, test2))
