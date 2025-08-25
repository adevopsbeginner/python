"""

Code
Testcase
Test Result
Test Result
100365. Minimum Array Changes to Make Differences Equal
Medium
You are given an integer array nums of size n where n is even, and an integer k.

You can perform some changes on the array, where in one change you can replace any element in the array with any integer in the range from 0 to k.

You need to perform some changes (possibly none) such that the final array satisfies the following condition:

There exists an integer X such that abs(a[i] - a[n - i - 1]) = X for all (0 <= i < n).
Return the minimum number of changes required to satisfy the above condition.



Example 1:

Input: nums = [1,0,1,2,4,3], k = 4

Output: 2

Explanation:
We can perform the following changes:

Replace nums[1] by 2. The resulting array is nums = [1,2,1,2,4,3].
Replace nums[3] by 3. The resulting array is nums = [1,2,1,3,4,3].
The integer X will be 2.

Example 2:

Input: nums = [0,1,2,3,3,6,5,4], k = 6

Output: 2

Explanation:
We can perform the following operations:

Replace nums[3] by 0. The resulting array is nums = [0,1,2,0,3,6,5,4].
Replace nums[4] by 4. The resulting array is nums = [0,1,2,0,4,6,5,4].
The integer X will be 4.



Constraints:

2 <= n == nums.length <= 105
n is even.
0 <= nums[i] <= k <= 105
"""

from typing import List
from collections import defaultdict

class Solution:
    def leetcode(self, nums: List[int], k: int) -> int:
        ll = len(nums)
        ll2 = ll // 2
        labs = [0] * ll2
        for ii in range(ll2):
            labs[ii] = abs(nums[ii]-nums[ll-ii-1])
        dd = defaultdict(int)
        for each in labs:
            dd[each] += 1

        ## try#2
        result = ll
        for each in dd:
            total1 = ll2-dd[each]
            if total1 > result:
                continue
            for jj in range(ll2):
                if max(nums[jj], nums[ll - jj - 1]) - each < 0 and min(nums[jj], nums[ll - jj - 1]) + each > k:
                    total1 += 1
                    if total1 > result:
                        break
            result = min(result,total1)
        return result

        ## try#1, not working

        maxvalue = 0
        diff = 0
        for each in dd:
            if dd[each] > maxvalue:
                maxvalue = dd[each]
                diff = each
        result = ll2-maxvalue
        for ii in range(ll2):
            if abs(nums[ii]-nums[ll-ii-1]) == diff:
                continue
            print(nums[ii],diff,result)
            if max(nums[ii],nums[ll-ii-1])-diff < 0 and min(nums[ii],nums[ll-ii-1])+diff > k:
                result += 1

        return result

if __name__ == "__main__":
    app = Solution()
    a = [0,1,2,3,3,6,5,4]
    k = 6
    a = [1,10,5,1,4,6,4,2,4,9,7,9,0,11]
    k = 12
    print(app.leetcode(a,k))
