"""
1114. Print in Order
Easy
Topics
Companies
Suppose we have a class:

public class Foo {
  public void first() { print("first"); }
  public void second() { print("second"); }
  public void third() { print("third"); }
}
The same instance of Foo will be passed to three different threads. Thread A will call first(), thread B will call second(), and thread C will call third(). Design a mechanism and modify the program to ensure that second() is executed after first(), and third() is executed after second().

Note:

We do not know how the threads will be scheduled in the operating system, even though the numbers in the input seem to imply the ordering. The input format you see is mainly to ensure our tests' comprehensiveness.

 

Example 1:

Input: nums = [1,2,3]
Output: "firstsecondthird"
Explanation: There are three threads being fired asynchronously. The input [1,2,3] means thread A calls first(), thread B calls second(), and thread C calls third(). "firstsecondthird" is the correct output.
Example 2:

Input: nums = [1,3,2]
Output: "firstsecondthird"
Explanation: The input [1,3,2] means thread A calls first(), thread B calls third(), and thread C calls second(). "firstsecondthird" is the correct output.
 

Constraints:

nums is a permutation of [1, 2, 3].
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

class Foo:
    def __init__(self):
        self.flagfirst = 0
        self.flagsecond = 0


    def first(self, printFirst: 'Callable[[], None]') -> None:
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.flagfirst = 1

    def second(self, printSecond: 'Callable[[], None]') -> None:
        for ii in range(5):
            if self.flagfirst == 0:
                time.sleep(0.1)
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.flagsecond = 1
        self.flagfirst = 0
        


    def third(self, printThird: 'Callable[[], None]') -> None:
        for ii in range(5):
            if self.flagsecond == 0:
                time.sleep(0.1)
        # printThird() outputs "third". Do not change or remove this line.
        printThird()
        self.flagsecond = 0


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
