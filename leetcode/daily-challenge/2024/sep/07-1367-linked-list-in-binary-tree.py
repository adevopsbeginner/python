"""
1367. Linked List in Binary Tree
Attempted
Medium
Topics
Companies
Hint
Given a binary tree root and a linked list with head as the first node.

Return True if all the elements in the linked list starting from the head correspond to some downward path connected in the binary tree otherwise return False.

In this context downward path means a path that starts at some node and goes downwards.



Example 1:



Input: head = [4,2,8], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
Output: true
Explanation: Nodes in blue form a subpath in the binary Tree.
Example 2:



Input: head = [1,4,2,6], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
Output: true
Example 3:

Input: head = [1,4,2,6,8], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
Output: false
Explanation: There is no path in the binary tree that contains all the elements of the linked list from head.


Constraints:

The number of nodes in the tree will be in the range [1, 2500].
The number of nodes in the list will be in the range [1, 100].
1 <= Node.val <= 100 for each node in the linked list and binary tree.
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
    def leetcode(self,     # Helper function to check if the current tree node can match the linked list node
    def dfs(tree_node, list_node):
        if list_node is None:  # If we've matched the entire linked list, return True
            return True
        if tree_node is None:  # If we run out of tree nodes, return False
            return False
        if tree_node.val != list_node.val:  # If the values don't match, return False
            return False
        # Recursively check left and right children
        return dfs(tree_node.left, list_node.next) or dfs(tree_node.right, list_node.next)

    if root is None:
        return False
    # Start checking from the root node or any node in the tree
    return dfs(root, head) or isSubPath(head, root.left) or isSubPath(head, root.right)


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
