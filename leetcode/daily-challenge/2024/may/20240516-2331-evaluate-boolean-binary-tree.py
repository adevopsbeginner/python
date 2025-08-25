'''
2331. Evaluate Boolean Binary Tree
Solved
Easy
Topics
Companies
Hint
You are given the root of a full binary tree with the following properties:

Leaf nodes have either the value 0 or 1, where 0 represents False and 1 represents True.
Non-leaf nodes have either the value 2 or 3, where 2 represents the boolean OR and 3 represents the boolean AND.
The evaluation of a node is as follows:

If the node is a leaf node, the evaluation is the value of the node, i.e. True or False.
Otherwise, evaluate the node's two children and apply the boolean operation of its value with the children's evaluations.
Return the boolean result of evaluating the root node.

A full binary tree is a binary tree where each node has either 0 or 2 children.

A leaf node is a node that has zero children.

 

Example 1:


Input: root = [2,1,3,null,null,0,1]
Output: true
Explanation: The above diagram illustrates the evaluation process.
The AND node evaluates to False AND True = False.
The OR node evaluates to True OR False = True.
The root node evaluates to True, so we return true.
Example 2:

Input: root = [0]
Output: false
Explanation: The root node is a leaf node and it evaluates to false, so we return false.
 

Constraints:

The number of nodes in the tree is in the range [1, 1000].
0 <= Node.val <= 3
Every node has either 0 or 2 children.
Leaf nodes have a value of 0 or 1.
Non-leaf nodes have a value of 2 or 3.
'''

import string
from typing import List
from collections import defaultdict

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def leetcode(self, root: Optional[TreeNode]) -> bool:
        if root.val == 0:
            return False
        elif root.val == 1:
            return True
        elif root.val == 2:
            if root.left.val == 1 or root.right.val == 1:
                return True
            elif root.left.val == 0 and root.right.val == 0:
                return False
            else:
                return self.evaluateTree(root.left) or self.evaluateTree(root.right)

        elif root.val == 3:
            if root.left.val == 1 and root.right.val == 1:
                return True
            elif root.left.val == 0 or root.right.val == 0:
                return False
            else:
                return self.evaluateTree(root.left) and self.evaluateTree(root.right)

if __name__ == "__main__":
    app = Solution()
    a = 2
    print(app.leetcode(a))
