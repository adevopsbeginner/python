"""
653. Two Sum IV - Input is a BST
Easy
Topics
Companies
Given the root of a binary search tree and an integer k, return true if there exist two elements in the BST such that their sum is equal to k, or false otherwise.



Example 1:


Input: root = [5,3,6,2,4,null,7], k = 9
Output: true
Example 2:


Input: root = [5,3,6,2,4,null,7], k = 28
Output: false


Constraints:

The number of nodes in the tree is in the range [1, 104].
-104 <= Node.val <= 104
root is guaranteed to be a valid binary search tree.
-105 <= k <= 105
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
    def leetcode(self, root: Optional[TreeNode], k: int) -> bool:
        if root == None:
            return False
        q = [root]
        values = []
        while q:
            p = q.pop()
            values.append(p.val)
            if p.left:
                q.append(p.left)
            if p.right:
                q.append(p.right)
        ll = len(values)
        for ii in range(ll-1):
            if k-values[ii] in values[0:ii] or k-values[ii] in values[ii+1:]:
                return True

        return False


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
