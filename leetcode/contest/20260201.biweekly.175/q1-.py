"""
Q1. Reverse Letters Then Special Characters in a String
Easy
3 pt.
You are given a string s consisting of lowercase English letters and special characters.

Your task is to perform these in order:

Reverse the lowercase letters and place them back into the positions originally occupied by letters.
Reverse the special characters and place them back into the positions originally occupied by special characters.
Return the resulting string after performing the reversals.

 

Example 1:

Input: s = ")ebc#da@f("

Output: "(fad@cb#e)"

Explanation:

The letters in the string are ['e', 'b', 'c', 'd', 'a', 'f']:
Reversing them gives ['f', 'a', 'd', 'c', 'b', 'e']
s becomes ")fad#cb@e("
​​​​​​​The special characters in the string are [')', '#', '@', '(']:
Reversing them gives ['(', '@', '#', ')']
s becomes "(fad@cb#e)"
Example 2:

Input: s = "z"

Output: "z"

Explanation:

The string contains only one letter, and reversing it does not change the string. There are no special characters.

Example 3:

Input: s = "!@#$%^&*()"

Output: ")(*&^%$#@!"

Explanation:

The string contains no letters. The string contains all special characters, so reversing the special characters reverses the whole string.

 

Constraints:

1 <= s.length <= 100
s consists only of lowercase English letters and the special characters in "!@#$%^&*()".
"""

from typing import List
from collections import defaultdict

class Solution:
    def leetcode(self, s: str) -> str:
        ll = len(s)
        az = "abcdefghijklmnopqrstuvwxyz"
        result = [""]*ll
        
        index_english = ll-1
        while s[index_english] not in az and index_english >= 0:
            index_english -= 1
            
        index_special = ll-1
        while s[index_special] in az and index_special >= 0:
            index_special -= 1
        
        for ii in range(ll):
            if s[ii] in az:
                result[ii] = s[index_english]
                index_english -= 1
                while s[index_english] not in az and index_english >= 0:
                    index_english -= 1
            else:
                result[ii] = s[index_special]
                index_special -= 1
                while s[index_special] in az and index_special >= 0:
                    index_special -= 1

        return "".join(result)
