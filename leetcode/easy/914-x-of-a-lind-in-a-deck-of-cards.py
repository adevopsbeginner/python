"""
914. X of a Kind in a Deck of Cards
Easy
Topics
Companies
You are given an integer array deck where deck[i] represents the number written on the ith card.

Partition the cards into one or more groups such that:

Each group has exactly x cards where x > 1, and
All the cards in one group have the same integer written on them.
Return true if such partition is possible, or false otherwise.



Example 1:

Input: deck = [1,2,3,4,4,3,2,1]
Output: true
Explanation: Possible partition [1,1],[2,2],[3,3],[4,4].
Example 2:

Input: deck = [1,1,1,2,2,2,3,3]
Output: false
Explanation: No possible partition.


Constraints:

1 <= deck.length <= 104
0 <= deck[i] < 104
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
    def leetcode(self, deck: List[int]) -> bool:
        ll = len(deck)
        if ll == 1:
            return False
        dd = defaultdict(int)
        for each in deck:
            dd[each] += 1

        mineach = ll
        for each in deck:
            mineach = min(mineach, dd[each])
        for ii in range(2,mineach+1):
            if mineach % ii:
                continue
            flag = 0
            for each in deck:
                if dd[each] % ii:
                    flag = 1
                    break
            if flag == 0:
                return True
        return False


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
