"""
Q3. Find the Count of Good Integers
Hard
7 pt.
You are given two positive integers n and k.

An integer x is called k-palindromic if:

x is a
palindrome
.
x is divisible by k.
An integer is called good if its digits can be rearranged to form a k-palindromic integer. For example, for k = 2, 2020 can be rearranged to form the k-palindromic integer 2002, whereas 1010 cannot be rearranged to form a k-palindromic integer.

Return the count of good integers containing n digits.

Note that any integer must not have leading zeros, neither before nor after rearrangement. For example, 1010 cannot be rearranged to form 101.



Example 1:

Input: n = 3, k = 5

Output: 27

Explanation:

Some of the good integers are:

551 because it can be rearranged to form 515.
525 because it is already k-palindromic.
Example 2:

Input: n = 1, k = 4

Output: 2

Explanation:

The two good integers are 4 and 8.

Example 3:

Input: n = 5, k = 6

Output: 2468



Constraints:

1 <= n <= 10
1 <= k <= 9
"""

from typing import List
from collections import defaultdict

class Solution:
    def leetcode(self, n: int, k: int) -> int:
        ### chatgpt, but wrong answer or time exceeded
        def generate_palindromes(length):
            palindromes = set()

            if length == 1:
                return set(range(1, 10))

            half_length = (length + 1) // 2
            start = 10**(half_length - 1)
            end = 10**half_length

            for num in range(start, end):
                s = str(num)
                if length % 2 == 0:
                    palindrome = s + s[::-1]
                else:
                    palindrome = s + s[-2::-1]
                palindromes.add(int(palindrome))

            return palindromes

        def is_good_integer(digits, k):
            digit_count = Counter(digits)
            length = len(digits)

            palindromes = generate_palindromes(length)

            for p in palindromes:
                if p % k != 0:
                    continue
                p_str = str(p)
                p_count = Counter(p_str)
                if p_count == digit_count:
                    return True
            return False

        #def count_good_integers(n, k):
        if n < 1:
            return 0

        count = 0
        digits = [str(d) for d in range(1, 10)]

        for perm in permutations(digits * n, n):
            if perm[0] != '0' and is_good_integer(perm, k):
                count += 1

        return count
        #xx = [0,9,9,90,90,900,900,9000,9000,90000,90000]

if __name__ == "__main__":
    app = Solution()
    a = [1,4,3,3,2]
    b = 2
    print(app.leetcode(a))
