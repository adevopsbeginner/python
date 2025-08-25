"""
2096. Step-By-Step Directions From a Binary Tree Node to Another
Medium
Topics
Companies
Hint
You are given the root of a binary tree with n nodes. Each node is uniquely assigned a value from 1 to n. You are also given an integer startValue representing the value of the start node s, and a different integer destValue representing the value of the destination node t.

Find the shortest path starting from node s and ending at node t. Generate step-by-step directions of such path as a string consisting of only the uppercase letters 'L', 'R', and 'U'. Each letter indicates a specific direction:

'L' means to go from a node to its left child node.
'R' means to go from a node to its right child node.
'U' means to go from a node to its parent node.
Return the step-by-step directions of the shortest path from node s to node t.



Example 1:


Input: root = [5,1,2,3,null,6,4], startValue = 3, destValue = 6
Output: "UURL"
Explanation: The shortest path is: 3 → 1 → 5 → 2 → 6.
Example 2:


Input: root = [2,1], startValue = 2, destValue = 1
Output: "L"
Explanation: The shortest path is: 2 → 1.


Constraints:

The number of nodes in the tree is n.
2 <= n <= 105
1 <= Node.val <= n
All the values in the tree are unique.
1 <= startValue, destValue <= n
startValue != destValue
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
    def leetcode(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        q = [[root,""]]
        startpath = ""
        destpath = ""
        while q:
            p,path = q.pop()
            if p.val == startValue:
                startpath = path
                # print(path)
            if p.val == destValue:
                destpath = path
                # print(path)

            if p.left:
                q.append([p.left,path+"L"])
            if p.right:
                q.append([p.right,path+"R"])
        lls = len(startpath)
        lld = len(destpath)
        ll = min(lls,lld)
        #print(startpath,destpath)
        for ii in range(ll):
            if startpath[ii] != destpath[ii]:
                #print(lls,ii,lls-ii,lld,"U"*(lls-ii))
                #print(destpath[ii:])
                return "U"*(lls-ii) + destpath[ii:]

        if lls < lld:
            return destpath[lls:]
        if lld < lls:
            return "U"*(lls-lld)

        return ""


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
