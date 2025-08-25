"""
729. My Calendar I
Attempted
Medium
Topics
Companies
Hint
You are implementing a program to use as your calendar. We can add a new event if adding the event will not cause a double booking.

A double booking happens when two events have some non-empty intersection (i.e., some moment is common to both events.).

The event can be represented as a pair of integers start and end that represents a booking on the half-open interval [start, end), the range of real numbers x such that start <= x < end.

Implement the MyCalendar class:

MyCalendar() Initializes the calendar object.
boolean book(int start, int end) Returns true if the event can be added to the calendar successfully without causing a double booking. Otherwise, return false and do not add the event to the calendar.


Example 1:

Input
["MyCalendar", "book", "book", "book"]
[[], [10, 20], [15, 25], [20, 30]]
Output
[null, true, false, true]

Explanation
MyCalendar myCalendar = new MyCalendar();
myCalendar.book(10, 20); // return True
myCalendar.book(15, 25); // return False, It can not be booked because time 15 is already booked by another event.
myCalendar.book(20, 30); // return True, The event can be booked, as the first event takes every time less than 20, but not including 20.


Constraints:

0 <= start < end <= 109
At most 1000 calls will be made to book.
"""

import string
import heapq
from typing import List
from collections import defaultdict


class MyCalendar:

    def __init__(self):
        self.start = []
        self.end = []
        self.count = 0

    def book(self, start: int, end: int) -> bool:
        if self.count == 0:
            self.start.append(start)
            self.end.append(end)
            self.count += 1
            return True
        elif start >= self.end[-1]:
            # print(start,self.end[-1])
            self.start.append(start)
            self.end.append(end)
            self.count += 1
            return True

        for ii in range(self.count):
            if start < self.start[ii]:
                if end <= self.start[ii]:
                    if start == 8:
                        print(ii, start, end)
                    if ii == 0:
                        # print(111,start,end)
                        self.start = [start] + self.start
                        self.end = [end] + self.end
                        self.count += 1
                        return True
                    else:
                        if start >= self.end[ii - 1]:
                            self.start = self.start[:ii] + [start] + self.start[ii:]
                            self.end = self.end[:ii] + [end] + self.end[ii:]
                            self.count += 1
                            return True
                break

        return False


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
