"""
3233. Find the Count of Numbers Which Are Not Special
Solved
Medium
Companies
Hint
You are given 2 positive integers l and r. For any number x, all positive divisors of x except x are called the proper divisors of x.

A number is called special if it has exactly 2 proper divisors. For example:

The number 4 is special because it has proper divisors 1 and 2.
The number 6 is not special because it has proper divisors 1, 2, and 3.
Return the count of numbers in the range [l, r] that are not special.



Example 1:

Input: l = 5, r = 7

Output: 3

Explanation:

There are no special numbers in the range [5, 7].

Example 2:

Input: l = 4, r = 16

Output: 11

Explanation:

The special numbers in the range [4, 16] are 4 and 9.



Constraints:

1 <= l <= r <= 109
"""

from typing import List
from collections import defaultdict

class Solution:
    def leetcode(self, l: int, r: int) -> int:
        def is_prime(n):
            """Return True if n is a prime number, else False."""
            if n <= 1:
                return False
            if n == 2:
                return True
            if n % 2 == 0:
                return False
            max_divisor = int(n**0.5) + 1
            for d in range(3, max_divisor, 2):
                if n % d == 0:
                    return False
            return True

        result = r-l+1

        for ii in range(2,100000000):
            ii2 = ii*ii
            if ii2 < l:
                continue
            if ii2 > r:
                break

            if is_prime(ii):
                result -= 1

        return result

if __name__ == "__main__":
    app = Solution()
    a = [1,4,3,3,2]
    b = 2
    print(app.leetcode(a))
