"""
42. Trapping Rain Water
Solved
Hard
Topics
Companies
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

 

Example 1:


Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9
 

Constraints:

n == height.length
1 <= n <= 2 * 104
0 <= height[i] <= 105
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
    def leetcode(self, height: List[int]) -> int:
        ll = len(height)
        if ll < 2:
            return 0
        walls = sum(height)
        highest = max(height)
        #height.sort()
        front = 0
        end = ll-1
        result = 0
        current_height = 0
        while front < end:
            if front + 1 == end:
                if height[front] > current_height:
                    result += height[front] - current_height
                if height[end] > current_height:
                    result += height[end] - current_height
                print("finish", front, end)
                break
            if height[front] <= current_height:
                #print("front==0", front)
                front += 1
                continue
            if height[end] <= current_height:
                #print("end==0", end)
                end -= 1
                continue
            
            #print(result, front, end)

            if height[front] < height[end]:
                result += (end-front+1) * (height[front]-current_height)
                current_height = height[front]
                front += 1
            elif height[front] == height[end]:
                result += (end-front+1) * (height[front]-current_height)
                current_height = height[front]
                front += 1
                end -= 1
            else:
                result += (end-front+1) * (height[end]-current_height)
                current_height = height[end]
                end -= 1

            if front == end:
                if height[front] > current_height:
                    result += height[front] - current_height

        #print(result, walls)
        result -= walls

        return result


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
