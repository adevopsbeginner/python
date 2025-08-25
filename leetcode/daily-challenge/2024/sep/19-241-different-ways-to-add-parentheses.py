"""
241. Different Ways to Add Parentheses
Medium
Topics
Companies
Given a string expression of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. You may return the answer in any order.

The test cases are generated such that the output values fit in a 32-bit integer and the number of different results does not exceed 104.



Example 1:

Input: expression = "2-1-1"
Output: [0,2]
Explanation:
((2-1)-1) = 0
(2-(1-1)) = 2
Example 2:

Input: expression = "2*3-4*5"
Output: [-34,-14,-10,-10,10]
Explanation:
(2*(3-(4*5))) = -34
((2*3)-(4*5)) = -14
((2*(3-4))*5) = -10
(2*((3-4)*5)) = -10
(((2*3)-4)*5) = 10


Constraints:

1 <= expression.length <= 20
expression consists of digits and the operator '+', '-', and '*'.
All the integer values in the input expression are in the range [0, 99].
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
    def leetcode(self, expression: str) -> List[int]:
        ### chatgpt
        # Memoization dictionary to store results for subexpressions
        memo = {}

        # Helper function to compute all possible results for a subexpression
        def compute(expr):
            # Check if the result is already in memo
            if expr in memo:
                return memo[expr]

            # List to store all the possible results for this expression
            results = []

            # Try to split the expression at each operator
            for i, char in enumerate(expr):
                if char in "+-*":  # If it's an operator, split the expression
                    # Recursively compute left and right parts
                    left_results = compute(expr[:i])
                    right_results = compute(expr[i+1:])

                    # Combine the results from the left and right parts using the current operator
                    for left in left_results:
                        for right in right_results:
                            if char == '+':
                                results.append(left + right)
                            elif char == '-':
                                results.append(left - right)
                            elif char == '*':
                                results.append(left * right)

            # Base case: if the expression is a single number, return it as an integer
            if not results:
                results.append(int(expr))

            # Store the result in memo before returning
            memo[expr] = results
            return results

        # Call the helper function for the full expression
        return compute(expression)
        num = 0
        nums = []
        signs = ["+"]
        for each in expression:
            if each in "0123456789":
                num = num*10+int(each)
            else:
                nums.append(num)
                signs.append(each)
                num = 0
        nums.append(num)
        ll = len(nums)
        print(nums, signs)
        cal = nums[0]
        for ii in range(1,ll):
            pass
        result = []

        return result


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
