"""
3066. Minimum Operations to Exceed Threshold Value II

You are given a 0-indexed integer array nums, and an integer k.

In one operation, you will:

Take the two smallest integers x and y in nums.
Remove x and y from nums.
Add min(x, y) * 2 + max(x, y) anywhere in the array.
Note that you can only apply the described operation if nums contains at least two elements.

Return the minimum number of operations needed so that all elements of the array are greater than or equal to k.

 

Example 1:

Input: nums = [2,11,10,1,3], k = 10
Output: 2
Explanation: In the first operation, we remove elements 1 and 2, then add 1 * 2 + 2 to nums. nums becomes equal to [4, 11, 10, 3].
In the second operation, we remove elements 3 and 4, then add 3 * 2 + 4 to nums. nums becomes equal to [10, 11, 10].
At this stage, all the elements of nums are greater than or equal to 10 so we can stop.
It can be shown that 2 is the minimum number of operations needed so that all elements of the array are greater than or equal to 10.
Example 2:

Input: nums = [1,1,2,4,9], k = 20
Output: 4
Explanation: After one operation, nums becomes equal to [2, 4, 9, 3].
After two operations, nums becomes equal to [7, 4, 9].
After three operations, nums becomes equal to [15, 9].
After four operations, nums becomes equal to [33].
At this stage, all the elements of nums are greater than 20 so we can stop.
It can be shown that 4 is the minimum number of operations needed so that all elements of the array are greater than or equal to 20.
 

Constraints:

2 <= nums.length <= 2 * 105
1 <= nums[i] <= 109
1 <= k <= 109
The input is generated such that an answer always exists. That is, there exists some sequence of operations after which all elements of the array are greater than or equal to k.
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
        heapq.heapify(nums)
        result = 0
        while len(nums) > 1 and nums[0] < k:
            x = heapq.heappop(nums)
            y = heapq.heappop(nums)
            heapq.heappush(nums, min(x,y)*2+max(x,y))
            result += 1

        return result

        ### worst solution ever
        ll = len(nums)
        nums.sort()
        nums.append(k+1)
        print(nums)
        
        result = 0
        min12 = [k]*(ll+1)
        min12[0] =nums[0]*2+nums[1]
        index12 = 0
        index12last = 0
        index = 0
        while index < ll or min12[index12] < k:
            if nums[index] >= k and min12[index12] >= k:
                break
            result += 1
            if index >= ll:
                min1 = min12[index12]
                min2 = min12[index12+1]
                index12 += 2
            elif min12[index12+1] <= nums[index]:
                min1 = min12[index12]
                min2 = min12[index12+1]
                index12 += 2
            elif min12[index12] <= nums[index]:
                min1 = min12[index12]
                min2 = nums[index]
                index += 1
                index12 += 1
            elif min12[index12] <= nums[index+1]:
                min1 = nums[index]
                min2 = min12[index12]
                index += 1
                index12 += 1
            else:
                min1 = nums[index]
                min2 = nums[index+1]
                index += 2

            min12[index12last] = min1*2+min2
            index12last += 1
            #print(result, k, index,min12, min1,min2)

        return result

        ### wrong answer since min12 could be possible lost
        ll = len(nums)
        nums.sort()
        nums.append(k+1)
        result = 0
        min12 = nums[0]*2+nums[1]
        if nums[0] < k:
            result += 1
        
        print(nums)
        for ii in range(2,ll):
            if nums[ii] >= k and min12 >= k:
                break
            min1 = min(min12, nums[ii])
            min2 = min(min12, nums[ii+1])
            print(result, k, min12,min1,min2)
            min12 = min1*2+min2
            result += 1
        return result

        ### time limit exceeded
        def newsort(to_insert, start, end):
            nonlocal nums
            #print(to_insert,nums[to_insert], start, nums[start], end, nums[end])
            if start > end:
                return
            if start == end or start+1 == end:
                if nums[to_insert] > nums[start]:
                    nums = nums[:to_insert]+nums[to_insert+1:start+1]+[nums[to_insert]] + nums[start+1:]
                else:
                    nums = nums[:to_insert]+nums[to_insert+1:start]+[nums[to_insert]] + nums[start:]
                return
                
            middle = start + (end-start)//2

            if nums[to_insert] <= nums[middle]:
                newsort(to_insert, start, middle)
            else:
                newsort(to_insert, middle, end)

        nums.append(k)
        ll = len(nums)
        nums.sort()
        result = 0
        ii = 0
        while ii < ll:
            ii += 1
            #print(ii, result, nums)
            if nums[ii-1] >= k:
                break

            result += 1
            nums[ii] += nums[ii-1]*2

            if nums[ii] >= k:
                ii += 1
                continue

            newsort(ii,ii+1,ll-1)
            #print(ii,result,nums)

            # for jj in range(ii+1,ll):
            #     if nums[jj] < nums[jj-1]:
            #         nums[jj], nums[jj-1] = nums[jj-1], nums[jj]
            #     else:
            #         break

        return result



if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
