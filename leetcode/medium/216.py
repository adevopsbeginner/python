"""
216. Combination Sum III
Solved
Medium
Topics
￼
Companies
Find all valid combinations of k numbers that sum up to n such that the following conditions are true:

Only numbers 1 through 9 are used.
Each number is used at most once.
Return a list of all possible valid combinations. The list must not contain the same combination twice, and the combinations may be returned in any order.

 

Example 1:

Input: k = 3, n = 7
Output: [[1,2,4]]
Explanation:
1 + 2 + 4 = 7
There are no other valid combinations.
Example 2:

Input: k = 3, n = 9
Output: [[1,2,6],[1,3,5],[2,3,4]]
Explanation:
1 + 2 + 6 = 9
1 + 3 + 5 = 9
2 + 3 + 4 = 9
There are no other valid combinations.
Example 3:

Input: k = 4, n = 1
Output: []
Explanation: There are no valid combinations.
Using 4 different numbers in the range [1,9], the smallest sum we can get is 1+2+3+4 = 10 and since 10 > 1, there are no valid combination.
 

Constraints:

2 <= k <= 9
1 <= n <= 60
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
    def leetcode(self, k: int, n: int) -> List[List[int]]:
        ans = []
        q = [[{0},0]]
        
        while len(q):
            #print(q)
            combn,level = q.pop(0)
            if level > k:
                continue

            sumc = sum(combn)
            #print(combn, sumc)
            if sumc == n and level == k:
                if combn not in ans:
                    listcomb = list(combn)
                    listcomb.remove(0)
                    ans.append(listcomb)
                continue
            
            for ii in range(max(combn)+1,10):
                if ii in combn:
                    continue
                if sumc+ii <= n:
                    q.append([combn.union({ii}),level+1])
        
        return ans


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
