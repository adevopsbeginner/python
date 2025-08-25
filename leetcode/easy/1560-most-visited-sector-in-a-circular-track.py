"""
1560. Most Visited Sector in a Circular Track
Solved
Easy
Topics
Companies
Hint
Given an integer n and an integer array rounds. We have a circular track which consists of n sectors labeled from 1 to n. A marathon will be held on this track, the marathon consists of m rounds. The ith round starts at sector rounds[i - 1] and ends at sector rounds[i]. For example, round 1 starts at sector rounds[0] and ends at sector rounds[1]

Return an array of the most visited sectors sorted in ascending order.

Notice that you circulate the track in ascending order of sector numbers in the counter-clockwise direction (See the first example).

 

Example 1:


Input: n = 4, rounds = [1,3,1,2]
Output: [1,2]
Explanation: The marathon starts at sector 1. The order of the visited sectors is as follows:
1 --> 2 --> 3 (end of round 1) --> 4 --> 1 (end of round 2) --> 2 (end of round 3 and the marathon)
We can see that both sectors 1 and 2 are visited twice and they are the most visited sectors. Sectors 3 and 4 are visited only once.
Example 2:

Input: n = 2, rounds = [2,1,2,1,2,1,2,1,2]
Output: [2]
Example 3:

Input: n = 7, rounds = [1,3,5,7]
Output: [1,2,3,4,5,6,7]
 

Constraints:

2 <= n <= 100
1 <= m <= 100
rounds.length == m + 1
1 <= rounds[i] <= n
rounds[i] != rounds[i + 1] for 0 <= i < m
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
    def leetcode(self, n: int, rounds: List[int]) -> List[int]:
        m = len(rounds)
        visited = [0]*(n+1)
        for ii in range(1,m):
            ### start and end wont be the same in one round
            ### do not tag end point for now
            if rounds[ii] > rounds[ii-1]:
                for jj in range(rounds[ii-1], rounds[ii]):
                    visited[jj] += 1
            elif rounds[ii] < rounds[ii-1]:
                for jj in range(rounds[ii-1],n+1):
                    visited[jj] += 1
                for jj in range(1,rounds[ii]):
                    visited[jj] += 1

        ### until last round
        ### this also covers m==0
        visited[rounds[-1]] += 1

        #print(visited)
        max_visited = max(visited)
        result = []
        for ii in range(1,n+1):
            if visited[ii] == max_visited:
                result.append(ii)

        return result


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
