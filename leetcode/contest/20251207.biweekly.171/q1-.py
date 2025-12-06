"""
Q1. Complete Prime Number
Medium
4 pt.
You are given an integer num.

A number num is called a Complete Prime Number if every prefix and every suffix of num is prime.

Return true if num is a Complete Prime Number, otherwise return false.

Note:

A prefix of a number is formed by the first k digits of the number.
A suffix of a number is formed by the last k digits of the number.
A prime number is a natural number greater than 1 with only two factors, 1 and itself.
Single-digit numbers are considered Complete Prime Numbers only if they are prime.
 

Example 1:

Input: num = 23

Output: true

Explanation:

​​​​​​​Prefixes of num = 23 are 2 and 23, both are prime.
Suffixes of num = 23 are 3 and 23, both are prime.
All prefixes and suffixes are prime, so 23 is a Complete Prime Number and the answer is true.
Example 2:

Input: num = 39

Output: false

Explanation:

Prefixes of num = 39 are 3 and 39. 3 is prime, but 39 is not prime.
Suffixes of num = 39 are 9 and 39. Both 9 and 39 are not prime.
At least one prefix or suffix is not prime, so 39 is not a Complete Prime Number and the answer is false.
Example 3:

Input: num = 7

Output: true

Explanation:

7 is prime, so all its prefixes and suffixes are prime and the answer is true.
 

Constraints:

1 <= num <= 109
"""

from typing import List
from collections import defaultdict

class Solution:
    def leetcode(self, num: int) -> bool:
        def is_prime(num):
            if num <= 1:
                return False
            if num <= 3:
                return True
            if num%2 == 0 or num%3 == 0:
                return False
            ii = 5
            while ii*ii <= num:
                if num%ii == 0 or num%(ii+2) == 0:
                    return False
                ii += 6
                
            return True
            
        if not is_prime(num):
            return False
            
        strnum = str(num)
        for each in "4680":
            if each in strnum:
                return False
        ll = len(strnum)
        for ii in range(1, ll):
            if not is_prime(int(strnum[:ii])):
                return False
            if not is_prime(int(strnum[ii:])):
                return False
                
        return True
