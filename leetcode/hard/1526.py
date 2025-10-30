"""
1526. Minimum Number of Increments on Subarrays to Form a Target Array
Solved
Hard
Topics
premium lock icon
Companies
Hint
You are given an integer array target. You have an integer array initial of the same size as target with all elements initially zeros.

In one operation you can choose any subarray from initial and increment each value by one.

Return the minimum number of operations to form a target array from initial.

The test cases are generated so that the answer fits in a 32-bit integer.

 

Example 1:

Input: target = [1,2,3,2,1]
Output: 3
Explanation: We need at least 3 operations to form the target array from the initial array.
[0,0,0,0,0] increment 1 from index 0 to 4 (inclusive).
[1,1,1,1,1] increment 1 from index 1 to 3 (inclusive).
[1,2,2,2,1] increment 1 at index 2.
[1,2,3,2,1] target array is formed.
Example 2:

Input: target = [3,1,1,2]
Output: 4
Explanation: [0,0,0,0] -> [1,1,1,1] -> [1,1,1,2] -> [2,1,1,2] -> [3,1,1,2]
Example 3:

Input: target = [3,1,5,4,2]
Output: 7
Explanation: [0,0,0,0,0] -> [1,1,1,1,1] -> [2,1,1,1,1] -> [3,1,1,1,1] -> [3,1,2,2,2] -> [3,1,3,3,2] -> [3,1,4,4,2] -> [3,1,5,4,2].
 

Constraints:

1 <= target.length <= 105
1 <= target[i] <= 105
"""

import string
import heapq
from typing import List
from collections import defaultdict

class Solution:
    def leetcode(self, target: List[int]) -> int:
        target.insert(0,0)
        target.append(0)
        target.append(0)
        ll = len(target)
        result = 0
        low = high = 0
        goingup = 1
        for ii in range(1, ll-1):
            if goingup == 1 and target[ii] < target[ii-1]:
                high = ii-1
                goingup = 0
                result += target[high] - target[low]
            elif goingup == 0 and target[ii] > target[ii-1]:
                low = ii-1
                goingup = 1

        return result