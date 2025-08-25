'''
119. Pascal's Triangle II
Solved
Easy
Topics
Companies
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


 

Example 1:

Input: rowIndex = 3
Output: [1,3,3,1]
Example 2:

Input: rowIndex = 0
Output: [1]
Example 3:

Input: rowIndex = 1
Output: [1,1]
 

Constraints:

0 <= rowIndex <= 33
 

Follow up: Could you optimize your algorithm to use only O(rowIndex) extra space?

'''

from typing import List

# Definition for singly-linked list.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def leetcode(self, rowIndex: int) -> List[int]:
        pascal = [[1]]
        for ii in range(rowIndex):
            arr = [0]+pascal[-1]+[0]
            new = [arr[i] + arr[i+1] for i in range(len(arr)-1)]
            pascal.append(new)
        return pascal[-1]

if __name__ == "__main__":
    app = Solution()
    a = [1,2,2,3,4,4,3]
    print(app.leetcode(a))
