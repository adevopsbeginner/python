"""

Code


Testcase
Test Result
Test Result
412. Fizz Buzz
Solved
Easy
Topics
Companies
Given an integer n, return a string array answer (1-indexed) where:

answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i (as a string) if none of the above conditions are true.


Example 1:

Input: n = 3
Output: ["1","2","Fizz"]
Example 2:

Input: n = 5
Output: ["1","2","Fizz","4","Buzz"]
Example 3:

Input: n = 15
Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]


Constraints:

1 <= n <= 104
"""

import string
from typing import List
from collections import defaultdict

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def leetcode(self, n: int) -> List[str]:
        ln = [str(x) for x in range(n + 1)]
        for ii in range(1, n + 1):
            if ii % 15 == 0:
                ln[ii] = "FizzBuzz"
            elif ii % 3 == 0:
                ln[ii] = "Fizz"
            elif ii % 5 == 0:
                ln[ii] = "Buzz"
        ln.pop(0)
        return ln

if __name__ == "__main__":
    app = Solution()
    a = "hello"
    a = " "
    a = [4, 9, 5]
    b = [9, 4, 9, 8, 4]
    a = 16
    print(app.leetcode(a))
