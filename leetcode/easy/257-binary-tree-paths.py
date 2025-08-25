"""
257. Binary Tree Paths
Solved
Easy
Topics
Companies
Given the root of a binary tree, return all root-to-leaf paths in any order.

A leaf is a node with no children.

 

Example 1:


Input: root = [1,2,3,null,5]
Output: ["1->2->5","1->3"]
Example 2:

Input: root = [1]
Output: ["1"]
 

Constraints:

The number of nodes in the tree is in the range [1, 100].
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
    def leetcode(self, root: Optional[TreeNode]) -> List[str]:
        result = []
        if root == None:
            return result

        q = [[root,[]]]
        while q:
            node,path = q.pop(0)
            # path.append(str(node.val))
            newpath = path+[str(node.val)]
            if node.left == None and node.right == None:
                result.append("->".join(newpath))

            if node.left:
                q.append([node.left, newpath])
            if node.right:
                q.append([node.right, newpath])

        return result

if __name__ == "__main__":
    app = Solution()
    a = [0,1,2,4,5,7]
    print(app.leetcode(a))
