"""
2349. Design a Number Container System

Design a number container system that can do the following:

Insert or Replace a number at the given index in the system.
Return the smallest index for the given number in the system.
Implement the NumberContainers class:

NumberContainers() Initializes the number container system.
void change(int index, int number) Fills the container at index with the number. If there is already a number at that index, replace it.
int find(int number) Returns the smallest index for the given number, or -1 if there is no index that is filled by number in the system.
 

Example 1:

Input
["NumberContainers", "find", "change", "change", "change", "change", "find", "change", "find"]
[[], [10], [2, 10], [1, 10], [3, 10], [5, 10], [10], [1, 20], [10]]
Output
[null, -1, null, null, null, null, 1, null, 2]

Explanation
NumberContainers nc = new NumberContainers();
nc.find(10); // There is no index that is filled with number 10. Therefore, we return -1.
nc.change(2, 10); // Your container at index 2 will be filled with number 10.
nc.change(1, 10); // Your container at index 1 will be filled with number 10.
nc.change(3, 10); // Your container at index 3 will be filled with number 10.
nc.change(5, 10); // Your container at index 5 will be filled with number 10.
nc.find(10); // Number 10 is at the indices 1, 2, 3, and 5. Since the smallest index that is filled with 10 is 1, we return 1.
nc.change(1, 20); // Your container at index 1 will be filled with number 20. Note that index 1 was filled with 10 and then replaced with 20. 
nc.find(10); // Number 10 is at the indices 2, 3, and 5. The smallest index that is filled with 10 is 2. Therefore, we return 2.
 

Constraints:

1 <= index, number <= 109
At most 105 calls will be made in total to change and find.
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

class NumberContainers:

    def __init__(self):
        self.count = 0
        self.index = defaultdict(int)
        self.number = defaultdict(list)
   

    def change(self, index: int, number: int) -> None:
        if index in self.index:
            if index == 20:
                print(self.index)
            existing_number = self.index[index]
            if existing_number == number:
                return
            if index in self.number[existing_number]:
                self.number[existing_number].remove(index)

        self.index[index] = number

        if number not in self.number:
            self.number[number] = [index]
            return
        ll = len(self.number[number])
        if len (self.number[number]) == 0:
            self.number[number] = [index]
            return

        if index < self.number[number][0]:
            self.number[number] = [index]+self.number[number]
        elif index > self.number[number][-1]:
            self.number[number].append(index)
        elif index in self.number[number]:
            pass
        else:
            self.number[number].append(index)
            self.number[number].sort()
            # for ii in range(0,ll):
            #     if index < self.number[number][ii]:
            #         self.number[number] = self.number[number][0:ii] + [index] + self.number[number][ii:]


    def find(self, number: int) -> int:
        if number not in self.number:
            return -1
        if len(self.number[number]) == 0:
            return -1
        return self.number[number][0]

        


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
