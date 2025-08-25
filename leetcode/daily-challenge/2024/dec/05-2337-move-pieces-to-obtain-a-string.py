"""
2337. Move Pieces to Obtain a String
Medium
Topics
Companies
Hint
You are given two strings start and target, both of length n. Each string consists only of the characters 'L', 'R', and '_' where:

The characters 'L' and 'R' represent pieces, where a piece 'L' can move to the left only if there is a blank space directly to its left, and a piece 'R' can move to the right only if there is a blank space directly to its right.
The character '_' represents a blank space that can be occupied by any of the 'L' or 'R' pieces.
Return true if it is possible to obtain the string target by moving the pieces of the string start any number of times. Otherwise, return false.

 

Example 1:

Input: start = "_L__R__R_", target = "L______RR"
Output: true
Explanation: We can obtain the string target from start by doing the following moves:
- Move the first piece one step to the left, start becomes equal to "L___R__R_".
- Move the last piece one step to the right, start becomes equal to "L___R___R".
- Move the second piece three steps to the right, start becomes equal to "L______RR".
Since it is possible to get the string target from start, we return true.
Example 2:

Input: start = "R_L_", target = "__LR"
Output: false
Explanation: The 'R' piece in the string start can move one step to the right to obtain "_RL_".
After that, no pieces can move anymore, so it is impossible to obtain the string target from start.
Example 3:

Input: start = "_R", target = "R_"
Output: false
Explanation: The piece in the string start can move only to the right, so it is impossible to obtain the string target from start.
 

Constraints:

n == start.length == target.length
1 <= n <= 105
start and target consist of the characters 'L', 'R', and '_'.
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
    def leetcode(self, start: str, target: str) -> bool:
        lls = len(start)
        llt = len(target)
        indexs = 0
        indext = 0

        while indexs < lls and indext < llt:
            while indexs < lls:
                if start[indexs] == "_":
                    indexs += 1
                else:
                    break
            while indext < llt:
                if target[indext] == "_":
                    indext += 1
                else:
                    break

            if indexs >= lls or indext >= llt:
                break

            if start[indexs] == "L" and target[indext] == "L":
                if indexs < indext:
                    return False
            elif start[indexs] == "R" and target[indext] == "R":
                if indexs > indext:
                    return False
            else:
                return False

            indexs += 1
            indext += 1
        
        while indexs < lls:
            if start[indexs] == "_":
                indexs += 1
            else:
                return False
        while indext < llt:
            if target[indext] == "_":
                indext += 1
            else:
                return False

        return True


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
