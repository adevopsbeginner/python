"""
2762. Continuous Subarrays
Medium
Topics
Companies
Hint
You are given a 0-indexed integer array nums. A subarray of nums is called continuous if:

Let i, i + 1, ..., j be the indices in the subarray. Then, for each pair of indices i <= i1, i2 <= j, 0 <= |nums[i1] - nums[i2]| <= 2.
Return the total number of continuous subarrays.

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [5,4,2,4]
Output: 8
Explanation: 
Continuous subarray of size 1: [5], [4], [2], [4].
Continuous subarray of size 2: [5,4], [4,2], [2,4].
Continuous subarray of size 3: [4,2,4].
Thereare no subarrys of size 4.
Total continuous subarrays = 4 + 3 + 1 = 8.
It can be shown that there are no more continuous subarrays.
 

Example 2:

Input: nums = [1,2,3]
Output: 6
Explanation: 
Continuous subarray of size 1: [1], [2], [3].
Continuous subarray of size 2: [1,2], [2,3].
Continuous subarray of size 3: [1,2,3].
Total continuous subarrays = 3 + 2 + 1 = 6.
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 109
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
    def leetcode(self,  nums: List[int]) -> int:
        n = len(nums)
        start = 0
        count = 0
        
        max_deque = deque()  # Stores indices of max elements in descending order
        min_deque = deque()  # Stores indices of min elements in ascending order
        
        for end in range(n):
            # Maintain max_deque: Remove smaller elements from the back
            while max_deque and nums[max_deque[-1]] <= nums[end]:
                max_deque.pop()
            max_deque.append(end)
            
            # Maintain min_deque: Remove larger elements from the back
            while min_deque and nums[min_deque[-1]] >= nums[end]:
                min_deque.pop()
            min_deque.append(end)
            
            # Shrink the window if invalid
            while nums[max_deque[0]] - nums[min_deque[0]] > 2:
                start += 1
                if max_deque[0] < start:
                    max_deque.popleft()
                if min_deque[0] < start:
                    min_deque.popleft()
            
            # Add the count of valid subarrays ending at 'end'
            count += end - start + 1
        
        return count

        ll = len(nums)
        # maxnum = max(nums)
        # minnum = min(nums)
        # if maxnum-minnum <= 2:
        #     return ll*(ll+1)//2

        nums.append(nums[-1]+9)
        result = 0
        start = 1
        for ii in range(ll+1):
            if start == ll:
                result += start-ii
                continue
            if ii > 0 and nums[ii] == nums[ii-1]:
                result += start-ii
                continue

            if start > ii:
                maxi = max(nums[ii:start])
                mini = min(nums[ii:start])
            else:
                maxi = nums[ii]
                mini = nums[ii]
            while start < ll+1:
                #print(ii,start, nums[start], maxi, mini)
                if nums[start] > maxi:
                    maxi = nums[start]
                if nums[start] < mini:
                    mini = nums[start]
                if maxi-mini > 2:
                    result += start-ii
                    break
                start += 1

        return result


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
