"""
2390. Removing Stars From a String
Medium
Topics
Companies
Hint
You are given a string s, which contains stars *.

In one operation, you can:

Choose a star in s.
Remove the closest non-star character to its left, as well as remove the star itself.
Return the string after all stars have been removed.

Note:

The input will be generated such that the operation is always possible.
It can be shown that the resulting string will always be unique.
 

Example 1:

Input: s = "leet**cod*e"
Output: "lecoe"
Explanation: Performing the removals from left to right:
- The closest character to the 1st star is 't' in "leet**cod*e". s becomes "lee*cod*e".
- The closest character to the 2nd star is 'e' in "lee*cod*e". s becomes "lecod*e".
- The closest character to the 3rd star is 'd' in "lecod*e". s becomes "lecoe".
There are no more stars, so we return "lecoe".
Example 2:

Input: s = "erase*****"
Output: ""
Explanation: The entire string is removed, so we return an empty string.
 

Constraints:

1 <= s.length <= 105
s consists of lowercase English letters and stars *.
The operation above can be performed on s.
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
    def removeStars(self, s: str) -> str:
        # Use a stack to keep track of characters
        stack = []
        
        # Process each character in the string
        for char in s:
            if char == '*':
                # If we encounter a star, remove the top element from the stack
                # (which is the closest non-star character to the left)
                if stack:  # Check if stack is not empty
                    stack.pop()
            else:
                # If it's not a star, add it to the stack
                stack.append(char)
        
        # Join the remaining characters in the stack to form the result
        return ''.join(stack)
    
        ### mine
        result = []
        for each in s:
            if each == "*":
                if result:
                    result.pop()
            else:
                result.append(each)
        return "".join(result)

if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
