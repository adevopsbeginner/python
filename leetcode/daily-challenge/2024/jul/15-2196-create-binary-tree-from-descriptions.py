"""
2196. Create Binary Tree From Descriptions
Medium
Topics
Companies
Hint
You are given a 2D integer array descriptions where descriptions[i] = [parenti, childi, isLefti] indicates that parenti is the parent of childi in a binary tree of unique values. Furthermore,

If isLefti == 1, then childi is the left child of parenti.
If isLefti == 0, then childi is the right child of parenti.
Construct the binary tree described by descriptions and return its root.

The test cases will be generated such that the binary tree is valid.



Example 1:


Input: descriptions = [[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]]
Output: [50,20,80,15,17,19]
Explanation: The root node is the node with value 50 since it has no parent.
The resulting binary tree is shown in the diagram.
Example 2:


Input: descriptions = [[1,2,1],[2,3,0],[3,4,1]]
Output: [1,2,null,null,3,4]
Explanation: The root node is the node with value 1 since it has no parent.
The resulting binary tree is shown in the diagram.


Constraints:

1 <= descriptions.length <= 104
descriptions[i].length == 3
1 <= parenti, childi <= 105
0 <= isLefti <= 1
The binary tree described by descriptions is valid.
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
    def leetcode(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        ll = len(descriptions)
        dd = defaultdict(TreeNode)
        dp = defaultdict(int)
        for ii in range(ll):
            dp[descriptions[ii][0]] = 0

        for each in descriptions:
            # print(each,each[0])
            if each[0] not in dd:
                p = TreeNode(each[0])
                # print("p", p.val)
                dd[each[0]] = p
            if each[1] not in dd:
                c = TreeNode(each[1])
                # print("c", c.val)
                dd[each[1]] = c
            if each[2]:
                dd[each[0]].left = dd[each[1]]
            else:
                dd[each[0]].right = dd[each[1]]

            dp[each[1]] = 1

        # for each in dd:
        #     print(each,dd[each])

        # for each in dp:
        #     print(each,dp[each])

        for each in dp:
            if dp[each] == 0:
                # print(each, dd[each])
                return dd[each]

        return None


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
