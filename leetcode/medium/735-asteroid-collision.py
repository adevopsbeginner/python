"""
735. Asteroid Collision
Solved
Medium
Topics
Companies
Hint
We are given an array asteroids of integers representing asteroids in a row. The indices of the asteriod in the array represent their relative position in space.

For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

 

Example 1:

Input: asteroids = [5,10,-5]
Output: [5,10]
Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.
Example 2:

Input: asteroids = [8,-8]
Output: []
Explanation: The 8 and -8 collide exploding each other.
Example 3:

Input: asteroids = [10,2,-5]
Output: [10]
Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.
 

Constraints:

2 <= asteroids.length <= 104
-1000 <= asteroids[i] <= 1000
asteroids[i] != 0
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
    def leetcode(self, asteroids: List[int]) -> List[int]:
        ll = len(asteroids)
        q = []
        for each in asteroids:
            #print(each,q)
            while len(q) > 0:
                if q[-1] < 0 and each < 0:
                    q.append(each)
                    break
                elif q[-1] > 0 and each > 0:
                    q.append(each)
                    break
                elif q[-1] < 0 and each > 0:
                    q.append(each)
                    break
                elif abs(q[-1]) == abs(each):
                    q.pop()
                    each = 0
                    break
                elif abs(q[-1]) > abs(each):
                    break
                else:
                    q.pop()

            if len(q) == 0 and each != 0:
                q.append(each)

        return q


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
