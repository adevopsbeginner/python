"""
3038. Maximum Number of Operations With the Same Score I
Easy
Topics
premium lock icon
Companies
You are given an array of integers nums. Consider the following operation:

Delete the first two elements nums and define the score of the operation as the sum of these two elements.
You can perform this operation until nums contains fewer than two elements. Additionally, the same score must be achieved in all operations.

Return the maximum number of operations you can perform.

 

Example 1:

Input: nums = [3,2,1,4,5]

Output: 2

Explanation:

We can perform the first operation with the score 3 + 2 = 5. After this operation, nums = [1,4,5].
We can perform the second operation as its score is 4 + 1 = 5, the same as the previous operation. After this operation, nums = [5].
As there are fewer than two elements, we can't perform more operations.
Example 2:

Input: nums = [1,5,3,3,4,1,3,2,2,3]

Output: 2

Explanation:

We can perform the first operation with the score 1 + 5 = 6. After this operation, nums = [3,3,4,1,3,2,2,3].
We can perform the second operation as its score is 3 + 3 = 6, the same as the previous operation. After this operation, nums = [4,1,3,2,2,3].
We cannot perform the next operation as its score is 4 + 1 = 5, which is different from the previous scores.
Example 3:

Input: nums = [5,3]

Output: 1

 

Constraints:

2 <= nums.length <= 100
1 <= nums[i] <= 1000
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
    def leetcode(self, nums: List[int]) -> int:
        ll = len(nums)
        if ll == 1:
            return 0
        result = 1
        sum2 = nums[0]+nums[1]
        for ii in range(1, ll//2):
            if nums[ii*2]+nums[ii*2+1] == sum2:
                result += 1
            else:
                break
        return result


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
