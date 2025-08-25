"""
1046. Last Stone Weight
Easy
Topics
Companies
Hint
You are given an array of integers stones where stones[i] is the weight of the ith stone.

We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together. Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:

If x == y, both stones are destroyed, and
If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
At the end of the game, there is at most one stone left.

Return the weight of the last remaining stone. If there are no stones left, return 0.



Example 1:

Input: stones = [2,7,4,1,8,1]
Output: 1
Explanation:
We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of the last stone.
Example 2:

Input: stones = [1]
Output: 1


Constraints:

1 <= stones.length <= 30
1 <= stones[i] <= 1000
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
    def leetcode(self, stones: List[int]) -> int:
        ll = len(stones)
        stones.sort(reverse=True) ### from bigest to smallest
        index = 1
        while index < ll:
            #print(index,stones)
            smash = stones[index-1] - stones[index]
            stones[index] = smash
            if smash == 0:        ### destroyed
                index += 2
                continue
            
            #index += 1
            if index >= ll-1:
                return smash      ### finish
            elif stones[index+1] == 0:
                return smash      ### no more smash needed, finish
            else:
                ii = index
                while stones[ii] < stones[ii+1]:
                    stones[ii], stones[ii+1] = stones[ii+1], stones[ii]
                    ii += 1
                    if ii == ll-1: ### the end
                        break
                index += 1

        return stones[-1]


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
