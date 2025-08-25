'''
979. Distribute Coins in Binary Tree
Medium
Topics
Companies
You are given the root of a binary tree with n nodes where each node in the tree has node.val coins. There are n coins in total throughout the whole tree.

In one move, we may choose two adjacent nodes and move one coin from one node to another. A move may be from parent to child, or from child to parent.

Return the minimum number of moves required to make every node have exactly one coin.



Example 1:


Input: root = [3,0,0]
Output: 2
Explanation: From the root of the tree, we move one coin to its left child, and one coin to its right child.
Example 2:


Input: root = [0,3,0]
Output: 3
Explanation: From the left child of the root, we move two coins to the root [taking two moves]. Then, we move one coin from the root of the tree to the right child.


Constraints:

The number of nodes in the tree is n.
1 <= n <= 100
0 <= Node.val <= n
The sum of all Node.val is n.
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
    def leetcode(self, root: Optional[TreeNode]) -> int:
        nodesum,nodecount,abs_sum_minus_count = self.a(root)
        return abs_sum_minus_count

    def a(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return [0,0,0]
        if root.left == None and root.right == None:
            return [root.val,1,abs(root.val-1)]
        l1,l2,l3 = self.a(root.left)
        r1,r2,r3 = self.a(root.right)

        return [(l1+r1+root.val),(l2+r2+1),abs((l1+r1+root.val)-(l2+r2+1))+(l3+r3)]

if __name__ == "__main__":
    app = Solution()
    a = 2
    print(app.leetcode(a))
