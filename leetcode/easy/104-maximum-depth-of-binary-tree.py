'''
104. Maximum Depth of Binary Tree
Solved
Easy
Topics
Companies
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 3
Example 2:

Input: root = [1,null,2]
Output: 2
 

Constraints:

The number of nodes in the tree is in the range [0, 104].
-100 <= Node.val <= 100

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

        q = [[root,0]]
        result = 0
        while q:
            index = q.pop(0)
            if index[0] == None:
                continue
            if index[0].left == None and index[0].right == None:
                result = max(result,index[1]+1)
            if index[0].left:
                q.append([index[0].left,index[1]+1])
            if index[0].right:
                q.append([index[0].right,index[1]+1])
        return result

if __name__ == "__main__":
    app = Solution()
    a = [1,2,2,3,4,4,3]
    print(app.leetcode(a))
