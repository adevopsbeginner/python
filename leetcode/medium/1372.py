"""
1372. Longest ZigZag Path in a Binary Tree
Medium
Topics
￼
Companies
Hint
You are given the root of a binary tree.

A ZigZag path for a binary tree is defined as follow:

Choose any node in the binary tree and a direction (right or left).
If the current direction is right, move to the right child of the current node; otherwise, move to the left child.
Change the direction from right to left or from left to right.
Repeat the second and third steps until you can't move in the tree.
Zigzag length is defined as the number of nodes visited - 1. (A single node has a length of 0).

Return the longest ZigZag path contained in that tree.

 

Example 1:

￼
Input: root = [1,null,1,1,1,null,null,1,1,null,1,null,null,null,1]
Output: 3
Explanation: Longest ZigZag path in blue nodes (right -> left -> right).
Example 2:

￼
Input: root = [1,1,1,null,1,null,null,1,1,null,1]
Output: 4
Explanation: Longest ZigZag path in blue nodes (left -> right -> left -> right).
Example 3:

Input: root = [1]
Output: 0
 

Constraints:

The number of nodes in the tree is in the range [1, 5 * 104].
1 <= Node.val <= 100
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
    def leetcode(self, root: Optional[TreeNode]) -> int:
        q = [[root.left,0,"L"], [root.right, 0, "R"]]
        result = 0
        while q:
            p, depth, direction = q.pop(0)
            
            if p == None:
                continue
            
            #print(p.val, depth, direction, result)
            result = max(result, depth+1)

            if p.left:
                if direction == "L":
                    q.append([p.left, 0, "L"])
                else:
                    q.append([p.left, depth+1, "L"])
            if p.right:
                if direction == "L":
                    q.append([p.right, depth+1, "R"])
                else:
                    q.append([p.right, 0, "R"])


        return result


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
