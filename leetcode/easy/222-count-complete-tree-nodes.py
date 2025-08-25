"""
222. Count Complete Tree Nodes
Solved
Easy
Topics
Companies
Given the root of a complete binary tree, return the number of the nodes in the tree.

According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Design an algorithm that runs in less than O(n) time complexity.



Example 1:


Input: root = [1,2,3,4,5,6]
Output: 6
Example 2:

Input: root = []
Output: 0
Example 3:

Input: root = [1]
Output: 1


Constraints:

The number of nodes in the tree is in the range [0, 5 * 104].
0 <= Node.val <= 5 * 104
The tree is guaranteed to be complete.
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
    def leetcode(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        q = [root]
        count = 0
        while q:
            p = q.pop()
            count += 1
            if p.left:
                q.append(p.left)
            if p.right:
                q.append(p.right)
        return count

if __name__ == "__main__":
    app = Solution()
    a = 2
    print(app.leetcode(a))
