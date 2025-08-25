"""
1792. Maximum Average Pass Ratio
Attempted
Medium
Topics
Companies
Hint
There is a school that has classes of students and each class will be having a final exam. You are given a 2D integer array classes, where classes[i] = [passi, totali]. You know beforehand that in the ith class, there are totali total students, but only passi number of students will pass the exam.

You are also given an integer extraStudents. There are another extraStudents brilliant students that are guaranteed to pass the exam of any class they are assigned to. You want to assign each of the extraStudents students to a class in a way that maximizes the average pass ratio across all the classes.

The pass ratio of a class is equal to the number of students of the class that will pass the exam divided by the total number of students of the class. The average pass ratio is the sum of pass ratios of all the classes divided by the number of the classes.

Return the maximum possible average pass ratio after assigning the extraStudents students. Answers within 10-5 of the actual answer will be accepted.

 

Example 1:

Input: classes = [[1,2],[3,5],[2,2]], extraStudents = 2
Output: 0.78333
Explanation: You can assign the two extra students to the first class. The average pass ratio will be equal to (3/4 + 3/5 + 2/2) / 3 = 0.78333.
Example 2:

Input: classes = [[2,4],[3,9],[4,5],[2,10]], extraStudents = 4
Output: 0.53485
 

Constraints:

1 <= classes.length <= 105
classes[i].length == 2
1 <= passi <= totali <= 105
1 <= extraStudents <= 105
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
    def leetcode(self, classes: List[List[int]], extraStudents: int) -> float:
        # Create a max heap based on the gain in pass ratio
        heap = []
        for passi, totali in classes:
            current_ratio = passi / totali
            gain = ((passi + 1) / (totali + 1)) - current_ratio
            heapq.heappush(heap, (-gain, passi, totali))
        
        # Assign extra students
        for _ in range(extraStudents):
            # Pop the class with the max gain
            gain, passi, totali = heapq.heappop(heap)
            # Add one extra student
            passi += 1
            totali += 1
            # Calculate the new gain and push it back
            new_gain = ((passi + 1) / (totali + 1)) - (passi / totali)
            heapq.heappush(heap, (-new_gain, passi, totali))
        
        # Calculate the final average pass ratio
        total_ratio = 0
        while heap:
            _, passi, totali = heapq.heappop(heap)
            total_ratio += passi / totali
        
        return total_ratio / len(classes)

        ### 3, time limit exceeded
        ll = len(classes)
        classes.sort(reverse=True, key=lambda x:((x[0]+1)/(x[1]+1)-x[0]/x[1]))
        for ii in range(extraStudents):
            #print(classes)
            classes[0][0] += 1
            classes[0][1] += 1

            ### reorder the updated list, by moving down the index-0
            index = 0
            while index < ll-1:
                ix,iy = classes[index]
                ix1,iy1 = classes[index+1]
                if (ix+1)/(iy+1)-ix/iy < (ix1+1)/(iy1+1)-ix1/iy1:
                    classes[index][0], classes[index+1][0] = classes[index+1][0], classes[index][0]
                    classes[index][1], classes[index+1][1] = classes[index+1][1], classes[index][1]
                    index += 1
                else:
                    break
        
        result = 0
        for ii in range(ll):
            result += classes[ii][0] / classes[ii][1]

        return result/ll

        ### 2 wrong, just a try
        ll = len(classes)
        result = 0
        diff = 0
        for ii in range(ll):
            a, b = classes[ii]
            result += a / b
            diff = max(diff, (((a+extraStudents)*b - a*(b+extraStudents))/(b*(b+extraStudents))))
            print(result,diff, classes)

        return (result+diff) / ll

        ### 1 wrong answer, sort key incorrect
        ll = len(classes)
        classes.sort(key=lambda x:(x[0]/x[1]))
        for ii in range(extraStudents):
            print(classes)
            classes[0][0] += 1
            classes[0][1] += 1

            ### reorder the updated list, by moving down the index-0
            index = 0
            while index < ll:
                if classes[index][0]*classes[index+1][1] > classes[index+1][0]*classes[index][1]:
                    classes[index][0], classes[index+1][0] = classes[index+1][0], classes[index][0]
                    classes[index][1], classes[index+1][1] = classes[index+1][1], classes[index][1]
                    index += 1
                else:
                    break
        
        result = 0
        for ii in range(ll):
            result += classes[ii][0] / classes[ii][1]

        return result/ll


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
