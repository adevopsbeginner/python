'''
101. Symmetric Tree
Solved
Easy
Topics
Companies
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

 

Example 1:


Input: root = [1,2,2,3,4,4,3]
Output: true
Example 2:


Input: root = [1,2,2,null,3,null,3]
Output: false
 

Constraints:

The number of nodes in the tree is in the range [1, 1000].
-100 <= Node.val <= 100
 

Follow up: Could you solve it both recursively and iteratively?

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
            return True

        leftq  = [root]
        rightq = [root]

        while leftq or rightq:
            if leftq == None and rightq == None:
                return True
            elif leftq and rightq:
                leftnode = leftq.pop(0)
                rightnode = rightq.pop(0)

                if leftnode == None and rightnode == None:
                    continue
                elif leftnode and rightnode:
                    pass
                else:
                    #print(2222)
                    return False

                if leftnode.val != rightnode.val:
                    #print(3333)
                    return False
                
                leftq.append(leftnode.left)
                leftq.append(leftnode.right)
                rightq.append(rightnode.right)
                rightq.append(rightnode.left)
            else:
                return False
            
        return True

if __name__ == "__main__":
    app = Solution()
    a = [1,2,2,3,4,4,3]
    print(app.leetcode(a))
