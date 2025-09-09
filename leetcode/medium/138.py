"""
138. Copy List with Random Pointer
Medium
Topics
premium lock icon
Companies
Hint
A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.

Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.

For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.

Return the head of the copied linked list.

The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.
Your code will only be given the head of the original linked list.

 

Example 1:


Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
Example 2:


Input: head = [[1,1],[2,1]]
Output: [[1,1],[2,1]]
Example 3:



Input: head = [[3,null],[3,0],[3,null]]
Output: [[3,null],[3,0],[3,null]]
 

Constraints:

0 <= n <= 1000
-104 <= Node.val <= 104
Node.random is null or is pointing to some node in the linked list.
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
    def leetcode(self, head: 'Optional[Node]') -> 'Optional[Node]':
        result = None
        index_o = head
        index_n = result
        #count = 0

        ### 1. new copied list
        while index_o:
            ### 2. new_node-> random pointing to original node(2)
            new_node = Node(index_o.val, None, index_o)

            if result == None:
                result = new_node
                index_n = new_node
            else:
                index_n.next = new_node
                index_n = index_n.next

            ### 3. original node -> next pointing to new node
            index_o.next, index_o = new_node, index_o.next

            #count += 1
            #print(count, index_o.val)

        index_n = result
        while index_n:
            original_node = index_n.random
            if original_node.random == None:
                index_n.random = None
            else:
                index_n.random = original_node.random.next
            
            index_n = index_n.next

        return result


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
