"""
3495. Minimum Operations to Make Array Elements Zero
Hard
Topics
premium lock icon
Companies
Hint
You are given a 2D array queries, where queries[i] is of the form [l, r]. Each queries[i] defines an array of integers nums consisting of elements ranging from l to r, both inclusive.

In one operation, you can:

Select two integers a and b from the array.
Replace them with floor(a / 4) and floor(b / 4).
Your task is to determine the minimum number of operations required to reduce all elements of the array to zero for each query. Return the sum of the results for all queries.

 

Example 1:

Input: queries = [[1,2],[2,4]]

Output: 3

Explanation:

For queries[0]:

The initial array is nums = [1, 2].
In the first operation, select nums[0] and nums[1]. The array becomes [0, 0].
The minimum number of operations required is 1.
For queries[1]:

The initial array is nums = [2, 3, 4].
In the first operation, select nums[0] and nums[2]. The array becomes [0, 3, 1].
In the second operation, select nums[1] and nums[2]. The array becomes [0, 0, 0].
The minimum number of operations required is 2.
The output is 1 + 2 = 3.

Example 2:

Input: queries = [[2,6]]

Output: 4

Explanation:

For queries[0]:

The initial array is nums = [2, 3, 4, 5, 6].
In the first operation, select nums[0] and nums[3]. The array becomes [0, 3, 4, 1, 6].
In the second operation, select nums[2] and nums[4]. The array becomes [0, 3, 1, 1, 1].
In the third operation, select nums[1] and nums[2]. The array becomes [0, 0, 0, 1, 1].
In the fourth operation, select nums[3] and nums[4]. The array becomes [0, 0, 0, 0, 0].
The minimum number of operations required is 4.
The output is 4.

 

Constraints:

1 <= queries.length <= 105
queries[i].length == 2
queries[i] == [l, r]
1 <= l < r <= 109
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
    def leetcode(self, queries: List[List[int]]) -> int:
        ### 34...16
        ### 12...3
        ### sum = 28
        ### max = 3
        ### result = 28

        result = 0

        ### final loop and addup
        for l, r in queries:
            ### 1. turn integer to operations
            operations_l = 0
            for ii in range(1, 16):
                if l < (1<<ii*2):
                    operations_l = ii
                    break

            operations_r = 0
            for ii in range(1, 16):
                if r < (1<<ii*2):
                    operations_r = ii
                    break

            ### 2. sum
            if operations_l == operations_r:
                sum_operations = (r-l+1)*operations_l
            else:
                sum_operations = 0

                sum_operations += operations_l*((1<<(2*operations_l)) - l)
                #print(sum_operations)
                
                for ii in range(operations_l+1, operations_r):
                    sum_operations += ii*((1<<(2*ii)) - (1<<(2*(ii-1))))
                    #print(ii, sum_operations)

                sum_operations += operations_r*(r - (1<<(2*(operations_r-1))) + 1)
                #print(sum_operations)


            ### 3. max(sum, max)
            #print(l, r, operations_l, operations_r, sum_operations, (sum_operations+1)//2, (operations_r+1)//2)
            result += max((sum_operations+1)//2, (operations_r+1)//2)

        return result


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
