"""
808. Soup Servings
Medium
Topics
premium lock icon
Companies
You have two soups, A and B, each starting with n mL. On every turn, one of the following four serving operations is chosen at random, each with probability 0.25 independent of all previous turns:

pour 100 mL from type A and 0 mL from type B
pour 75 mL from type A and 25 mL from type B
pour 50 mL from type A and 50 mL from type B
pour 25 mL from type A and 75 mL from type B
Note:

There is no operation that pours 0 mL from A and 100 mL from B.
The amounts from A and B are poured simultaneously during the turn.
If an operation asks you to pour more than you have left of a soup, pour all that remains of that soup.
The process stops immediately after any turn in which one of the soups is used up.

Return the probability that A is used up before B, plus half the probability that both soups are used up in the same turn. Answers within 10-5 of the actual answer will be accepted.

 

Example 1:

Input: n = 50
Output: 0.62500
Explanation: 
If we perform either of the first two serving operations, soup A will become empty first.
If we perform the third operation, A and B will become empty at the same time.
If we perform the fourth operation, B will become empty first.
So the total probability of A becoming empty first plus half the probability that A and B become empty at the same time, is 0.25 * (1 + 1 + 0.5 + 0) = 0.625.
Example 2:

Input: n = 100
Output: 0.71875
Explanation: 
If we perform the first serving operation, soup A will become empty first.
If we perform the second serving operations, A will become empty on performing operation [1, 2, 3], and both A and B become empty on performing operation 4.
If we perform the third operation, A will become empty on performing operation [1, 2], and both A and B become empty on performing operation 3.
If we perform the fourth operation, A will become empty on performing operation 1, and both A and B become empty on performing operation 2.
So the total probability of A becoming empty first plus half the probability that A and B become empty at the same time, is 0.71875.
 

Constraints:

0 <= n <= 109
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
    def leetcode(self, n: int) -> float:
        ### for large input n, the probability approaches 1 (<10-5)
        if n > 10000:
            return 0.99999

        @lru_cache(None)
        def probability(na, nb):
            if na <= 0 and nb <= 0:
                return 0.5
            elif na <= 0:
                return 1
            elif nb <= 0:
                return 0
            
            return 0.25*(probability(na-100,nb) + probability(na-75,nb-25) + probability(na-50,nb-50) + probability(na-25,nb-75))

        return probability(n, n)

        
        if n > 5000:  # For large n, probability approaches 1
            return 1.0
        
        #n = math.ceil(n / 25)
        
        @lru_cache(None)
        def dp(a, b):
            if a <= 0 and b <= 0:
                return 0.5
            if a <= 0:
                return 1.0
            if b <= 0:
                return 0.0
            
            return 0.25 * (
                dp(a - 100, b) +
                dp(a - 75, b - 25) +
                dp(a - 50, b - 50) +
                dp(a - 25, b - 75)
            )
        
        return dp(n, n)

        def probability(p, na, nb):
            if na <= 0 and nb <= 0:
                return p * 0.5  # both empty -> half credit to A
            if na <= 0:
                return p        # A empty first
            if nb <= 0:
                return 0        # B empty first -> no credit

            return (
                probability(p * 0.25, na - 100, nb) +
                probability(p * 0.25, na - 75,  nb - 25) +
                probability(p * 0.25, na - 50,  nb - 50) +
                probability(p * 0.25, na - 25,  nb - 75)
            )

        def probability1(p, na, nb, p_a_before_b, p_a_same_b, level, operation):
            #print(level, na, nb, p_a_before_b, p_a_same_b, operation)
            
            if na <= 0 or nb <= 0:
                if na <= 0 and nb <= 0:
                    p_a_same_b += p
                elif na <= 0:
                    p_a_before_b += p

                return p_a_before_b, p_a_same_b

            ### operation1
            if na <= 100 and nb > 0:
                p_a_before_b += p*0.25
            elif na <= 100 and nb == 0:
                p_a_same_b += p*0.25
            else:
                p_a_before_b, p_a_same_b = probability(p*0.25, na-100, nb, p_a_before_b, p_a_same_b, level+1, 1)

            #print(p_a_before_b, p_a_same_b, 1)

            ### operation2
            if na <= 75 and nb > 25:
                p_a_before_b += p*0.25
            elif na <= 75 and nb <= 25:
                p_a_same_b += p*0.25
            else:
                p_a_before_b, p_a_same_b = probability(p*0.25, na-75, nb-25, p_a_before_b, p_a_same_b, level+1, 2)

            #print(p_a_before_b, p_a_same_b, 2)

            ### operation3
            if na <= 50 and nb > 50:
                p_a_before_b += p*0.25
            elif na <= 50 and nb <= 50:
                p_a_same_b += p*0.25
            else:
                p_a_before_b, p_a_same_b = probability(p*0.25, na-50, nb-50, p_a_before_b, p_a_same_b, level+1, 3)

            #print(p_a_before_b, p_a_same_b, 3)

            ### operation4
            if na <= 25 and nb > 75:
                p_a_before_b += p*0.25
            elif na <= 25 and nb <= 75:
                p_a_same_b += p*0.25
            else:
                p_a_before_b, p_a_same_b = probability(p*0.25, na-25, nb-75, p_a_before_b, p_a_same_b, level+1, 4)
            
            #print(p_a_before_b, p_a_same_b, 4)

            return p_a_before_b, p_a_same_b


        na = n
        nb = n
        # na -= (n//250)*250
        # nb -= (n//250)*150

        level = 1
        #p_a_before_b, p_a_same_b = probability(1, na, nb, 0, 0, level, 0)
        return probability(1, na, nb)

        #print(p_a_before_b, p_a_same_b)

        return p_a_before_b + 0.5*p_a_same_b



if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
