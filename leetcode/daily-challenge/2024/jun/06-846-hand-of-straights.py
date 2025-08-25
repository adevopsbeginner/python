"""

Code
Testcase
Test Result
Test Result
846. Hand of Straights
Medium
Topics
Companies
Alice has some number of cards and she wants to rearrange the cards into groups so that each group is of size groupSize, and consists of groupSize consecutive cards.

Given an integer array hand where hand[i] is the value written on the ith card and an integer groupSize, return true if she can rearrange the cards, or false otherwise.



Example 1:

Input: hand = [1,2,3,6,2,3,4,7,8], groupSize = 3
Output: true
Explanation: Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8]
Example 2:

Input: hand = [1,2,3,4,5], groupSize = 4
Output: false
Explanation: Alice's hand can not be rearranged into groups of 4.



Constraints:

1 <= hand.length <= 104
0 <= hand[i] <= 109
1 <= groupSize <= hand.length
"""

import string
from typing import List
from collections import defaultdict

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def leetcode(self, hand: List[int], groupSize: int) -> bool:
        ll = len(hand)
        if ll % groupSize:
            return False
        lg = []
        hand.sort()
        # print(hand)
        for ii in range(ll//groupSize):
            lg = [0]
            for jj in range(1,groupSize):
                for kk in range(1,len(hand)):
                    # print(ii,jj,kk,lg,hand)
                    if hand[kk] == hand[lg[-1]]+1:
                        lg.append(kk)
                    if hand[kk] > hand[lg[-1]]+1:
                        return False
                    if len(lg) == groupSize:
                        break
            if len(lg) != groupSize:
                return False
            lg = lg[::-1]
            for each in lg:
                hand.pop(each)
            # print(hand)

        return True

if __name__ == "__main__":
    app = Solution()
    a = ["bella","label","roller"]
    a = [1,2,3,6,2,3,4,7,8]
    b = 3
    print(app.leetcode(a,b))
