"""
783. Minimum Distance Between BST Nodes
Easy
Topics
Companies
Given the root of a Binary Search Tree (BST), return the minimum difference between the values of any two different nodes in the tree.



Example 1:


Input: root = [4,2,6,1,3]
Output: 1
Example 2:


Input: root = [1,0,48,null,null,12,49]
Output: 1


Constraints:

The number of nodes in the tree is in the range [2, 100].
0 <= Node.val <= 105


Note: This question is the same as 530: https://leetcode.com/problems/minimum-absolute-difference-in-bst/
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
    def leetcode(self, root: Optional[TreeNode]) -> int:
        nodes = []
        q = [root]
        while q:
            p = q.pop()
            nodes.append(p.val)
            if p.left:
                q.append(p.left)
            if p.right:
                q.append(p.right)
        nodes.sort()

        result = nodes[1] - nodes[0]
        ll = len(nodes)
        for ii in range(2,ll):
            result = min(result, nodes[ii] - nodes[ii-1])
        return result


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
