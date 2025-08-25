'''
70. Climbing Stairs
Solved
Easy
Topics
Companies
Hint
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
 

Constraints:

1 <= n <= 45
'''

from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def climbStairs(self, n: int) -> int:
        nn = [1,2]
        for ii in range(3,n+1):
            #print(nn)
            nn.append(nn[ii-3]+nn[ii-2])
        return nn[n-1]

        if n == 1:
            return 1
        if n == 2:
            return 2
        if n == 3:
            return 3
        return self.climbStairs(n-1)+self.climbStairs(n-2)

if __name__ == "__main__":
    app = Solution()
    a = [1,3,5,6]
    a = 44
    b = "1011"
    print(app.climbStairs(a))
