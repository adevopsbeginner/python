'''
100264. Longest Strictly Increasing or Strictly Decreasing Subarray
User Accepted:6253
User Tried:7223
Total Accepted:6322
Total Submissions:9688
Difficulty:Easy
You are given an array of integers nums. Return the length of the longest subarray of nums which is either strictly increasing or strictly decreasing.

 

Example 1:

Input: nums = [1,4,3,3,2]

Output: 2

Explanation:

The strictly increasing subarrays of nums are [1], [2], [3], [3], [4], and [1,4].

The strictly decreasing subarrays of nums are [1], [2], [3], [3], [4], [3,2], and [4,3].

Hence, we return 2.

Example 2:

Input: nums = [3,3,3,3]

Output: 1

Explanation:

The strictly increasing subarrays of nums are [3], [3], [3], and [3].

The strictly decreasing subarrays of nums are [3], [3], [3], and [3].

Hence, we return 1.

Example 3:

Input: nums = [3,2,1]

Output: 3

Explanation:

The strictly increasing subarrays of nums are [3], [2], and [1].

The strictly decreasing subarrays of nums are [3], [2], [1], [3,2], [2,1], and [3,2,1].

Hence, we return 3.

 

Constraints:

1 <= nums.length <= 50
1 <= nums[i] <= 50
'''
from typing import List

class Solution:
    def leetcode(self, nums: List[int]) -> int:
        ll = len(nums)
        if ll < 2:
            return ll
        
        start = end = 0
        increase = 1
        while start < ll:
            for end in range(start+1,ll):
                if nums[end] > nums[end-1]:
                    increase = max(increase, end-start+1)
                    print(nums[start:end+1])
                    pass
                else:
                    start = end

                if end == ll-1:
                    start = ll
                    break

        start = end = 0
        decrease = 1
        while start < ll:
            for end in range(start+1,ll):
                if nums[end] < nums[end-1]:
                    decrease = max(decrease, end-start+1)
                    print(nums[start:end+1])
                    pass
                else:
                    start = end

                if end == ll-1:
                    start = ll
                    break

        return max(increase, decrease)

if __name__ == "__main__":
    app = Solution()
    test1 = [1,4,3,3,2]
    test1 = [3,3,3,3]
    test2 = [1,3,4]
    print(app.leetcode(test1))
