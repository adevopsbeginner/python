"""
1530. Number of Good Leaf Nodes Pairs
Medium
Topics
Companies
Hint
You are given the root of a binary tree and an integer distance. A pair of two different leaf nodes of a binary tree is said to be good if the length of the shortest path between them is less than or equal to distance.

Return the number of good leaf node pairs in the tree.



Example 1:


Input: root = [1,2,3,null,4], distance = 3
Output: 1
Explanation: The leaf nodes of the tree are 3 and 4 and the length of the shortest path between them is 3. This is the only good pair.
Example 2:


Input: root = [1,2,3,4,5,6,7], distance = 3
Output: 2
Explanation: The good pairs are [4,5] and [6,7] with shortest path = 2. The pair [4,6] is not good because the length of ther shortest path between them is 4.
Example 3:

Input: root = [7,1,4,6,null,5,3,null,null,null,null,null,2], distance = 3
Output: 1
Explanation: The only good pair is [2,5].


Constraints:

The number of nodes in the tree is in the range [1, 210].
1 <= Node.val <= 100
1 <= distance <= 10
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
    def leetcode(self, root: TreeNode, distance: int) -> int:
        def dfs(node):
            if not node:
                return []
            if not node.left and not node.right:
                return [1]  # This is a leaf node, return distance 1

            left_distances = dfs(node.left)
            right_distances = dfs(node.right)

            for l in left_distances:
                for r in right_distances:
                    if l + r <= distance:
                        self.result += 1

            # Increase all distances by 1 (because we are moving one level up)
            return [d + 1 for d in left_distances + right_distances]

        self.result = 0
        dfs(root)
        return self.result

        ## my code did not pass
        def distances(node1: List[int], node2: List[int]) -> int:
            ll1 = len(node1)
            ll2 = len(node2)
            for ii in range(min(ll1,ll2)):
                if node1[ii] != node2[ii]:
                    return (ll1-ii)+(ll2-ii)
                if ii == ll1-1:
                    return ll2-ii-1
                if ii == ll2-1:
                    return ll1-ii-1

            return 0
        if root == None:
            return 0
        nodes = []
        q = [[root,[root.val]]]
        while q:
            p,pl = q.pop(0)
            if p.left == None and p.right == None:
                nodes.append(pl)
            if p.left:
                q.append([p.left,pl+[p.left.val]])
            if p.right:
                q.append([p.right,pl+[p.right.val]])
        result = 0
        ll = len(nodes)
        for ii in range(ll-1):
            for jj in range(ii+1,ll):
                if distances(nodes[ii], nodes[jj]) <= distance:
                    #print(nodes[ii])
                    result += 1

        return result


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
