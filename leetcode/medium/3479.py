"""
3479. Fruits Into Baskets III
Solved
Medium
Topics
premium lock icon
Companies
Hint
You are given two arrays of integers, fruits and baskets, each of length n, where fruits[i] represents the quantity of the ith type of fruit, and baskets[j] represents the capacity of the jth basket.

From left to right, place the fruits according to these rules:

Each fruit type must be placed in the leftmost available basket with a capacity greater than or equal to the quantity of that fruit type.
Each basket can hold only one type of fruit.
If a fruit type cannot be placed in any basket, it remains unplaced.
Return the number of fruit types that remain unplaced after all possible allocations are made.

 

Example 1:

Input: fruits = [4,2,5], baskets = [3,5,4]

Output: 1

Explanation:

fruits[0] = 4 is placed in baskets[1] = 5.
fruits[1] = 2 is placed in baskets[0] = 3.
fruits[2] = 5 cannot be placed in baskets[2] = 4.
Since one fruit type remains unplaced, we return 1.

Example 2:

Input: fruits = [3,6,1], baskets = [6,4,7]

Output: 0

Explanation:

fruits[0] = 3 is placed in baskets[0] = 6.
fruits[1] = 6 cannot be placed in baskets[1] = 4 (insufficient capacity) but can be placed in the next available basket, baskets[2] = 7.
fruits[2] = 1 is placed in baskets[1] = 4.
Since all fruits are successfully placed, we return 0.

 

Constraints:

n == fruits.length == baskets.length
1 <= n <= 105
1 <= fruits[i], baskets[i] <= 109
"""

import string
import heapq
from typing import List
from collections import defaultdict

class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.tree = [0] * (4 * self.n)
        self.build(data, 0, 0, self.n - 1)

    def build(self, data, node, l, r):
        if l == r:
            self.tree[node] = (data[l], l)  # store (value, index)
        else:
            mid = (l + r) // 2
            self.build(data, 2*node+1, l, mid)
            self.build(data, 2*node+2, mid+1, r)
            self.tree[node] = max(self.tree[2*node+1], self.tree[2*node+2])

    def update(self, index, node, l, r):
        if l == r:
            self.tree[node] = (-1, l)
        else:
            mid = (l + r) // 2
            if index <= mid:
                self.update(index, 2*node+1, l, mid)
            else:
                self.update(index, 2*node+2, mid+1, r)
            self.tree[node] = max(self.tree[2*node+1], self.tree[2*node+2])

    def query(self, fruit, node, l, r):
        if self.tree[node][0] < fruit:
            return -1
        if l == r:
            return l
        mid = (l + r) // 2
        if self.tree[2*node+1][0] >= fruit:
            return self.query(fruit, 2*node+1, l, mid)
        else:
            return self.query(fruit, 2*node+2, mid+1, r)

class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        seg = SegmentTree(baskets)
        unplaced = 0

        for fruit in fruits:
            idx = seg.query(fruit, 0, 0, len(baskets) - 1)
            if idx == -1:
                unplaced += 1
            else:
                seg.update(idx, 0, 0, len(baskets) - 1)

        return unplaced

        ### wrong answers
# class Solution:
#     def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(baskets)
        used = [False] * n
        unplaced = 0
        start = 0  # Optimization: start from last checked basket

        for fruit in fruits:
            placed = False
            for i in range(n):
                if not used[i] and baskets[i] >= fruit:
                    used[i] = True
                    placed = True
                    break
            if not placed:
                unplaced += 1

        return unplaced
        
        result = 0
        used = [False] * len(baskets)  # Track used baskets

        for fruit in fruits:
            placed = False
            for i in range(len(baskets)):
                if not used[i] and baskets[i] >= fruit:
                    used[i] = True
                    placed = True
                    break
            if not placed:
                result += 1

        return result
        
        available = SortedList((cap, i) for i, cap in enumerate(baskets))
        print(available)
        placed_indices = set()
        unplaced = 0

        for fruit in fruits:
            # Binary search to find the first basket with capacity >= fruit
            idx = available.bisect_left((fruit, -1))
            print(fruit, idx, available)
            while idx < len(available):
                cap, i = available[idx]
                if i not in placed_indices:
                    placed_indices.add(i)
                    available.pop(idx)
                    break
                else:
                    idx += 1
            else:
                unplaced += 1

        return unplaced
        
        result = 0
        n = len(baskets)

        for fruit in fruits:
            placed = False
            for i in range(n):
                if baskets[i] >= fruit:
                    baskets[i] = -1  # Mark this basket as used
                    placed = True
                    break
            if not placed:
                result += 1

        return result
        
        result = 0
        ll = len(baskets)
        for fruit in fruits:
            if max(baskets) < fruit:
                result += 1
                continue
                
            for ii in range(ll):
                if baskets[ii] >= fruit:
                    baskets[ii] = 0
                    break

        return result


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
