"""
117. Populating Next Right Pointers in Each Node II
Solved
Medium
Topics
premium lock icon
Companies
Given a binary tree

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

 

Example 1:


Input: root = [1,2,3,4,5,null,7]
Output: [1,#,2,3,#,4,5,7,#]
Explanation: Given the above binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.
Example 2:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 6000].
-100 <= Node.val <= 100
 

Follow-up:

You may only use constant extra space.
The recursive approach is fine. You may assume implicit stack space does not count as extra space for this problem.
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
    def leetcode(self, root: 'Node') -> 'Node':
        if root == None:
            return None
        q = [[root,0]]
        while len(q):
            c,l = q.pop(0)
            #print('c.val=',c.val)
            c.next = None

            #print(2222,c.val,l,len(q))
            if len(q):
                #print(q[0][1])
                if l == q[0][1]:
                    c.next = q[0][0]

            if c.left:
                #print('in queue, c.left.val=', c.left.val)
                q.append([c.left,l+1])
            if c.right:
                #print('in queue, c.right.val=', c.right.val)
                q.append([c.right,l+1])
        return root


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
