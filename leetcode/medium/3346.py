"""
3346. Maximum Frequency of an Element After Performing Operations I
Medium
Topics
premium lock icon
Companies
Hint
You are given an integer array nums and two integers k and numOperations.

You must perform an operation numOperations times on nums, where in each operation you:

Select an index i that was not selected in any previous operations.
Add an integer in the range [-k, k] to nums[i].
Return the maximum possible frequency of any element in nums after performing the operations.

 

Example 1:

Input: nums = [1,4,5], k = 1, numOperations = 2

Output: 2

Explanation:

We can achieve a maximum frequency of two by:

Adding 0 to nums[1]. nums becomes [1, 4, 5].
Adding -1 to nums[2]. nums becomes [1, 4, 4].
Example 2:

Input: nums = [5,11,20,20], k = 5, numOperations = 1

Output: 2

Explanation:

We can achieve a maximum frequency of two by:

Adding 0 to nums[1].
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 105
0 <= k <= 105
0 <= numOperations <= nums.length
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
    def leetcode(self, nums: List[int], k: int, numOperations: int) -> int:
        cnt = Counter(nums)
        nums.sort()
        ll = len(nums)
        l = 0
        r = 0
        result = 1
        count = 0
        num = nums[0]
        while num <= nums[-1]:
        #for ii in range(ll):
            print(l,r,num, result)
            while l < r and nums[l] < num-k:
                count -= 1
                l += 1
            while r < ll and nums[r] <= num+k:
                count += 1
                r += 1
                #print(r, count)

            result = max(result, min(count, cnt[num]+numOperations))
            num += 1

        return result


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
