'''
21. Merge Two Sorted Lists
Solved
Easy
Topics
Companies
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

 

Example 1:


Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]
 

Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def leetcode(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
#        while list1:
#            print(list1.val)
#            list1 = list1.next
#        while list2:
#            print(list2.val)
#            list2 = list2.next

        if list1 == None:
            return list2
        if list2 == None:
            return list1

        head = index = None

        while list1 and list2:
            if head:
                if list1.val < list2.val:
                    index.next = list1
                    list1 = list1.next
                else:
                    index.next = list2
                    list2 = list2.next
                index = index.next
                index.next = None
            else:
                if list1.val < list2.val:
                    head = list1
                    list1 = list1.next
                else:
                    head = list2
                    list2 = list2.next
                index = head

            if list1:
                index.next = list1
            if list2:
                index.next = list2

        return head

if __name__ == "__main__":
    app = Solution()
    test1 = [1,2,4]
    test2 = [1,3,4]
    print(app.leetcode(test1,test2))
