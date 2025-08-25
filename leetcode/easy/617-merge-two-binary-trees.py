"""
617. Merge Two Binary Trees
Easy
Topics
Companies
You are given two binary trees root1 and root2.

Imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not. You need to merge the two trees into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of the new tree.

Return the merged tree.

Note: The merging process must start from the root nodes of both trees.



Example 1:


Input: root1 = [1,3,2,5], root2 = [2,1,3,null,4,null,7]
Output: [3,4,5,5,4,null,7]
Example 2:

Input: root1 = [1], root2 = [1,2]
Output: [2,2]


Constraints:

The number of nodes in both trees is in the range [0, 2000].
-104 <= Node.val <= 104
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
    def leetcode(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 == None:
            return root2
        if root2 == None:
            return root1

        q1 = [root1]
        q2 = [root2]
        while q1:
            p1 = q1.pop(0)
            p2 = q2.pop(0)
            p1.val += p2.val

            if p1.left == None:
                p1.left = p2.left
            elif p2.left == None:
                pass
            else:
                q1.append(p1.left)
                q2.append(p2.left)

            if p1.right == None:
                p1.right = p2.right
            elif p2.right == None:
                pass
            else:
                q1.append(p1.right)
                q2.append(p2.right)


        return root1



if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
