"""
826. Most Profit Assigning Work
Medium
Topics
Companies
You have n jobs and m workers. You are given three arrays: difficulty, profit, and worker where:

difficulty[i] and profit[i] are the difficulty and the profit of the ith job, and
worker[j] is the ability of jth worker (i.e., the jth worker can only complete a job with difficulty at most worker[j]).
Every worker can be assigned at most one job, but one job can be completed multiple times.

For example, if three workers attempt the same job that pays $1, then the total profit will be $3. If a worker cannot complete any job, their profit is $0.
Return the maximum profit we can achieve after assigning the workers to the jobs.



Example 1:

Input: difficulty = [2,4,6,8,10], profit = [10,20,30,40,50], worker = [4,5,6,7]
Output: 100
Explanation: Workers are assigned jobs of difficulty [4,4,6,6] and they get a profit of [20,20,30,30] separately.
Example 2:

Input: difficulty = [85,47,57], profit = [24,66,99], worker = [40,25,25]
Output: 0


Constraints:

n == difficulty.length
n == profit.length
m == worker.length
1 <= n, m <= 104
1 <= difficulty[i], profit[i], worker[i] <= 105
"""

import string
import heapq
import math
from typing import List
from collections import defaultdict


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def leetcode(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        n = len(difficulty)
        m = len(worker)
        nm = sorted(zip(profit,difficulty),reverse=True)
        # print(nm)
        # for each in nm:
        #     print(each)
        # dd = {each[0]:each[1] for each in sorted(zip(difficulty,profit),reverse=True)}
        dd = defaultdict(int)

        for each in nm:
            if each[0] in dd:
                dd[each[0]] = min(dd[each[0]], each[1])
            else:
                dd[each[0]] = each[1]
        # for each in dd:
        #     print(each,dd[each])
        result = 0
        for w in worker:
            for each in dd:
                if w >= dd[each]:
                    result += each
                    break

        return result

if __name__ == "__main__":
    app = Solution()
    difficulty = [2,4,6,8,10]
    profit = [10,20,30,40,50]
    worker = [4,5,6,7]
    difficulty =    [68, 35, 52, 47, 86]
    profit =    [67, 17, 1, 81, 3]
    worker =    [92, 10, 85, 84, 82]
    difficulty =    [17, 23, 25, 30, 30, 34, 55, 58, 72, 85]
    profit =    [4, 41, 57, 64, 65, 68, 73, 73, 87, 98]
    worker =    [99, 35, 21, 66, 22, 7, 12, 75, 8, 94]
    print(app.leetcode(difficulty,profit,worker))
