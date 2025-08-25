"""
437. Path Sum III
Solved
Medium
Topics
premium lock icon
Companies
Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values along the path equals targetSum.

The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).

 

Example 1:


Input: root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
Output: 3
Explanation: The paths that sum to 8 are shown.
Example 2:

Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: 3
 

Constraints:

The number of nodes in the tree is in the range [0, 1000].
-109 <= Node.val <= 109
-1000 <= targetSum <= 1000
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
    def leetcode(self, root: Optional[TreeNode], targetSum: int) -> int:
        if root == None:
            return 0
        
        q = [[root,[0]]]
        ans = 0
        while len(q):
            n,p = q.pop(0)
            
            add = n.val
            llp = len(p)
            #print(p,n.val)
            for ii in range(llp-1,-1,-1):
                if add == targetSum:
                    #print(p,n.val)
                    ans += 1
                add += p[ii]
            
            np = p+[n.val]
            if n.left:
                q.append([n.left,np])
            if n.right:
                q.append([n.right,np])
                
        return ans


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
