"""
661. Image Smoother
Easy
Topics
Companies
An image smoother is a filter of the size 3 x 3 that can be applied to each cell of an image by rounding down the average of the cell and the eight surrounding cells (i.e., the average of the nine cells in the blue smoother). If one or more of the surrounding cells of a cell is not present, we do not consider it in the average (i.e., the average of the four cells in the red smoother).


Given an m x n integer matrix img representing the grayscale of an image, return the image after applying the smoother on each cell of it.



Example 1:


Input: img = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[0,0,0],[0,0,0],[0,0,0]]
Explanation:
For the points (0,0), (0,2), (2,0), (2,2): floor(3/4) = floor(0.75) = 0
For the points (0,1), (1,0), (1,2), (2,1): floor(5/6) = floor(0.83333333) = 0
For the point (1,1): floor(8/9) = floor(0.88888889) = 0
Example 2:


Input: img = [[100,200,100],[200,50,200],[100,200,100]]
Output: [[137,141,137],[141,138,141],[137,141,137]]
Explanation:
For the points (0,0), (0,2), (2,0), (2,2): floor((100+200+200+50)/4) = floor(137.5) = 137
For the points (0,1), (1,0), (1,2), (2,1): floor((200+200+50+200+100+100)/6) = floor(141.666667) = 141
For the point (1,1): floor((50+200+200+200+200+100+100+100+100)/9) = floor(138.888889) = 138


Constraints:

m == img.length
n == img[i].length
1 <= m, n <= 200
0 <= img[i][j] <= 255
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
    def leetcode(self, img: List[List[int]]) -> List[List[int]]:
        m = len(img)
        if m == 0:
            return []
        n = len(img[0])
        result = [[0 for _ in range(n)] for _ in range(m)]
        for ii in range(m):
            for jj in range(n):
                count = 1
                total = img[ii][jj]
                if ii > 0:
                    if jj > 0:
                        total += img[ii-1][jj-1]
                        count += 1

                    total += img[ii-1][jj]
                    count += 1

                    if jj < n-1:
                        total += img[ii-1][jj+1]
                        count += 1
                if ii < m-1:
                    if jj > 0:
                        total += img[ii+1][jj-1]
                        count += 1

                    total += img[ii+1][jj]
                    count += 1

                    if jj < n-1:
                        total += img[ii+1][jj+1]
                        count += 1

                if jj > 0:
                    total += img[ii][jj-1]
                    count += 1

                if jj < n-1:
                    total += img[ii][jj+1]
                    count += 1


                result[ii][jj] = total//count

        return result


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
