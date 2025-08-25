"""
1482. Minimum Number of Days to Make m Bouquets
Medium
Topics
Companies
Hint
You are given an integer array bloomDay, an integer m and an integer k.

You want to make m bouquets. To make a bouquet, you need to use k adjacent flowers from the garden.

The garden consists of n flowers, the ith flower will bloom in the bloomDay[i] and then can be used in exactly one bouquet.

Return the minimum number of days you need to wait to be able to make m bouquets from the garden. If it is impossible to make m bouquets return -1.



Example 1:

Input: bloomDay = [1,10,3,10,2], m = 3, k = 1
Output: 3
Explanation: Let us see what happened in the first three days. x means flower bloomed and _ means flower did not bloom in the garden.
We need 3 bouquets each should contain 1 flower.
After day 1: [x, _, _, _, _]   // we can only make one bouquet.
After day 2: [x, _, _, _, x]   // we can only make two bouquets.
After day 3: [x, _, x, _, x]   // we can make 3 bouquets. The answer is 3.
Example 2:

Input: bloomDay = [1,10,3,10,2], m = 3, k = 2
Output: -1
Explanation: We need 3 bouquets each has 2 flowers, that means we need 6 flowers. We only have 5 flowers so it is impossible to get the needed bouquets and we return -1.
Example 3:

Input: bloomDay = [7,7,7,7,12,7,7], m = 2, k = 3
Output: 12
Explanation: We need 2 bouquets each should have 3 flowers.
Here is the garden after the 7 and 12 days:
After day 7: [x, x, x, x, _, x, x]
We can make one bouquet of the first three flowers that bloomed. We cannot make another bouquet from the last three flowers that bloomed because they are not adjacent.
After day 12: [x, x, x, x, x, x, x]
It is obvious that we can make two bouquets in different ways.


Constraints:

bloomDay.length == n
1 <= n <= 105
1 <= bloomDay[i] <= 109
1 <= m <= 106
1 <= k <= n
"""

import string
import heapq
import math
from typing import List
from collections import defaultdict


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def leetcode(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1

        def canMakeBouquets(days):
            bouquets = 0
            flowers = 0

            for bloom in bloomDay:
                if bloom <= days:
                    flowers += 1
                    if flowers == k:
                        bouquets += 1
                        flowers = 0
                else:
                    flowers = 0

                if bouquets >= m:
                    return True
            return False

        low, high = 1, max(bloomDay)

        while low < high:
            mid = (low + high) // 2
            if canMakeBouquets(mid):
                high = mid
            else:
                low = mid + 1

        return low

        n = len(bloomDay)
        if n < m * k:
            return -1

        result = max(bloomDay[:m * k])
        for ii in range(n):
            if bloomDay[ii] == 5364:
                print(ii)

        for ii in range(m):
            if ii == m-1:
                max1 = 0
            else:
                max1 = max(bloomDay[:((m - ii - 1) * k)])
            max2 = max(bloomDay[(m-ii-1)*k:(m-ii)*k])
            if ii == 0:
                max3 = 0
            else:
                max3 = max(bloomDay[(n-ii*k):])
            current = max(max1, max2, max3)
            for jj in range(n - m * k):
                i1 = jj + (m-ii-1) * k
                i2 = jj + (m-ii) * k
                # if ii in [29,30,31]:
                #     print(ii,jj,i1,i2)
                #print(result,i1, bloomDay[i1], i2, bloomDay[i2])
                # if bloomDay[i1] < current:
                #     continue
                # if bloomDay[i2] >= current:
                #     continue
                new = max(max1, max(bloomDay[i1 + 1:i2 + 1]), max3)
                current = min(current, new)
                if bloomDay[i1] == 5364:
                    print(1,ii, jj, result, current)
                if max(bloomDay[i1 + 1:i2 + 1]) == 5364:
                    print(4,ii, jj, i1,i2, result, current, max1,max3)


            result = min(result, current)

        return result

if __name__ == "__main__":
    app = Solution()
    a = [1,10,3,10,2]
    m = 3
    k = 1
    a = [1542,5142,4695,4385,2629,2492,933,1068,151,3960,3790,1196,3842,5147,5526,5528,2259,1708,2714,5462,3016,3262,1175,4348,4826,80,789,5285,3855,3455,3480,4277,648,1748,625,4256,3931,4938,4553,2129,4480,824,3048,2383,3036,2192,2156,7,438,5258,2430,2459,3769,1694,1687,5130,70,3219,4140,2341,1159,3952,4934,4335,2786,3124,5344,803,4586,1000,2821,4769,629,4673,3920,3437,4533,2984,3576,5364,1255,1876,2309,5619,2402,1978,4127,1668,147,4139,292,1499,1786,2435,1988,146,500,3377,3789,1301,1193,1686,3501,3895,1321,1587,4263,593,1580,3652,1638,4905,1927,567,2797,2082,1349,4158,679,4944,4638,4770,3458,2117,2620,938,4121,2374,1478,5269,5548,5125,5237,1693,2188,690,4640,827,2721,2329,430,4423,5510,2312,2493,4884,223,1904,4660,5124,2851,5227,4160,694,5660,5571,834,1704,4550,988,573,3373,5419,311,4280,399,5319,4723,5467,1155,4267,303,4233,770,3087,3306,1042,4192,3736,893,5087,1903,3650,393,5304,2767,3562,5501,4789,1863,1653,2528,5521,3802,3925,2718,5402,2642,304,4171,4356,5486,1426,4526,4541,4310,2160,4542,2850,2396,1612,4780,3921,5219,2585,4027,1861,3799,101,1434,996,203,1216,1654,4382,3791,3417,1912,5337,814,352,3892,3851,3432,2400]
    m = 49
    k = 4
    print(app.leetcode(a,m,k))
