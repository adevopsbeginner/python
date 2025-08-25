"""
872. Leaf-Similar Trees
Easy
Topics
Companies
Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence.



For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

Two binary trees are considered leaf-similar if their leaf value sequence is the same.

Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.



Example 1:


Input: root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
Output: true
Example 2:


Input: root1 = [1,2,3], root2 = [1,3,2]
Output: false


Constraints:

The number of nodes in each tree will be in the range [1, 200].
Both of the given trees will have values in the range [0, 200].
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
    def leetcode(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        q = [root1]
        leaf1 = []
        while q:
            p = q.pop()
            if p.left == None and p.right == None:
                leaf1.append(p.val)
                continue
            if p.right:
                q.append(p.right)
            if p.left:
                q.append(p.left)

        q = [root2]
        leaf2 = []
        while q:
            p = q.pop()
            if p.left == None and p.right == None:
                leaf2.append(p.val)
                continue
            if p.right:
                q.append(p.right)
            if p.left:
                q.append(p.left)

        ll1 = len(leaf1)
        ll2 = len(leaf2)
        #print(leaf1,leaf2)
        if ll1-ll2:
            return False
        for ii in range(ll1):
            if leaf1[ii] != leaf2[ii]:
                return False

        return True


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
