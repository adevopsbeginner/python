'''
100321. Find the Number of Good Pairs II
User Accepted:0
User Tried:0
Total Accepted:0
Total Submissions:0
Difficulty:Medium
You are given 2 integer arrays nums1 and nums2 of lengths n and m respectively. You are also given a positive integer k.

A pair (i, j) is called good if nums1[i] is divisible by nums2[j] * k (0 <= i <= n - 1, 0 <= j <= m - 1).

Return the total number of good pairs.

 

Example 1:

Input: nums1 = [1,3,4], nums2 = [1,3,4], k = 1

Output: 5

Explanation:

The 5 good pairs are (0, 0), (1, 0), (1, 1), (2, 0), and (2, 2).
Example 2:

Input: nums1 = [1,2,4,12], nums2 = [2,4], k = 3

Output: 2

Explanation:

The 2 good pairs are (3, 0) and (3, 1).

 

Constraints:

1 <= n, m <= 10^5
1 <= nums1[i], nums2[j] <= 10^6
1 <= k <= 10^3
'''
from typing import List
from collections import defaultdict

class Solution:
    def leetcode(self, nums1: List[int], nums2: List[int], k: int) -> int:
        d1 = defaultdict(int)
        d2 = defaultdict(int)
        for each in nums1:
            if each >= k and each % k  == 0:
                d1[each//k] += 1

        for each in nums2:
            d2[each] += 1

        count = 0
        for each1 in d1:
            for each2 in d2:
                if each1 >= each2 and each1 % each2 == 0:
                    count += d1[each1]*d2[each2]

        return count
        

if __name__ == "__main__":
    app = Solution()
    a = [6,12,18]
    b = [1,2,3]
    k = 2
    print(app.leetcode(a,b,k))
