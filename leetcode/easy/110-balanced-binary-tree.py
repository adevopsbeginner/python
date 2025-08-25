'''
110. Balanced Binary Tree
Solved
Easy
Topics
Companies
Given a binary tree, determine if it is 
height-balanced
.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: true
Example 2:


Input: root = [1,2,2,3,3,null,null,4,4]
Output: false
Example 3:

Input: root = []
Output: true
 

Constraints:

The number of nodes in the tree is in the range [0, 5000].
-104 <= Node.val <= 104

'''

from typing import List

# Definition for singly-linked list.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def leetcode(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True

        left  = self.depth(root.left)
        right = self.depth(root.right)

        if left == -1 or right == -1:
            return False
        
        if abs(left-right) <= 1:
            return True

        return False
        
    def depth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0

        ld = self.depth(root.left)
        rd = self.depth(root.right)

        if ld == -1 or rd == -1:
            return -1
       
        if abs(ld-rd) <= 1:
            return max(ld,rd)+1
        return -1

        

if __name__ == "__main__":
    app = Solution()
    a = [1,2,2,3,4,4,3]
    print(app.leetcode(a))
