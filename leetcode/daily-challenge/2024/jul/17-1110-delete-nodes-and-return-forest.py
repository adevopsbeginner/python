"""

Code
Testcase
Test Result
Test Result
1110. Delete Nodes And Return Forest
Medium
Topics
Companies
Given the root of a binary tree, each node in the tree has a distinct value.

After deleting all nodes with a value in to_delete, we are left with a forest (a disjoint union of trees).

Return the roots of the trees in the remaining forest. You may return the result in any order.



Example 1:


Input: root = [1,2,3,4,5,6,7], to_delete = [3,5]
Output: [[1,2,null,4],[6],[7]]
Example 2:

Input: root = [1,2,4,null,3], to_delete = [3]
Output: [[1,2,4]]


Constraints:

The number of nodes in the given tree is at most 1000.
Each node has a distinct value between 1 and 1000.
to_delete.length <= 1000
to_delete contains distinct values between 1 and 1000.
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
    def leetcode(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        result = []
        q = [[root, None, ""]]
        while q:
            # test1 = [[x[0].val,x[2]] for x in q]
            # test2 = [x.val for x in result]
            # print(test1,test2)
            p,parent,lr = q.pop()
            if p.val in to_delete:
                if p.left:
                    q.append([p.left,None,""])
                if p.right:
                    q.append([p.right,None, ""])
                p.left = None
                p.right = None
                if parent:
                    if lr == "L":
                        parent.left = None
                    if lr == "R":
                        parent.right = None
            else:
                if parent == None:
                    # print(p.val,result)
                    result.append(p)

                if p.left:
                    q.append([p.left,p,"L"])
                if p.right:
                    q.append([p.right,p,"R"])

        return result


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
