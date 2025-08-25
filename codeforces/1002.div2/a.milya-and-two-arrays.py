"""
A. Milya and Two Arrays
time limit per test1 second
memory limit per test256 megabytes
An array is called good if for any element x
 that appears in this array, it holds that x
 appears at least twice in this array. For example, the arrays [1,2,1,1,2]
, [3,3]
, and [1,2,4,1,2,4]
 are good, while the arrays [1]
, [1,2,1]
, and [2,3,4,4]
 are not good.

Milya has two good arrays a
 and b
 of length n
. She can rearrange the elements in array a
 in any way. After that, she obtains an array c
 of length n
, where ci=ai+bi
 (1≤i≤n
).

Determine whether Milya can rearrange the elements in array a
 such that there are at least 3
 distinct elements in array c
.

Input
Each test consists of multiple test cases. The first line contains a single integer t
 (1≤t≤1000
) — the number of test cases. The description of the test cases follows.

The first line of each test case contains a single integer n
 (3≤n≤50
) — the length of the arrays a
 and b
.

The second line of each test case contains n
 integers a1,a2,…,an
 (1≤ai≤109
) — the elements of the array a
.

The third line of each test case contains n
 integers b1,b2,…,bn
 (1≤bi≤109
) — the elements of the array b
.

Output
For each test case, output «
YES»
 (without quotes) if it is possible to obtain at least 3
 distinct elements in array c
, and «
NO»
 otherwise.

You can output each letter in any case (for example, «
YES»
, «
Yes»
, «
yes»
, «
yEs»
 will be recognized as a positive answer).

Example
InputCopy
5
4
1 2 1 2
1 2 1 2
6
1 2 3 3 2 1
1 1 1 1 1 1
3
1 1 1
1 1 1
6
1 52 52 3 1 3
59 4 3 59 3 4
4
100 1 100 1
2 2 2 2
OutputCopy
YES
YES
NO
YES
NO
Note
In the first test case, you can swap the second and third elements. Then the array a=[1,1,2,2]
, b=[1,2,1,2]
, and then c=[2,3,3,4]
.

In the second test case, you can leave the elements unchanged. Then c=[2,3,4,4,3,2]
.

In the third test case, the array a
 will not change from rearranging the elements in it. Then c=[2,2,2]
, so the answer is «
NO»
.
"""

from collections import defaultdict
 
def codeforces(n: int, a: [], b: []):
    dda = defaultdict(int)
    ddb = defaultdict(int)
    for each in a:
        dda[each] += 1
    for each in b:
        ddb[each] += 1
    if len(list(dda.keys()))*len(list(ddb.keys())) <= 2:
        return "no"
        
    return "yes"
 
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        print(codeforces(n, a, b))