"""

Code
Testcase
Test Result
Test Result
1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit
Attempted
Medium
Topics
Companies
Hint
Given an array of integers nums and an integer limit, return the size of the longest non-empty subarray such that the absolute difference between any two elements of this subarray is less than or equal to limit.

 

Example 1:

Input: nums = [8,2,4,7], limit = 4
Output: 2 
Explanation: All subarrays are: 
[8] with maximum absolute diff |8-8| = 0 <= 4.
[8,2] with maximum absolute diff |8-2| = 6 > 4. 
[8,2,4] with maximum absolute diff |8-2| = 6 > 4.
[8,2,4,7] with maximum absolute diff |8-2| = 6 > 4.
[2] with maximum absolute diff |2-2| = 0 <= 4.
[2,4] with maximum absolute diff |2-4| = 2 <= 4.
[2,4,7] with maximum absolute diff |2-7| = 5 > 4.
[4] with maximum absolute diff |4-4| = 0 <= 4.
[4,7] with maximum absolute diff |4-7| = 3 <= 4.
[7] with maximum absolute diff |7-7| = 0 <= 4. 
Therefore, the size of the longest subarray is 2.
Example 2:

Input: nums = [10,1,2,4,7,2], limit = 5
Output: 4 
Explanation: The subarray [2,4,7,2] is the longest since the maximum absolute diff is |2-7| = 5 <= 5.
Example 3:

Input: nums = [4,2,2,2,4,4,2,2], limit = 0
Output: 3
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 109
0 <= limit <= 109
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
    def leetcode(self, nums: List[int], limit: int) -> int:
        ll = len(nums)
        result = 0
        for ii in range(ll):
            maxsub = 0
            minsub = 0
            start = ii+result+1
            for jj in range(start,ll+1):
                print(result,ii,jj,maxsub,minsub)
                if jj < ll and nums[jj-1] >= minsub and nums[jj-1] <= maxsub:
                    result = max(result,jj-ii)
                    continue
                if jj<ll:
                    print(result,ii,jj,nums[jj], maxsub,minsub)
                maxsub = max(nums[ii:jj])
                minsub = min(nums[ii:jj])
                diffsub = abs(maxsub-minsub)
                print(result,ii,jj,maxsub,minsub,diffsub,nums[ii:jj])
                if diffsub <= limit:
                    result = max(result,jj-ii)
                else:
                    print(result,ii,jj,maxsub,minsub,diffsub,nums[ii:jj])
                    break

        return result

if __name__ == "__main__":
    app = Solution()
    a = [10,1,2,4,7,2]
    limit = 5
    a = [1,5,6,7,8,10,6,5,6]
    limit = 4
    print(app.leetcode(a,limit))
