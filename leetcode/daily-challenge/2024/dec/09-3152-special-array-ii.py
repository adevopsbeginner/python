"""
3152. Special Array II
Attempted
Medium
Topics
Companies
Hint
An array is considered special if every pair of its adjacent elements contains two numbers with different parity.

You are given an array of integer nums and a 2D integer matrix queries, where for queries[i] = [fromi, toi] your task is to check that 
subarray
 nums[fromi..toi] is special or not.

Return an array of booleans answer such that answer[i] is true if nums[fromi..toi] is special.

 

Example 1:

Input: nums = [3,4,1,2,6], queries = [[0,4]]

Output: [false]

Explanation:

The subarray is [3,4,1,2,6]. 2 and 6 are both even.

Example 2:

Input: nums = [4,3,1,6], queries = [[0,2],[2,3]]

Output: [false,true]

Explanation:

The subarray is [4,3,1]. 3 and 1 are both odd. So the answer to this query is false.
The subarray is [1,6]. There is only one pair: (1,6) and it contains numbers with different parity. So the answer to this query is true.
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 105
1 <= queries.length <= 105
queries[i].length == 2
0 <= queries[i][0] <= queries[i][1] <= nums.length - 1
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
    def leetcode(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        n = len(nums)

        # Special case: If nums has only one element, all subarrays are "special".
        if n == 1:
            return [True] * len(queries)

        # Step 1: Compute parity differences
        parity_diff = [nums[i] % 2 != nums[i + 1] % 2 for i in range(n - 1)]

        # Step 2: Build prefix sum for parity_diff
        prefix = [0] * (n - 1)
        prefix[0] = 0 if parity_diff[0] else 1
        for i in range(1, n - 1):
            prefix[i] = prefix[i - 1] + (0 if parity_diff[i] else 1)

        # Step 3: Process each query
        result = []
        for fromi, toi in queries:
            if toi == fromi:  # Single element is always special
                result.append(True)
            else:
                # Count same-parity pairs in the range [fromi, toi-1]
                same_parity_count = prefix[toi - 1] - (prefix[fromi - 1] if fromi > 0 else 0)
                result.append(same_parity_count == 0)

        return result

        ll = len(nums)
        parity = 1
        for ii in range(1,ll):
            parity, nums[ii-1] = (nums[ii]%2)^(nums[ii-1]%2), parity
        nums[-1] = parity
        #print(nums)
 
        llq = len(queries)
        result = [True for ii in range(llq)]
        if sum(nums) == ll:
            return result
        zero = []
        for ii in range(ll):
            if nums[ii] == 0:
                zero.append(ii)
        #print(zero)
        #queries.sort()
        for ii in range(llq):
            for each in zero:
                if queries[ii][1] < each:
                    break
                if queries[ii][0] < each and queries[ii][1] >= each:
                    result[ii] = False

        return result
        
        ### time limit exceeded
        ll = len(nums)
        parity = 1
        for ii in range(1,ll):
            parity, nums[ii-1] = (nums[ii]%2)^(nums[ii-1]%2), parity
        nums[-1] = parity
        #print(nums)
 
        llq = len(queries)
        result = [sum(nums[queries[ii][0]+1:queries[ii][1]+1]) == queries[ii][1]-queries[ii][0]  for ii in range(llq)]

        return result


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
