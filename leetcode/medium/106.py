"""
106. Construct Binary Tree from Inorder and Postorder Traversal
Solved
Medium
Topics
premium lock icon
Companies
Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and postorder is the postorder traversal of the same tree, construct and return the binary tree.

 

Example 1:


Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
Output: [3,9,20,null,null,15,7]
Example 2:

Input: inorder = [-1], postorder = [-1]
Output: [-1]
 

Constraints:

1 <= inorder.length <= 3000
postorder.length == inorder.length
-3000 <= inorder[i], postorder[i] <= 3000
inorder and postorder consist of unique values.
Each value of postorder also appears in inorder.
inorder is guaranteed to be the inorder traversal of the tree.
postorder is guaranteed to be the postorder traversal of the tree.
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
    def leetcode(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        ll = len(inorder)
        if ll == 0:
            return None
        root = TreeNode()
        root.val = postorder[-1]
        root.left = root.right = None
        for ii in range(ll):
            if inorder[ii] == root.val:
                if ii > 0:
                    root.left = self.buildTree(inorder[:ii],postorder[:ii])
                if ii < ll-1:
                    root.right = self.buildTree(inorder[ii+1:],postorder[ii:ll-1])
        return root


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
