"""
2409. Count Days Spent Together
Solved
Easy
Topics
Companies
Hint
Alice and Bob are traveling to Rome for separate business meetings.

You are given 4 strings arriveAlice, leaveAlice, arriveBob, and leaveBob. Alice will be in the city from the dates arriveAlice to leaveAlice (inclusive), while Bob will be in the city from the dates arriveBob to leaveBob (inclusive). Each will be a 5-character string in the format "MM-DD", corresponding to the month and day of the date.

Return the total number of days that Alice and Bob are in Rome together.

You can assume that all dates occur in the same calendar year, which is not a leap year. Note that the number of days per month can be represented as: [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31].

 

Example 1:

Input: arriveAlice = "08-15", leaveAlice = "08-18", arriveBob = "08-16", leaveBob = "08-19"
Output: 3
Explanation: Alice will be in Rome from August 15 to August 18. Bob will be in Rome from August 16 to August 19. They are both in Rome together on August 16th, 17th, and 18th, so the answer is 3.
Example 2:

Input: arriveAlice = "10-01", leaveAlice = "10-31", arriveBob = "11-01", leaveBob = "12-31"
Output: 0
Explanation: There is no day when Alice and Bob are in Rome together, so we return 0.
 

Constraints:

All dates are provided in the format "MM-DD".
Alice and Bob's arrival dates are earlier than or equal to their leaving dates.
The given dates are valid dates of a non-leap year.
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
    def leetcode(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        """
        :type arriveAlice: str
        :type leaveAlice: str
        :type arriveBob: str
        :type leaveBob: str
        :rtype: int
        """
        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        days = [0]*13
        for ii in range(1,13):
            days[ii] += days[ii-1] + days_in_month[ii-1]
        #print(days)
        arrive_alice = days[int(arriveAlice[0:2])-1] + int(arriveAlice[3:])
        leave_alice = days[int(leaveAlice[0:2])-1] + int(leaveAlice[3:])
        arrive_bob = days[int(arriveBob[0:2])-1] + int(arriveBob[3:])
        #print(leaveBob, leaveBob[0:2], leaveBob[3:])
        leave_bob = days[int(leaveBob[0:2])-1] + int(leaveBob[3:])
        #print(leave_alice, arrive_bob)

        # if arrive_alice > arrive_bob:
        #     arrive_alice, leave_alice, arrive_bob, leave_bob = arrive_bob, leave_bob, arrive_alice, leave_alice

        arrive = max(arrive_alice, arrive_bob)
        leave = min(leave_alice, leave_bob)

        return max(0, leave-arrive+1)


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
