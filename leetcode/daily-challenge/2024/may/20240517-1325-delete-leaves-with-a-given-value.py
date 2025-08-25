'''
1325. Delete Leaves With a Given Value
Solved
Medium
Topics
Companies
Hint
Given a binary tree root and an integer target, delete all the leaf nodes with value target.

Note that once you delete a leaf node with value target, if its parent node becomes a leaf node and has the value target, it should also be deleted (you need to continue doing that until you cannot).

 

Example 1:



Input: root = [1,2,3,2,null,2,4], target = 2
Output: [1,null,3,null,4]
Explanation: Leaf nodes in green with value (target = 2) are removed (Picture in left). 
After removing, new nodes become leaf nodes with value (target = 2) (Picture in center).
Example 2:



Input: root = [1,3,3,3,2], target = 3
Output: [1,3,null,null,2]
Example 3:



Input: root = [1,2,null,2,null,2], target = 2
Output: [1]
Explanation: Leaf nodes in green with value (target = 2) are removed at each step.
 

Constraints:

The number of nodes in the tree is in the range [1, 3000].
1 <= Node.val, target <= 1000
'''

import string
from typing import List
from collections import defaultdict

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def leetcode(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        q = [[None, 'L', root, True]]
        while q:
            p,flag,c,new = q.pop()
            if c.left == None and c.right == None:
                if c.val == target:
                    if p == None:
                        return None
                    if flag == 'L':
                        p.left = None
                    if flag == 'R':
                        p.right = None
            if c.val == target and new:
                q.append([p, flag, c, False])
            if c.left:
                q.append([c, 'L', c.left, True])
            if c.right:
                q.append([c, 'R', c.right, True])

        return root

if __name__ == "__main__":
    app = Solution()
    a = 2
    print(app.leetcode(a))
