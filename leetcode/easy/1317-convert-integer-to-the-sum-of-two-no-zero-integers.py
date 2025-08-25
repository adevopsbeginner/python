"""
1317. Convert Integer to the Sum of Two No-Zero Integers
Easy
Topics
Companies
Hint
No-Zero integer is a positive integer that does not contain any 0 in its decimal representation.

Given an integer n, return a list of two integers [a, b] where:

a and b are No-Zero integers.
a + b = n
The test cases are generated so that there is at least one valid solution. If there are many valid solutions, you can return any of them.

 

Example 1:

Input: n = 2
Output: [1,1]
Explanation: Let a = 1 and b = 1.
Both a and b are no-zero integers, and a + b = 2 = n.
Example 2:

Input: n = 11
Output: [2,9]
Explanation: Let a = 2 and b = 9.
Both a and b are no-zero integers, and a + b = 11 = n.
Note that there are other valid answers as [8, 3] that can be accepted.
 

Constraints:

2 <= n <= 104
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
    def leetcode(self, n: int) -> List[int]:
        if n <= 10:
            return [1,n-1]
        nn = n
        a = 0
        high = 0
        borrow = 0
        al = []
        while nn >= 10:
            al.append(1)
            if nn%10 == 0:
                borrow = 1
            elif nn%10 == 1:
                print(nn,a,borrow)
                if borrow == 0:
                    al[-1] += 1
                    borrow = 1
            elif nn%10 == 2:
                if borrow == 1:
                    al[-1] += 1
                    borrow = 1
            else:
                borrow = 0

            nn //= 10

        #print(al)
        while al:
            a = a*10+al.pop()

        b = n-a

        return [a,b]


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
