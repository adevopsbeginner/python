"""
236. Lowest Common Ancestor of a Binary Tree
Medium
Topics
￼
Companies
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

 

Example 1:

￼
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.
Example 2:

￼
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
Example 3:

Input: root = [1,2], p = 1, q = 2
Output: 1
 

Constraints:

The number of nodes in the tree is in the range [2, 105].
-109 <= Node.val <= 109
All Node.val are unique.
p != q
p and q will exist in the tree.
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
    def leetcode(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        pathp = []
        pathq = []
        qq = [[root, []]]
        while qq:
            pp, path = qq.pop(0)
            if pp == None:
                continue
            #print(pp.val, bfspath)
            bfspath = path[:]

            ### new path
            bfspath.append(pp)

            #print("path", [n.val for n in bfspath])
            #print(pp.val, p.val, q.val)

            ### found path for p
            if pp.val == p.val:
                if pathp == []:
                    pathp = bfspath[:]
            
            ### found path for q
            if pp.val == q.val:
                if pathq == []:
                    pathq = bfspath[:]

            if len(pathp) > 0 and len(pathq) > 0:
                break

            if pp.left:
                qq.append([pp.left, bfspath])
            if pp.right:
                qq.append([pp.right, bfspath])
        
        ### find out the last same node which is the lowest common ancestor
        llp = len(pathp)
        llq = len(pathq)
        #print("p", llp, [n.val for n in pathp])
        #print("q", llq, [n.val for n in pathq])
        if llq == 0 or llq == 0:
            return None

        ll = min(llp, llq)
        for ii in range(ll):
            if pathp[ii] != pathq[ii]:
                return pathp[ii-1]
        
        ### p is ancestor of q
        if llp > llq:
            return pathp[ll-1]
        
        ### q is ancestor of p
        elif llp < llq:
            return pathq[ll-1]
        
        return pathp[-1]


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
