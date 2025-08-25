"""
1957. Delete Characters to Make Fancy String
Solved
Easy
Topics
Companies
Hint
A fancy string is a string where no three consecutive characters are equal.

Given a string s, delete the minimum possible number of characters from s to make it fancy.

Return the final string after the deletion. It can be shown that the answer will always be unique.

 

Example 1:

Input: s = "leeetcode"
Output: "leetcode"
Explanation:
Remove an 'e' from the first group of 'e's to create "leetcode".
No three consecutive characters are equal, so return "leetcode".
Example 2:

Input: s = "aaabaaaa"
Output: "aabaa"
Explanation:
Remove an 'a' from the first group of 'a's to create "aabaaaa".
Remove two 'a's from the second group of 'a's to create "aabaa".
No three consecutive characters are equal, so return "aabaa".
Example 3:

Input: s = "aab"
Output: "aab"
Explanation: No three consecutive characters are equal, so return "aab".
 

Constraints:

1 <= s.length <= 105
s consists only of lowercase English letters.
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
    def leetcode(self, s: str) -> str:
        result = ""
        ll = len(s)
        current = s[0]
        start = 0
        count = 0
        more_than_3_flag = 0
        for ii in range(1,ll):
            #print(ii,s[ii], current)
            if s[ii] != current:
                current = s[ii]
                count = 0
                if more_than_3_flag == 1:
                    start = ii
                more_than_3_flag = 0
            else:
                count += 1
                if count == 2:
                    result += s[start:ii]
                    #print(2, result)
                    more_than_3_flag = 1

        if more_than_3_flag == 0:
            result += s[start:]
            #print(3, result)

        return result


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
