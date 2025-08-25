"""
1028. Recover a Tree From Preorder Traversal
Hard
Topics
Companies
Hint
We run a preorder depth-first search (DFS) on the root of a binary tree.

At each node in this traversal, we output D dashes (where D is the depth of this node), then we output the value of this node.  If the depth of a node is D, the depth of its immediate child is D + 1.  The depth of the root node is 0.

If a node has only one child, that child is guaranteed to be the left child.

Given the output traversal of this traversal, recover the tree and return its root.

 

Example 1:


Input: traversal = "1-2--3--4-5--6--7"
Output: [1,2,5,3,4,6,7]
Example 2:


Input: traversal = "1-2--3---4-5--6---7"
Output: [1,2,5,3,null,6,null,4,null,7]
Example 3:


Input: traversal = "1-401--349---90--88"
Output: [1,401,null,349,88,90]
 

Constraints:

The number of nodes in the original tree is in the range [1, 1000].
1 <= Node.val <= 109
"""

import string
import heapq
from typing import List
from collections import defaultdict

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        traversal += "-"
        ll = len(traversal)
        if ll == 0:
            return None
        
        number = 0
        ii = 0
        while ii < ll:
            if traversal[ii] == "-":
                break
            else:
                number = number*10 + int(traversal[ii])
            ii += 1
        ii -= 1
        #print(ii, number)

        root = TreeNode(number)
        number = 0
        current = root
        level = 0
        q = [[root, 0]]
        count = 0
        while ii < ll-1:
            ii += 1
            if traversal[ii] == "-":
                if number <= 0:
                    count += 1
                    continue
            
                #print(number, count, level, level+1)
                node = TreeNode(number)
                if count > level+1:
                    return root
                elif count == level+1:
                    current.left = node
                    q.append([current, level])
                    level += 1
                    current = node
                else:
                    while count < level+1:
                        #print(ii, traversal[ii], count, level, level+1)
                        current, level = q.pop()
                    current.right = node
                    q.append([current, level])
                    level += 1
                    current = node

                number = 0
                count = 1
            else:
                number = number*10 + int(traversal[ii])

        return root
