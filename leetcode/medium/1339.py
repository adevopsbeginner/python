"""
1339. Maximum Product of Splitted Binary Tree
Medium
Topics
premium lock icon
Companies
Hint
Given the root of a binary tree, split the binary tree into two subtrees by removing one edge such that the product of the sums of the subtrees is maximized.

Return the maximum product of the sums of the two subtrees. Since the answer may be too large, return it modulo 109 + 7.

Note that you need to maximize the answer before taking the mod and not after taking it.

 

Example 1:


Input: root = [1,2,3,4,5,6]
Output: 110
Explanation: Remove the red edge and get 2 binary trees with sum 11 and 10. Their product is 110 (11*10)
Example 2:


Input: root = [1,null,2,3,4,null,null,5,6]
Output: 90
Explanation: Remove the red edge and get 2 binary trees with sum 15 and 6.Their product is 90 (15*6)
 

Constraints:

The number of nodes in the tree is in the range [2, 5 * 104].
1 <= Node.val <= 104
"""

import string
import heapq
from typing import List
from collections import defaultdict

class Solution:
    def leetcode(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if root == None:
                return 0
            if root.left == None and root.right == None:
                return root.val
            
            root.val += dfs(root.left) + dfs(root.right)

            return root.val

        root.val = dfs(root)
        
        result = 0
        q = [root]
        while q:
            p = q.pop()
            #print(p.val)
            result = max(result, p.val*(root.val-p.val))
            if p.left:
                q.append(p.left)
            if p.right:
                q.append(p.right)

        return result%(10**9+7)
        