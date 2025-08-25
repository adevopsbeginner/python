"""

Code
Testcase
Test Result
Test Result
993. Cousins in Binary Tree
Solved
Easy
Topics
Companies
Given the root of a binary tree with unique values and the values of two different nodes of the tree x and y, return true if the nodes corresponding to the values x and y in the tree are cousins, or false otherwise.

Two nodes of a binary tree are cousins if they have the same depth with different parents.

Note that in a binary tree, the root node is at the depth 0, and children of each depth k node are at the depth k + 1.



Example 1:


Input: root = [1,2,3,4], x = 4, y = 3
Output: false
Example 2:


Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
Output: true
Example 3:


Input: root = [1,2,3,null,4], x = 2, y = 3
Output: false


Constraints:

The number of nodes in the tree is in the range [2, 100].
1 <= Node.val <= 100
Each node has a unique value.
x != y
x and y are exist in the tree.
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
    def leetcode(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        q = [[root,0]]
        dx = -1
        dy = -1
        while q:
            p,d = q.pop()
            if p == None:
                return False
            if p.val == x:
                dx = d
            if p.val == y:
                dy = d

            if p.left and p.right:
                if p.left.val == x and p.right.val == y:
                    return False
                if p.left.val == y and p.right.val == x:
                    return False

            if dx >= 0 and dy >= 0:
                if dx == dy:
                    return True

            if p.left:
                q.append([p.left,d+1])
            if p.right:
                q.append([p.right,d+1])

        return False


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
