'''
111. Minimum Depth of Binary Tree
Solved
Easy
Topics
Companies
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 2
Example 2:

Input: root = [2,null,3,null,4,null,5,null,6]
Output: 5
 

Constraints:

The number of nodes in the tree is in the range [0, 105].
-1000 <= Node.val <= 1000

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
             return 0
        if root.left == None and root.right == None:
            return 1
        if root.left == None:
            return self.minDepth(root.right)+1
        if root.right == None:
            return self.minDepth(root.left)+1

        return min(self.minDepth(root.left), self.minDepth(root.right))+1

        

if __name__ == "__main__":
    app = Solution()
    a = [1,2,2,3,4,4,3]
    print(app.leetcode(a))
