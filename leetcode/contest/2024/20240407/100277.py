'''
100277. Minimum Operations to Make Median of Array Equal to KMy SubmissionsBack to Contest
User Accepted:82
User Tried:128
Total Accepted:83
Total Submissions:169
Difficulty:Medium
You are given an integer array nums and a non-negative integer k. In one operation, you can increase or decrease any element by 1.

Return the minimum number of operations needed to make the median of nums equal to k.

 

Example 1:

Input: nums = [2,5,6,8,5], k = 4

Output: 2

Explanation:

We can subtract one from nums[1] and nums[4] to obtain [2, 4, 6, 8, 4]. The median of the resulting array is equal to k.

Example 2:

Input: nums = [2,5,6,8,5], k = 7

Output: 3

Explanation:

We can add one to nums[1] twice and add one to nums[2] once to obtain [2, 7, 7, 8, 5].

Example 3:

Input: nums = [1,2,3,4,5,6], k = 4

Output: 0

Explanation:

The median of the array is already equal to k.

 

Constraints:

1 <= nums.length <= 2 * 105
1 <= nums[i] <= 109
1 <= k <= 109
'''
from typing import List

class Solution:
    def leetcode(self, nums: List[int], k: int) -> int:
        ll = len(nums)
        m = ll//2
        nums.sort()

        if nums[m] > k:
            if nums[0] >= k:
                return sum(nums[:m+1])-k*(m+1)
            for ii in range(m+1):
                if nums[ii] > k:
                    return sum(nums[ii:m+1])-k*(m+1-ii)
        if nums[m] < k:
            if nums[-1] <= k:
                return k*(m+ll%2)-sum(nums[m:])
            for ii in range(m+1,ll):
                if nums[ii] > k:
                    return k*(ii-m)-sum(nums[m:ii])

        return 0

if __name__ == "__main__":
    app = Solution()
    test1 = [1,4,3,3,2]
    test1 = [3,3,3,3]
    test1 = [1,1,1]
    k = 1000000
    test1 = [1]
    k = 1000000
    test1 = [7,62,90,68,88]
    k = 62
    test1 = [17,22,40,74,75,86]
    k = 86
    test2 = [1,3,4]
    print(app.leetcode(test1, k))
