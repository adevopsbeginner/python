"""
543. Diameter of Binary Tree
Easy
Topics
Companies
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.



Example 1:


Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
Example 2:

Input: root = [1,2]
Output: 1


Constraints:

The number of nodes in the tree is in the range [1, 104].
-100 <= Node.val <= 100
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
        def distances(node1: List[int], node2: List[int]) -> int:
            ll1 = len(node1)
            ll2 = len(node2)
            for ii in range(min(ll1,ll2)):
                if node1[ii] != node2[ii]:
                    return (ll1-ii)+(ll2-ii)
                if ii == ll1-1:
                    return ll2-ii-1
                if ii == ll2-1:
                    return ll1-ii-1

            return 0

        if root == None:
            return 0

        index = 100
        q = [[root,[index]]]
        nodes = [[index]]
        index += 1
        while q:
            p,pl = q.pop(0)
            if p.left == None and p.right == None:
                nodes.append(pl)
            if p.left:
                q.append([p.left,pl+[index]])
                index += 1
            if p.right:
                q.append([p.right,pl+[index]])
                index += 1

        result = 0
        ll = len(nodes)
        #print(nodes)
        for ii in range(ll-1):
            for jj in range(ii+1,ll):
                result = max(result, distances(nodes[ii], nodes[jj]))

        return result


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
