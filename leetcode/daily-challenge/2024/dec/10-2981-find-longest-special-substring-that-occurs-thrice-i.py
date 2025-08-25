"""
2981. Find Longest Special Substring That Occurs Thrice I
Medium
Topics
Companies
Hint
You are given a string s that consists of lowercase English letters.

A string is called special if it is made up of only a single character. For example, the string "abc" is not special, whereas the strings "ddd", "zz", and "f" are special.

Return the length of the longest special substring of s which occurs at least thrice, or -1 if no special substring occurs at least thrice.

A substring is a contiguous non-empty sequence of characters within a string.

 

Example 1:

Input: s = "aaaa"
Output: 2
Explanation: The longest special substring which occurs thrice is "aa": substrings "aaaa", "aaaa", and "aaaa".
It can be shown that the maximum length achievable is 2.
Example 2:

Input: s = "abcdef"
Output: -1
Explanation: There exists no special substring which occurs at least thrice. Hence return -1.
Example 3:

Input: s = "abcaba"
Output: 1
Explanation: The longest special substring which occurs thrice is "a": substrings "abcaba", "abcaba", and "abcaba".
It can be shown that the maximum length achievable is 1.
 

Constraints:

3 <= s.length <= 50
s consists of only lowercase English letters.
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
    def leetcode(self, s: str) -> int:
        s += "A"
        ll = len(s)
        dd = defaultdict(list)
        count = 1
        for ii in range(1,ll):
            if s[ii] == s[ii-1]:
                count += 1
            else:
                dd[s[ii-1]].append(count)
                count = 1
        #print(dd)
        result = -1
        for key in dd:
            llv = len(dd[key])
            dd[key].append(0)
            dd[key].append(0)
            dd[key].sort(reverse=True)
            for ii in range(llv):
                #print(result,key,ii,dd[key],dd[key][ii])
                if dd[key][ii] < result:
                    break
                if dd[key][ii] == dd[key][ii+1] and dd[key][ii] == dd[key][ii+2]:
                    result = max(result,dd[key][ii])
                    break
                if dd[key][ii] == dd[key][ii+1] or dd[key][ii] == dd[key][ii+1]+1:
                    if dd[key][ii] >= 2:
                        result = max(result,dd[key][ii]-1)
                if dd[key][ii] >= 3:
                    result = max(result,dd[key][ii]-2)

        return result


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
