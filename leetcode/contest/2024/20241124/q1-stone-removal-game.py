"""
Q1. Stone Removal Game
Easy
3 pt.
Alice and Bob are playing a game where they take turns removing stones from a pile, with Alice going first.

Alice starts by removing exactly 10 stones on her first turn.
For each subsequent turn, each player removes exactly 1 fewer stone than the previous opponent.
The player who cannot make a move loses the game.

Given a positive integer n, return true if Alice wins the game and false otherwise.

 

Example 1:

Input: n = 12

Output: true

Explanation:

Alice removes 10 stones on her first turn, leaving 2 stones for Bob.
Bob cannot remove 9 stones, so Alice wins.
Example 2:

Input: n = 1

Output: false

Explanation:

Alice cannot remove 10 stones, so Alice loses.
"""

from typing import List
from collections import defaultdict

class Solution:
    def leetcode(self, n: int) -> bool:
        start = 10
        alice_win = 1
        while start <= n:
            alice_win += 1
            n -= start
            start -= 1

        return alice_win%2 == 0

if __name__ == "__main__":
    app = Solution()
    a = [1,4,3,3,2]
    b = 2
    print(app.leetcode(a))
