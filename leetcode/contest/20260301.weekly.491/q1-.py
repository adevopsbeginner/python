"""
Q1. Trim Trailing Vowels
Easy
3 pt.
You are given a string s that consists of lowercase English letters.

Return the string obtained by removing all trailing vowels from s.

The vowels consist of the characters 'a', 'e', 'i', 'o', and 'u'.

 

Example 1:

Input: s = "idea"

Output: "id"

Explanation:

Removing "idea", we obtain the string "id".

Example 2:

Input: s = "day"

Output: "day"

Explanation:

There are no trailing vowels in the string "day".

Example 3:

Input: s = "aeiou"

Output: ""

Explanation:

Removing "aeiou", we obtain the string "".

 

Constraints:

1 <= s.length <= 100
s consists of only lowercase English letters.
"""

from typing import List
from collections import defaultdict

class Solution:
    def leetcode(self, s: str) -> str:
        ll = len(s)
        for ii in range(ll-1, -1, -1):
            if s[ii] not in "aeiou":
                return s[:ii+1]
        
        return ""
