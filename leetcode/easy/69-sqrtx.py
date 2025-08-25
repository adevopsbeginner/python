'''

Code
Testcase
Test Result
Test Result
69. Sqrt(x)
Solved
Easy
Topics
Companies
Hint
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
 

Example 1:

Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.
Example 2:

Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.
 

Constraints:

0 <= x <= 231 - 1
'''

from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def leetcode(self, x: int) -> int:
        power2 = 1
        ii = 1
        while power2 < x: ## 2079ms
            print(ii)
            i10 = ii*10
            power2 = i10 ** 2
            if power2 == x:
                return i10
            elif power2 > x:
                ii += 1
                power2 = ii ** 2
            else:
                ii = i10
        if power2 == x:
            return ii
        else:
            return ii-1
        
        for ii in range(100000): ## 1100ms
            if ii ** 2 >= x:
                if ii ** 2 == x:
                    return ii
                return ii-1
        return 1

if __name__ == "__main__":
    app = Solution()
    a = [1,3,5,6]
    a = 1010
    b = "1011"
    print(app.leetcode(a))
