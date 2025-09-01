"""
103. Binary Tree Zigzag Level Order Traversal
Solved
Medium
Topics
premium lock icon
Companies
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 2000].
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
    def leetcode(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        q = [[root,0]]
        ans = [[]]
        while len(q):
            cur,l = q.pop()
            if l >= len(ans):
                ans.append([])
            ans[l].append(cur.val)
            
            if cur.right:
                q.append([cur.right,l+1])
            if cur.left:
                q.append([cur.left,l+1])
                
        #print(ans)
        for ii in range(len(ans)):
            if ii%2 == 1:
                ans[ii] = ans[ii][::-1]
        #print(ans)
        
        return ans


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
