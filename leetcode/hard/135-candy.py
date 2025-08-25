"""
135. Candy
Solved
Hard
Topics
Companies
There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
Return the minimum number of candies you need to have to distribute the candies to the children.

 

Example 1:

Input: ratings = [1,0,2]
Output: 5
Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.
Example 2:

Input: ratings = [1,2,2]
Output: 4
Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
The third child gets 1 candy because it satisfies the above two conditions.
 

Constraints:

n == ratings.length
1 <= n <= 2 * 104
0 <= ratings[i] <= 2 * 104
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
    def leetcode(self, ratings: List[int]) -> int:
        ll = len(ratings)
        result = ll
        current_candy = 1
        highest = -1
        highest_candy = 1
        for ii in range(1,ll):
            #print(ii, result, highest, highest_candy, current_candy)
            if ratings[ii] == ratings[ii-1]:
                if highest >= 0 and highest_candy <= ii-1-highest:
                    result += (ii-highest)-highest_candy
                highest = -1
                current_candy = 1
                #print(444,highest, result)
            elif ratings[ii] > ratings[ii-1]:
                #print(111,result)
                if highest >= 0 and highest_candy <= ii-1-highest:
                    result += (ii-highest)-highest_candy
                highest = -1
                #print(222,result)
                result += current_candy
                current_candy += 1
                #print(333,result)
            else:
                #print(highest,highest_candy)
                if highest == -1:
                    highest_candy = current_candy
                    highest = ii-1
                    #result += 1
                else:
                    result += ii-highest-1
                current_candy = 1
            
        #print(result, highest, highest_candy)

        if highest >= 0 and highest_candy <= ii-highest:
            result += (ii-highest)+1-highest_candy

        return result


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
