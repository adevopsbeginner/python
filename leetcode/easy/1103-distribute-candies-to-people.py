"""
1103. Distribute Candies to People
Solved
Easy
Topics
Companies
Hint
We distribute some number of candies, to a row of n = num_people people in the following way:

We then give 1 candy to the first person, 2 candies to the second person, and so on until we give n candies to the last person.

Then, we go back to the start of the row, giving n + 1 candies to the first person, n + 2 candies to the second person, and so on until we give 2 * n candies to the last person.

This process repeats (with us giving one more candy each time, and moving to the start of the row after we reach the end) until we run out of candies.  The last person will receive all of our remaining candies (not necessarily one more than the previous gift).

Return an array (of length num_people and sum candies) that represents the final distribution of candies.

 

Example 1:

Input: candies = 7, num_people = 4
Output: [1,2,3,1]
Explanation:
On the first turn, ans[0] += 1, and the array is [1,0,0,0].
On the second turn, ans[1] += 2, and the array is [1,2,0,0].
On the third turn, ans[2] += 3, and the array is [1,2,3,0].
On the fourth turn, ans[3] += 1 (because there is only one candy left), and the final array is [1,2,3,1].
Example 2:

Input: candies = 10, num_people = 3
Output: [5,2,3]
Explanation: 
On the first turn, ans[0] += 1, and the array is [1,0,0].
On the second turn, ans[1] += 2, and the array is [1,2,0].
On the third turn, ans[2] += 3, and the array is [1,2,3].
On the fourth turn, ans[0] += 4, and the final array is [5,2,3].
 

Constraints:

1 <= candies <= 10^9
1 <= num_people <= 1000
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
    def leetcode(self, hcandies: int, num_people: int) -> List[int]:
        sqrt2 = floor(sqrt(2*candies))-1
        total = sqrt2*(sqrt2+1)//2
        while total <= candies:
            if total == candies:
                break
            if (sqrt2+2)*(sqrt2+1)//2 > candies:
                break
            else:
                sqrt2 += 1

        repeat = sqrt2//num_people
        result = [((ii+1)*repeat+num_people*repeat*(repeat-1)//2) for ii in range(num_people)]
        candies -= sum(result)
        for ii in range(num_people):
            this_time_share = repeat*num_people+(ii+1)
            if candies <= this_time_share:
                result[ii] += candies
                candies = 0
                break
            else:
                result[ii] += this_time_share
                candies -= this_time_share

        return result


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
