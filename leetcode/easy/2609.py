"""

Code
Testcase
Test Result
Test Result
2609. Find the Longest Balanced Substring of a Binary String
Easy
Topics
premium lock icon
Companies
Hint
You are given a binary string s consisting only of zeroes and ones.

A substring of s is considered balanced if all zeroes are before ones and the number of zeroes is equal to the number of ones inside the substring. Notice that the empty substring is considered a balanced substring.

Return the length of the longest balanced substring of s.

A substring is a contiguous sequence of characters within a string.

 

Example 1:

Input: s = "01000111"
Output: 6
Explanation: The longest balanced substring is "000111", which has length 6.
Example 2:

Input: s = "00111"
Output: 4
Explanation: The longest balanced substring is "0011", which has length 4. 
Example 3:

Input: s = "111"
Output: 0
Explanation: There is no balanced substring except the empty substring, so the answer is 0.
 

Constraints:

1 <= s.length <= 50
'0' <= s[i] <= '1'
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
        count0 = 0
        count1 = 0
        ll = len(s)
        result = 0
        for ii in range(ll):
            #print(ii, count0, count1)
            if s[ii] == "0":
                if count1 > 0:
                    result = max(result, 2*min(count0, count1))
                    count1 = 0
                    count0 = 1
                else:
                    count0 += 1
            else:
                count1 += 1

        if count1 > 0:
            result = max(result, 2*min(count0, count1))
        
        
        return result



if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
