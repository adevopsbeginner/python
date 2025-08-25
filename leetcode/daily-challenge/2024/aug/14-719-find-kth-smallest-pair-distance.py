"""

Code
Testcase
Test Result
Test Result
719. Find K-th Smallest Pair Distance
Hard
Topics
Companies
Hint
The distance of a pair of integers a and b is defined as the absolute difference between a and b.

Given an integer array nums and an integer k, return the kth smallest distance among all the pairs nums[i] and nums[j] where 0 <= i < j < nums.length.



Example 1:

Input: nums = [1,3,1], k = 1
Output: 0
Explanation: Here are all the pairs:
(1,3) -> 2
(1,1) -> 0
(3,1) -> 2
Then the 1st smallest distance pair is (1,1), and its distance is 0.
Example 2:

Input: nums = [1,1,1], k = 2
Output: 0
Example 3:

Input: nums = [1,6,1], k = 3
Output: 5


Constraints:

n == nums.length
2 <= n <= 104
0 <= nums[i] <= 106
1 <= k <= n * (n - 1) / 2
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
    def leetcode(self, nums: List[int], k: int) -> int:
        def count_pairs(nums, mid):
            count = 0
            left = 0
            for right in range(1, len(nums)):
                while nums[right] - nums[left] > mid:
                    left += 1
                count += right - left
            return count

        # def smallestDistancePair(nums, k):
        nums.sort()
        low, high = 0, nums[-1] - nums[0]

        while low < high:
            mid = (low + high) // 2
            if count_pairs(nums, mid) < k:
                low = mid + 1
            else:
                high = mid

        return low

        ### solution #3, time limit exceeded
        ll = len(nums)
        dd = defaultdict(int)
        for each in nums:
            dd[each] += 1

        total0 = 0
        for each in dd:
            total0 += dd[each]*(dd[each]-1)//2

        if k <= total0:
            return 0
        k -= total0

        ldd = list(dd.keys())
        #print(ldd)
        lld = len(ldd)

        dd2 = defaultdict(int)
        for r in range(lld-1):
            for c in range(r+1,lld):
                diff = abs(ldd[r]-ldd[c])
                dd2[diff] += dd[ldd[r]] * dd[ldd[c]]

        ldd2 = list(dd2.keys())
        ldd2.sort()
        #print(ldd2)
        for each in ldd2:
            #print(k)
            if k <= dd2[each]:
                return each
            k -= dd2[each]

        return ldd2[-1]

        ### solution 2
        matrix = [[0,0] for _ in range((lld*(lld-1))//2)]
        index = 0
        for r in range(lld-1):
            for c in range(r+1,lld):
                matrix[index][0] = abs(ldd[r]-ldd[c])
                matrix[index][1] = dd[ldd[r]] * dd[ldd[c]]
                index += 1
        matrix.sort()
        #print(matrix)
        for ii in range(len(matrix)):
            if k <= matrix[ii][1]:
                return matrix[ii][0]
            k -= matrix[ii][1]

        return matrix[-1][0]

        ### solution 1, memory exceeded
        matrix = [1000000] * (ll*ll)
        for r in range(ll-1):
            for c in range(r+1,ll):
                matrix[r*ll + c] = abs(nums[r]-nums[c])
        matrix.sort()
        #print(matrix)

        return matrix[k-1]


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
