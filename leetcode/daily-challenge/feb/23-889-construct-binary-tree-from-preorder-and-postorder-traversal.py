"""
889. Construct Binary Tree from Preorder and Postorder Traversal
Solved
Medium
Topics
Companies
Given two integer arrays, preorder and postorder where preorder is the preorder traversal of a binary tree of distinct values and postorder is the postorder traversal of the same tree, reconstruct and return the binary tree.

If there exist multiple answers, you can return any of them.

 

Example 1:


Input: preorder = [1,2,4,5,3,6,7], postorder = [4,5,2,6,7,3,1]
Output: [1,2,3,4,5,6,7]
Example 2:

Input: preorder = [1], postorder = [1]
Output: [1]
 

Constraints:

1 <= preorder.length <= 30
1 <= preorder[i] <= preorder.length
All the values of preorder are unique.
postorder.length == preorder.length
1 <= postorder[i] <= postorder.length
All the values of postorder are unique.
It is guaranteed that preorder and postorder are the preorder traversal and postorder traversal of the same binary tree.
"""

import string
import heapq
from typing import List
from collections import defaultdict

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        ll = len(preorder)
        if ll == 0:
            return None
        if preorder[0] != postorder[-1]:
            print("root error")
            return None
        root = TreeNode(preorder[0])
        
        if ll == 1:
            return root
        if ll == 2:
            root.left = TreeNode(preorder[1])
            return root
        # if ll == 3:
        #     root.left = TreeNode(preorder[1])
        #     root.right = TreeNode(preorder[2])
        #     return root

        for ii in range(ll-1):
            if preorder[1] == postorder[ii]:
                #print("left", preorder[1:ii+2], postorder[0:ii+1])
                root.left = self.constructFromPrePost(preorder[1:ii+2], postorder[0:ii+1])
                #print("right", preorder[ii+2:], postorder[ii+1:ll-1])
                root.right = self.constructFromPrePost(preorder[ii+2:], postorder[ii+1:ll-1])
            # if preorder[ii] == postorder[ll-2]:
            #     print("right", preorder[ii:], postorder[ii-1:ll-1])
            #     root.right = self.constructFromPrePost(preorder[ii:], postorder[ii-1:ll-1])
        return root


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
