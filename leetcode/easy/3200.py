"""
3200. Maximum Height of a Triangle
Solved
Easy
Topics
￼
Companies
Hint
You are given two integers red and blue representing the count of red and blue colored balls. You have to arrange these balls to form a triangle such that the 1st row will have 1 ball, the 2nd row will have 2 balls, the 3rd row will have 3 balls, and so on.

All the balls in a particular row should be the same color, and adjacent rows should have different colors.

Return the maximum height of the triangle that can be achieved.

 

Example 1:

Input: red = 2, blue = 4

Output: 3

Explanation:

￼

The only possible arrangement is shown above.

Example 2:

Input: red = 2, blue = 1

Output: 2

Explanation:

￼
The only possible arrangement is shown above.

Example 3:

Input: red = 1, blue = 1

Output: 1

Example 4:

Input: red = 10, blue = 1

Output: 2

Explanation:

￼
The only possible arrangement is shown above.

 

Constraints:

1 <= red, blue <= 100
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
    def leetcode(self, red: int, blue: int) -> int:
        def color(first: int, second: int) -> int:
            index = 1
            while first or second:
                #print(index,first,second)
                if index % 2:
                    if first < index:
                        break
                    first -= index
                else:
                    if second < index:
                        break
                    second -= index
                index += 1
            #print(index-1)
            return index-1

        max1 = color(red,blue)
        max2 = color(blue,red)

        return max(max1,max2)


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
