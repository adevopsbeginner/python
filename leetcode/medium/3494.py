"""
3494. Find the Minimum Amount of Time to Brew Potions
Attempted
Medium
Topics
premium lock icon
Companies
Hint
You are given two integer arrays, skill and mana, of length n and m, respectively.

In a laboratory, n wizards must brew m potions in order. Each potion has a mana capacity mana[j] and must pass through all the wizards sequentially to be brewed properly. The time taken by the ith wizard on the jth potion is timeij = skill[i] * mana[j].

Since the brewing process is delicate, a potion must be passed to the next wizard immediately after the current wizard completes their work. This means the timing must be synchronized so that each wizard begins working on a potion exactly when it arrives. ​

Return the minimum amount of time required for the potions to be brewed properly.

 

Example 1:

Input: skill = [1,5,2,4], mana = [5,1,4,2]

Output: 110

Explanation:

Potion Number   Start time  Wizard 0 done by    Wizard 1 done by    Wizard 2 done by    Wizard 3 done by
0   0   5   30  40  60
1   52  53  58  60  64
2   54  58  78  86  102
3   86  88  98  102 110
As an example for why wizard 0 cannot start working on the 1st potion before time t = 52, consider the case where the wizards started preparing the 1st potion at time t = 50. At time t = 58, wizard 2 is done with the 1st potion, but wizard 3 will still be working on the 0th potion till time t = 60.

Example 2:

Input: skill = [1,1,1], mana = [1,1,1]

Output: 5

Explanation:

Preparation of the 0th potion begins at time t = 0, and is completed by time t = 3.
Preparation of the 1st potion begins at time t = 1, and is completed by time t = 4.
Preparation of the 2nd potion begins at time t = 2, and is completed by time t = 5.
Example 3:

Input: skill = [1,2,3,4], mana = [1,2]

Output: 21

 

Constraints:

n == skill.length
m == mana.length
1 <= n, m <= 5000
1 <= mana[i], skill[i] <= 5000
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
    def leetcode(self, skill: List[int], mana: List[int]) -> int:
        n = len(skill)
        m = len(mana)

        sum_skills = sum(skill)

        ### first potion
        next_wizard_start = sum_skills * mana[0]

        for mm in range(1, m):
            wizard_finish_last_potion = next_wizard_start
            for nn in range(n-2, -1, -1):
                wizard_finish_last_potion -= skill[nn+1] * mana[mm-1]
                wizard_finish_current_potion = next_wizard_start - skill[nn] * mana[mm]
                next_wizard_start = max(wizard_finish_last_potion, wizard_finish_current_potion)

            next_wizard_start += sum_skills * mana[mm]

        return next_wizard_start


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
