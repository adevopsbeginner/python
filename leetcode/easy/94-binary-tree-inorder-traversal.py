'''
94. Binary Tree Inorder Traversal
Solved
Easy
Topics
Companies
Given the root of a binary tree, return the inorder traversal of its nodes' values.

 

Example 1:


Input: root = [1,null,2,3]
Output: [1,3,2]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [1]
Output: [1]
 

Constraints:

The number of nodes in the tree is in the range [0, 100].
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
    def leetcode(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        result = []
        q = [root]                          ### queuein first
        while q:                            ### reverse queue, operation from the end
            index = q.pop()                 ### q[-1]
            if index.right:                 ### leave right to last
                q.append(index.right)
                index.right = None
            if index.left == None:          ### left finished
                result.append(index.val)
            else:
                q.append(index)             ### queue root in
                q.append(index.left)        ### queue left in, which will be handled at first
                index.left = None           ### cleanup root node

        return result

if __name__ == "__main__":
    app = Solution()
    a = [1,null,2,3]
    print(app.leetcode(a))
