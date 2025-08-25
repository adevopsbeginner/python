'''
112. Path Sum
Solved
Easy
Topics
Companies
Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.

 

Example 1:


Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true
Explanation: The root-to-leaf path with the target sum is shown.
Example 2:


Input: root = [1,2,3], targetSum = 5
Output: false
Explanation: There two root-to-leaf paths in the tree:
(1 --> 2): The sum is 3.
(1 --> 3): The sum is 4.
There is no root-to-leaf path with sum = 5.
Example 3:

Input: root = [], targetSum = 0
Output: false
Explanation: Since the tree is empty, there are no root-to-leaf paths.
 

Constraints:

The number of nodes in the tree is in the range [0, 5000].
-1000 <= Node.val <= 1000
-1000 <= targetSum <= 1000

'''

from typing import List

# Definition for singly-linked list.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def leetcode(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return False

        q = [{"node":root,"pathsum":0}]
        while q:
            indexdict = q.pop(0)
            index = indexdict["node"]
            csum = indexdict["pathsum"]
            if index.left == None and index.right == None and index.val+csum == targetSum:
                return True
            if index.left:
                q.append({"node":index.left,"pathsum":csum+index.val})
            if index.right:
                q.append({"node":index.right,"pathsum":csum+index.val})

        return False

if __name__ == "__main__":
    app = Solution()
    a = [1,2,2,3,4,4,3]
    print(app.leetcode(a))
