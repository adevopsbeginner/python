"""
605. Can Place Flowers
Solved
Easy
Topics
Companies
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.



Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false


Constraints:

1 <= flowerbed.length <= 2 * 104
flowerbed[i] is 0 or 1.
There are no two adjacent flowers in flowerbed.
0 <= n <= flowerbed.length
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
    def leetcode(self, flowerbed: List[int], n: int) -> bool:
        ### for 0000 with 1...1
        if sum(flowerbed) == 0:
            return (len(flowerbed)+1)//2 >= n

        result = 0
        count0 = 0
        extra = 1 ### for first 1, 00001, which has no leftside 1
        for each in flowerbed:
            if each == 0:
                count0 += 1
            else:
                result += (count0-1+extra)//2
                extra = 0
                count0 = 0
                #print(each, count0, result)
        result += count0//2
        #print(result)

        return result >= n


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
