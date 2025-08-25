"""

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
    def leetcode(self, arr: List[int]) -> bool:
        ll = len(arr)
        arr.sort()
        diff = arr[1] - arr[0]
        for ii in range(2,ll):
            if arr[ii] - arr[ii-1] != diff:
                return False

        return True


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
