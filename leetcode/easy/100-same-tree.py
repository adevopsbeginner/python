'''
100. Same Tree
Solved
Easy
Topics
Companies
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

 

Example 1:


Input: p = [1,2,3], q = [1,2,3]
Output: true
Example 2:


Input: p = [1,2], q = [1,null,2]
Output: false
Example 3:


Input: p = [1,2,1], q = [1,1,2]
Output: false
 

Constraints:

The number of nodes in both trees is in the range [0, 100].
-104 <= Node.val <= 104

'''

from typing import List

# Definition for singly-linked list.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def leetcode(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p == None and q == None:
            return True
        if p == None or q == None:
            return False
        pq = [p]
        qq = [q]
        while pq or qq:
            if pq == None:
                return False
            if qq == None:
                return False

            pi = pq.pop(0)
            qi = qq.pop(0)
            if qi.val != pi.val:
                return False
            if pi.left:
                pq.append(pi.left)
                if qi.left :
                    qq.append(qi.left)
                else:
                    return False
            else:
                if qi.left :
                    return False

            if pi.right:
                pq.append(pi.right)
                if qi.right:
                    qq.append(qi.right)
                else:
                    return False
            else:
                if qi.right:
                    return False


        return True

if __name__ == "__main__":
    app = Solution()
    a = [1,null,2,3]
    print(app.leetcode(a))
