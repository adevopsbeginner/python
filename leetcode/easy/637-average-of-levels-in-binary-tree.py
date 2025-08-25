"""
637. Average of Levels in Binary Tree
Solved
Easy
Topics
Companies
Given the root of a binary tree, return the average value of the nodes on each level in the form of an array. Answers within 10-5 of the actual answer will be accepted.


Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [3.00000,14.50000,11.00000]
Explanation: The average value of nodes on level 0 is 3, on level 1 is 14.5, and on level 2 is 11.
Hence return [3, 14.5, 11].
Example 2:


Input: root = [3,9,20,15,7]
Output: [3.00000,14.50000,11.00000]


Constraints:

The number of nodes in the tree is in the range [1, 104].
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
    def leetcode(self, root: Optional[TreeNode]) -> List[float]:
        dd = defaultdict(list)
        q = [[root, 0]]
        ll = 0
        while q:
            p, l = q.pop(0)
            ll = max(ll, l)
            dd[l].append(p.val)
            if p.left:
                q.append([p.left, l + 1])
            if p.right:
                q.append([p.right, l + 1])

        result = [sum(dd[ii]) / len(dd[ii]) for ii in range(ll + 1)]

        return result


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
