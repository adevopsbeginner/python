"""
515. Find Largest Value in Each Tree Row
Medium
Topics
Companies
Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).

 

Example 1:


Input: root = [1,3,2,5,3,null,9]
Output: [1,3,9]
Example 2:

Input: root = [1,2,3]
Output: [1,3]
 

Constraints:

The number of nodes in the tree will be in the range [0, 104].
-231 <= Node.val <= 231 - 1
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
    def leetcode(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []

        q = [[root,0]]
        level = -1
        row = []
        result = []
        while q:
            p,l = q.pop(0)
            if l > level:
                #print(row, l, level)
                if len(row):
                    result.append(max(row))
                row = [p.val]
                level = l
            else:
                row.append(p.val)

            if p.left:
                q.append([p.left, l+1])
            if p.right:
                q.append([p.right, l+1])
            
        result.append(max(row))
        
        return result


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
