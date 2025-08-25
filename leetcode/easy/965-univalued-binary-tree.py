"""
965. Univalued Binary Tree
Easy
Topics
Companies
A binary tree is uni-valued if every node in the tree has the same value.

Given the root of a binary tree, return true if the given tree is uni-valued, or false otherwise.



Example 1:


Input: root = [1,1,1,1,1,null,1]
Output: true
Example 2:


Input: root = [2,2,2,5,2]
Output: false


Constraints:

The number of nodes in the tree is in the range [1, 100].
0 <= Node.val < 100
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
    def leetcode(self, root: Optional[TreeNode]) -> bool:
        q = [root]
        while q:
            p = q.pop()
            if p.left:
                if p.left.val != p.val:
                    return False
                q.append(p.left)
            if p.right:
                if p.right.val != p.val:
                    return False
                q.append(p.right)

        return True


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
