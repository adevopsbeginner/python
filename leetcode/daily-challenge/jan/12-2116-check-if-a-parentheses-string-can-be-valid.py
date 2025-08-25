"""

Code


Testcase
Testcase
Test Result
2116. Check if a Parentheses String Can Be Valid
Solved
Medium
Topics
Companies
Hint
A parentheses string is a non-empty string consisting only of '(' and ')'. It is valid if any of the following conditions is true:

It is ().
It can be written as AB (A concatenated with B), where A and B are valid parentheses strings.
It can be written as (A), where A is a valid parentheses string.
You are given a parentheses string s and a string locked, both of length n. locked is a binary string consisting only of '0's and '1's. For each index i of locked,

If locked[i] is '1', you cannot change s[i].
But if locked[i] is '0', you can change s[i] to either '(' or ')'.
Return true if you can make s a valid parentheses string. Otherwise, return false.

 

Example 1:


Input: s = "))()))", locked = "010100"
Output: true
Explanation: locked[1] == '1' and locked[3] == '1', so we cannot change s[1] or s[3].
We change s[0] and s[4] to '(' while leaving s[2] and s[5] unchanged to make s valid.
Example 2:

Input: s = "()()", locked = "0000"
Output: true
Explanation: We do not need to make any changes because s is already valid.
Example 3:

Input: s = ")", locked = "0"
Output: false
Explanation: locked permits us to change s[0]. 
Changing s[0] to either '(' or ')' will not make s valid.
 

Constraints:

n == s.length == locked.length
1 <= n <= 105
s[i] is either '(' or ')'.
locked[i] is either '0' or '1'.
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
    def leetcode(self, s: str, locked: str) -> bool:
        ll = len(s)

        if ll%2:
            return False

        count = 0
        count_p = 0
        for ii in range(ll):
            if locked[ii] == "1":
                if s[ii] == "(":
                    count  += 1
                    count_p += 1
                else:
                    if count < 1:
                        print(222)
                        return False
                    count_p -= 1
                    count  -= 1
            else:
                count += 1

        count = 0
        count_p = 0
        for ii in range(ll-1,-1,-1):
            if locked[ii] == "1":
                if s[ii] == ")":
                    count  += 1
                    count_p += 1
                else:
                    if count < 1:
                        print(222)
                        return False
                    count_p -= 1
                    count  -= 1
            else:
                count += 1

        return True


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
