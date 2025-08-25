"""
432. All O`one Data Structure
Hard
Topics
Companies
Design a data structure to store the strings' count with the ability to return the strings with minimum and maximum counts.

Implement the AllOne class:

AllOne() Initializes the object of the data structure.
inc(String key) Increments the count of the string key by 1. If key does not exist in the data structure, insert it with count 1.
dec(String key) Decrements the count of the string key by 1. If the count of key is 0 after the decrement, remove it from the data structure. It is guaranteed that key exists in the data structure before the decrement.
getMaxKey() Returns one of the keys with the maximal count. If no element exists, return an empty string "".
getMinKey() Returns one of the keys with the minimum count. If no element exists, return an empty string "".
Note that each function must run in O(1) average time complexity.

 

Example 1:

Input
["AllOne", "inc", "inc", "getMaxKey", "getMinKey", "inc", "getMaxKey", "getMinKey"]
[[], ["hello"], ["hello"], [], [], ["leet"], [], []]
Output
[null, null, null, "hello", "hello", null, "hello", "leet"]

Explanation
AllOne allOne = new AllOne();
allOne.inc("hello");
allOne.inc("hello");
allOne.getMaxKey(); // return "hello"
allOne.getMinKey(); // return "hello"
allOne.inc("leet");
allOne.getMaxKey(); // return "hello"
allOne.getMinKey(); // return "leet"
 

Constraints:

1 <= key.length <= 10
key consists of lowercase English letters.
It is guaranteed that for each call to dec, key is existing in the data structure.
At most 5 * 104 calls will be made to inc, dec, getMaxKey, and getMinKey.
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

class AllOne:

    def __init__(self):
        self.dd = defaultdict(int)
        self.max = ""
        self.maxcount = 0
        self.min = ""
        self.mincount = 0
        
    def redo(self, key: str) -> None:
        #print("redo1", key,self.min,self.mincount,self.max,self.maxcount)
        # for each in self.dd:
        #     print(each,self.dd[each],self.min,self.mincount,self.max,self.maxcount)
        self.min = ""
        self.mincount = 100000
        self.max = ""
        self.maxcount = 0
        for each in self.dd:
            ddeach = self.dd[each]
            if ddeach > 0 and ddeach <= self.mincount:
                self.mincount = ddeach
                self.min = each
            if ddeach >= self.maxcount:
                self.maxcount = ddeach
                self.max = each
        #print("redo2", key,self.min,self.mincount,self.max,self.maxcount)

    def inc(self, key: str) -> None:
        #print("inc", key,self.min,self.mincount,self.max,self.maxcount)
        if self.dd[key] == 0:
            self.min = key
            self.mincount = 1
            if self.maxcount == 0:
                self.max = key
                self.maxcount = 1
        self.dd[key] += 1
        #if key == self.min or self.dd[key] >= self.maxcount:
        if key == self.max:
            self.maxcount = self.dd[key]
            if key == self.min:
                self.redo(key)
        else:
            if key == self.min:
                self.redo(key)
            if self.dd[key] >= self.maxcount:
                self.redo(key)

    def dec(self, key: str) -> None:
        if self.dd[key] == 0:
            return
        
        self.dd[key] -= 1
        if key == self.min:
            self.redo(key)
        if key == self.max:
            self.redo(key)
        if self.dd[key] < self.mincount:
            self.redo(key)

    def getMaxKey(self) -> str:
        return self.max
        count = 0
        result = ""
        for each in self.dd:
            if self.dd[each] > count:
                count = self.dd[each]
                result = each
        return result

    def getMinKey(self) -> str:
        return self.min
        count = 100000
        result = ""
        # for each in self.dd:
        #     print(each, self.dd[each])
        for each in self.dd:
            if self.dd[each] == 0:
                continue
            if self.dd[each] < count:
                count = self.dd[each]
                result = each
 
        return result
        


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
