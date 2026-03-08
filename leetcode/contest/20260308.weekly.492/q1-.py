"""
Q1. Minimum Capacity Box
Solved
Easy
3 pt.
You are given an integer array capacity, where capacity[i] represents the capacity of the ith box, and an integer itemSize representing the size of an item.

The ith box can store the item if capacity[i] >= itemSize.

Return an integer denoting the index of the box with the minimum capacity that can store the item. If multiple such boxes exist, return the smallest index.

If no box can store the item, return -1.

 

Example 1:

Input: capacity = [1,5,3,7], itemSize = 3

Output: 2

Explanation:

The box at index 2 has a capacity of 3, which is the minimum capacity that can store the item. Thus, the answer is 2.

Example 2:

Input: capacity = [3,5,4,3], itemSize = 2

Output: 0

Explanation:

The minimum capacity that can store the item is 3, and it appears at indices 0 and 3. Thus, the answer is 0.

Example 3:

Input: capacity = [4], itemSize = 5

Output: -1

Explanation:

No box has enough capacity to store the item, so the answer is -1.

 

Constraints:

1 <= capacity.length <= 100
1 <= capacity[i] <= 100
1 <= itemSize <= 100
"""

from typing import List
from collections import defaultdict

class Solution:
    def leetcode(self, capacity: list[int], itemSize: int) -> int:
        result = -1
        ll = len(capacity)
        for ii in range(ll):
            if capacity[ii] == itemSize:
                return ii
            if capacity[ii] < itemSize:
                continue
            if result == -1:
                result = ii
            else:
                if capacity[ii] < capacity[result]:
                    result = ii
                    
        return result
