"""
1161. Maximum Level Sum of a Binary Tree
Medium
Topics
premium lock icon
Companies
Hint
Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.

Return the smallest level x such that the sum of all the values of nodes at level x is maximal.

 

Example 1:


Input: root = [1,7,0,7,-8,null,null]
Output: 2
Explanation: 
Level 1 sum = 1.
Level 2 sum = 7 + 0 = 7.
Level 3 sum = 7 + -8 = -1.
So we return the level with the maximum sum which is level 2.
Example 2:

Input: root = [989,null,10250,98693,-89388,null,null,null,-32127]
Output: 2
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
-105 <= Node.val <= 105
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
    def leetcode(self, root: Optional[TreeNode]) -> int:
        level_sum = [0]*100
        ll = 100
        q = [[root,1]]
        max_level = 1
        while q:
            p,l = q.pop(0)
            max_level = max(max_level, l)
            if l > ll:
                level_sum += [0]
                ll += 1
            level_sum[l] += p.val
            if p.left:
                q.append([p.left, l+1])
            if p.right:
                q.append([p.right, l+1])

        #print(level_sum)
        max_level_sum = max(level_sum[1:max_level+1])
        for ii in range(1, max_level+1):
            if level_sum[ii] == max_level_sum:
                return ii
        return 1


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
