"""

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
        ll = len(s)
        result = 0
        for ii in range(ll//2):
            if s[ii*2] == "1" and s[ii*2+1] == "0":
                result += 1
            if s[ii*2] == "0" and s[ii*2+1] == "1":
                result += 1
        return result


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
