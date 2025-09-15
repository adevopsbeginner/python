"""
102. Binary Tree Level Order Traversal
Medium
Topics
premium lock icon
Companies
Hint
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 2000].
-1000 <= Node.val <= 1000
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
    def leetcode(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        q = [[root,0]]
        current_level = -1
        result = []
        current_level_list = []
        while q:
            p, level = q.pop(0)
            if level != current_level:
                if len(current_level_list):
                    result.append(current_level_list)
                    current_level_list = []

            current_level_list.append(p.val)
            current_level = level

            if p.left:
                q.append([p.left,level+1])
            if p.right:
                q.append([p.right,level+1])

        if len(current_level_list):
            result.append(current_level_list)

        return result


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
