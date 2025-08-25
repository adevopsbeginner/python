"""
226. Invert Binary Tree
Solved
Easy
Topics
Companies
Given the root of a binary tree, invert the tree, and return its root.



Example 1:


Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]
Example 2:


Input: root = [2,1,3]
Output: [2,3,1]
Example 3:

Input: root = []
Output: []


Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
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
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return None
        q = [root]
        while q:
            p = q.pop()
            p.left, p.right = p.right, p.left
            if p.left:
                q.append(p.left)
            if p.right:
                q.append(p.right)

        return root

if __name__ == "__main__":
    app = Solution()
    a = 2
    print(app.leetcode(a))
