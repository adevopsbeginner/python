"""
1448. Count Good Nodes in Binary Tree
Solved
Medium
Topics
￼
Companies
Hint
Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.

 

Example 1:

￼

Input: root = [3,1,4,3,null,1,5]
Output: 4
Explanation: Nodes in blue are good.
Root Node (3) is always a good node.
Node 4 -> (3,4) is the maximum value in the path starting from the root.
Node 5 -> (3,4,5) is the maximum value in the path
Node 3 -> (3,1,3) is the maximum value in the path.
Example 2:

￼

Input: root = [3,3,null,4,2]
Output: 3
Explanation: Node 2 -> (3, 3, 2) is not good, because "3" is higher than it.
Example 3:

Input: root = [1]
Output: 1
Explanation: Root is considered as good.
 

Constraints:

The number of nodes in the binary tree is in the range [1, 10^5].
Each node's value is between [-10^4, 10^4].
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
    def leetcode(self, root: TreeNode) -> int:
        """
        :type root: TreeNode
        :rtype: int
        """
        sum = 0
        if root == None:
            return sum
        stack = [[root,0]]
        val = []
        while len(stack):
            current,level = stack.pop()
            while len(val) > level:
                val.pop()
            
            val.append(current.val)
            if current.val == max(val):
                #print(current.val,val,sum)
                sum +=1

            if current.right:
                stack.append([current.right,level+1])
            if current.left:
                stack.append([current.left,level+1])

        return sum


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
