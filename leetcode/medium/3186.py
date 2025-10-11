"""
3186. Maximum Total Damage With Spell Casting
Solved
Medium
Topics
premium lock icon
Companies
Hint
A magician has various spells.

You are given an array power, where each element represents the damage of a spell. Multiple spells can have the same damage value.

It is a known fact that if a magician decides to cast a spell with a damage of power[i], they cannot cast any spell with a damage of power[i] - 2, power[i] - 1, power[i] + 1, or power[i] + 2.

Each spell can be cast only once.

Return the maximum possible total damage that a magician can cast.

 

Example 1:

Input: power = [1,1,3,4]

Output: 6

Explanation:

The maximum possible damage of 6 is produced by casting spells 0, 1, 3 with damage 1, 1, 4.

Example 2:

Input: power = [7,1,6,6]

Output: 13

Explanation:

The maximum possible damage of 13 is produced by casting spells 1, 2, 3 with damage 1, 6, 6.

 

Constraints:

1 <= power.length <= 105
1 <= power[i] <= 109
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
    def leetcode(self, power: List[int]) -> int:
        ll = len(power)
        power.sort()
        dd = Counter(power)

        dp = dp1 = dp2 = dp3 = 0
        power1 = -1
        power2 = -2
        power3 = -5

        for each in dd:
            if power2 < each-2:
                dp3 = dp2
                power3 = power2
            
            if power1 == each-2:
                dp2 = dp1
                power2 = power1
            elif power1 < each-2:
                dp3 = dp1
                power3 = 1

            dp = max(dp3+each*dd[each], dp1)

            dp3, dp2, dp1 = dp2, dp1, dp
            power3, power2, power1 = power2, power1, each

        return dp

        ### 2024
        ll = len(power)
        power.sort()
        dd = defaultdict(int)
        # dd = Counter(power)
        # for each in dd:
        #     print(each,dd[each])

        for each in power:
            dd[each] += 1

        result = 0
        dp3 = 0
        dp2 = 0
        dp1 = 0
        dp0 = 0
        qi3 = -5
        qi2 = -2
        qi1 = -1
        qi0 = 0

        # for each in dd:
        #     print(each,dd[each])

        for each in dd:
            if qi2 < each-2:
                dp3 = dp2
                qi3 = qi2

            if qi1 == each - 2:
                dp2 = dp1
                qi2 = qi1
            elif qi1 < each-2:
                dp3 = dp1
                qi3 = qi1

            xx = each * dd[each]
            dp0 = max(dp3 + xx, dp1)
            qi0 = each

            dp3 = dp2
            dp2 = dp1
            dp1 = dp0
            qi3 = qi2
            qi2 = qi1
            qi1 = qi0

            #print(qi3,qi2,qi1,qi0,dp3,dp2,dp1,dp0)

        return dp0
    
        ll = len(power)
        power.sort()
        freq = Counter(power)
    
        # Extract unique damages and sort them
        unique_damages = sorted(freq.keys())

        # Initialize DP dictionary
        dp = {}

        for damage in unique_damages:
            # Maximum damage if we exclude this spell
            exclude_damage = dp.get(damage - 1, 0)

            # Maximum damage if we include this spell
            include_damage = damage * freq[damage]

            # Add the best previous damage that does not conflict
            if damage - 3 in dp:
                include_damage += dp[damage - 3]
            elif damage - 4 in dp:
                include_damage += dp[damage - 4]

            # Calculate the maximum damage for the current spell damage
            dp[damage] = max(exclude_damage, include_damage)

        # The maximum value in dp will be our answer
        return max(dp.values())

        freq = Counter(power)
    
        # Extract unique damages and sort them
        unique_damages = sorted(freq.keys())

        # Initialize DP dictionary
        dp = {}

        for damage in unique_damages:
            # Maximum damage if we exclude this spell
            exclude_damage = dp.get(damage - 1, 0)

            # Maximum damage if we include this spell
            include_damage = damage * freq[damage] + dp.get(damage - 3, 0)

            # Calculate the maximum damage for the current spell damage
            dp[damage] = max(exclude_damage, include_damage)

        # The maximum value in dp will be our answer
        return max(dp.values())


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
