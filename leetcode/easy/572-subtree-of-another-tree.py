"""
572. Subtree of Another Tree
Easy
Topics
Companies
Hint
Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.



Example 1:


Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true
Example 2:


Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
Output: false


Constraints:

The number of nodes in the root tree is in the range [1, 2000].
The number of nodes in the subRoot tree is in the range [1, 1000].
-104 <= root.val <= 104
-104 <= subRoot.val <= 104
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
    def leetcode(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sametree(root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
            if root1 == None and root2 == None:
                return True
            if root1 == None or root2 == None:
                return False
            q1 = [root1]
            q2 = [root2]
            while q1 and q2:
                p1 = q1.pop(0)
                p2 = q2.pop(0)

                if p1.val != p2.val:
                    return False

                if p1.left == None and p2.left == None:
                    pass
                elif p1.left == None or p2.left == None:
                    return False
                else:
                    q1.append(p1.left)
                    q2.append(p2.left)

                if p1.right == None and p2.right == None:
                    pass
                elif p1.right == None or p2.right == None:
                    return False
                else:
                    q1.append(p1.right)
                    q2.append(p2.right)

            if len(q1) or len(q2):
                return False

            return True

        if root == None:
            if subRoot == None:
                return True
            else:
                return False

        if subRoot == None:
            return False
        q = [root]
        while q:
            p = q.pop(0)
            if p.val == subRoot.val:
                print(p.val)
                if sametree(p,subRoot):
                    return True

            if p.left:
                q.append(p.left)
            if p.right:
                q.append(p.right)

        return False


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
