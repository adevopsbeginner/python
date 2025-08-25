"""
Q2. Closest Equal Element Queries
Medium
4 pt.
You are given a circular array nums and an array queries.

For each query i, you have to find the following:

The minimum distance between the element at index queries[i] and any other index j in the circular array, where nums[j] == nums[queries[i]]. If no such index exists, the answer for that query should be -1.
Return an array answer of the same size as queries, where answer[i] represents the result for query i.

 

Example 1:

Input: nums = [1,3,1,4,1,3,2], queries = [0,3,5]

Output: [2,-1,3]

Explanation:

Query 0: The element at queries[0] = 0 is nums[0] = 1. The nearest index with the same value is 2, and the distance between them is 2.
Query 1: The element at queries[1] = 3 is nums[3] = 4. No other index contains 4, so the result is -1.
Query 2: The element at queries[2] = 5 is nums[5] = 3. The nearest index with the same value is 1, and the distance between them is 3 (following the circular path: 5 -> 6 -> 0 -> 1).
Example 2:

Input: nums = [1,2,3,4], queries = [0,1,2,3]

Output: [-1,-1,-1,-1]

Explanation:

Each value in nums is unique, so no index shares the same value as the queried element. This results in -1 for all queries.

 

Constraints:

1 <= queries.length <= nums.length <= 105
1 <= nums[i] <= 106
0 <= queries[i] < nums.length
"""

from typing import List
from collections import defaultdict

class Solution:
    def leetcode(self, nums: List[int], queries: List[int]) -> List[int]:
        ll = len(nums)
        dd = defaultdict(list)
        for ii in range(ll):
            dd[nums[ii]].append(ii)
        for each in dd:
            dd[each].sort()
        llq = len(queries)
        result = [0]*llq
        for ii in range(llq):
            element = nums[queries[ii]]
            lldd = len(dd[element])
            if lldd <= 1:
                result[ii] = -1
                continue
            jj = bisect_left(dd[element], queries[ii])
            if jj == 0:
                result[ii] = min(dd[element][0]+ll-dd[element][-1], dd[element][jj+1]-dd[element][jj])
            elif jj == lldd-1:
                result[ii] = min(dd[element][-1]-dd[element][-2], dd[element][0]+ll-dd[element][-1])
            else:
                result[ii] = min(dd[element][jj]-dd[element][(jj-1)], dd[element][(jj+1)]-dd[element][jj])
            
        return result

if __name__ == "__main__":
    app = Solution()
    a = [1,4,3,3,2]
    b = 2
    print(app.leetcode(a))
