A - Railway Company / 
Time Limit: 3 sec / Memory Limit: 1024 MB

Story
Nihonbashi Simulator is a turn-based simulation game where you manage railway company X in the fictional country R. As a big fan of this game, your goal is to make the company highly profitable. By appropriately constructing rails and stations, you will assist the people living in country R in their commuting while developing X into the best railway company!

Problem Statement
Country R is composed of sections arranged in an 
N×N grid. The section in the 
i-th row from the top 
(0≤i<N), and the 
j-th column from the left 
(0≤j<N) is denoted as 
(i,j). Each section can be either empty, rail, or station:

Empty
Does not connect to other sections.
Can be changed to a station or rail by paying a cost.
Rail
Connects to a maximum of two adjacent non-empty sections on the up, down, left, and right. Rails are of six types, numbered as shown in the diagram below, depending on their connections.
Can be changed to a station by paying a cost.
Station
Connects to a maximum of four adjacent non-empty sections on the up, down, left, and right.

1
2
3
4
5
6
Types of rails
There are 
M people living in country R. The home of person 
c is located at section 
(i 
c,s
​
 ,j 
c,s
​
 ), and workplace is at section 
(i 
c,t
​
 ,j 
c,t
​
 ), between which he/she commutes.

At the start of the game, railway company X has money of 
K, and all sections are empty. The game will proceed for 
T turns.

How the game progresses
Each turn consists of a construction phase followed by a collection phase.

Construction phase
During the construction phase, one of the following actions is performed: placing a rail, placing a station, or waiting. Actions that would result in money going below zero are not allowed. The check for whether money is below zero is performed before the collection phase.

Placing a rail: Select one empty section and change it to one of the six types of rails. Money decreases by 100.
Placing a station: Select one empty or rail section and change it to a station. Money decreases by 5000.
Waiting: The state of the sections and the money do not change.
Collection phase
The people living in country R commute simultaneously. Person 
c will use train and pay a fare to railway company X only if there exist sections 
(i 
p
​
 ,j 
p
​
 ) and 
(i 
q
​
 ,j 
q
​
 ) that satisfy the following conditions:


Sections 
(i 
p
​
 ,j 
p
​
 ),(i 
q
​
 ,j 
q
​
 ) are stations.
It is possible to reach section 
(i 
q
​
 ,j 
q
​
 ) from section 
(i 
p
​
 ,j 
p
​
 ) via zero or more connected station or rail sections.
∣i 
c,s
​
 −i 
p
​
 ∣+∣j 
c,s
​
 −j 
p
​
 ∣≤2
∣i 
c,t
​
 −i 
q
​
 ∣+∣j 
c,t
​
 −j 
q
​
 ∣≤2
When person 
c uses the train, railway company X's money increases by 
∣i 
c,s
​
 −i 
c,t
​
 ∣+∣j 
c,s
​
 −j 
c,t
​
 ∣.


Please determine the actions to maximize the money at the end of turn 
T.

Scoring
For each test case, the absolute score is obtained as the value of the money at the end of 
T turns, and we compute the relative score 
round(10 
9
 × 
MAX
YOUR
​
 ), where YOUR is your absolute score and MAX is the maximum absolute score among all competitors obtained on that test case. The score of the submission is the sum of the relative scores. In test cases where MAX is 
0, the relative score for all participants who received  will be 
10 
9
 .

If the following invalid outputs are produced, it will be judged as 。

Placing a rail into a station or rail section
Placing a station into a station section
An action that results in money being less than 0
Invalid action with incorrect rail types or section position
The number of actions output is not 
T
The final ranking will be determined by the system test with more inputs which will be run after the contest is over. In both the provisional/system test, if your submission produces illegal output or exceeds the time limit for some test cases, only the score for those test cases will be zero, and your submission will be excluded from the MAX calculation for those test cases.

The system test will be performed only for the last submission which received a result other than  . Be careful not to make a mistake in the final submission.

Number of test cases
Provisional test: 50
System test: 2000
We will publish seeds.txt (sha256=ed5b3f922dc3633bade3f70cc6f1dd1bb3087dba36ce26ce9d4888ce2ec7a247) after the contest is over.
About Relative Evaluation System
In both the provisional/system test, the standings will be calculated using only the last submission which received a result other than . Only the last submissions are used to calculate the MAX for each test case when calculating the relative scores.

The scores shown in the standings are relative, and whenever a new submission arrives, all relative scores are recalculated. On the other hand, the score for each submission shown on the submissions page is the sum of the absolute score for each test case, and the relative scores are not shown. In order to know the relative score of submission other than the latest one in the current standings, you need to resubmit it. If your submission produces illegal output or exceeds the time limit for some test cases, the score shown on the submissions page will be 0, but the standings show the sum of the relative scores for the test cases that were answered correctly.

About execution time
Execution time may vary slightly from run to run. In addition, since system tests simultaneously perform a large number of executions, it has been observed that execution time increases by several percent compared to provisional tests. For these reasons, submissions that are very close to the time limit may result in  in the system test. Please measure the execution time in your program to terminate the process, or make sure to have enough time margin for the execution.

Input
Input will be provided from Standard Input in the following format.

N M K T
i 
0,s
​
  j 
0,s
​
  i 
0,t
​
  j 
0,t
​
 
i 
1,s
​
  j 
1,s
​
  i 
1,t
​
  j 
1,t
​
 
⋮
i 
M−1,s
​
  j 
M−1,s
​
  i 
M−1,t
​
  j 
M−1,t
​
 
On the first line, there are four integers 
N,M,K,T separated by spaces.
N represents the number of rows and columns in country R and satisfies 
N=50.
M represents the number of people in country R and satisfies 
50≤M≤1600.
K represents the initial money of railway company X and satisfies 
11000≤K≤20000.
T represents the number of turns in the game and satisfies 
T=800.
The following 
M lines provide information about the commuting of people living in country R. Each line contains four space-separated integers, where the home of person 
c is at section 
(i 
c,s
​
 ,j 
c,s
​
 ) and the workplace is at section 
(i 
c,t
​
 ,j 
c,t
​
 ). The following conditions are satisfied: 
0≤i 
c,s
​
 ,i 
c,t
​
 <N,0≤j 
c,s
​
 ,j 
c,t
​
 <N,∣i 
c,s
​
 −i 
c,t
​
 ∣+∣j 
c,s
​
 −j 
c,t
​
 ∣>4(0≤c<M).
Output
Output 
T lines. For the 
t-th row, output the action taken during the 
t-th construction phase in the following format:

When placing a rail
If you are constructing a rail of type 
p at section 
(i,j), output 
p,i,j separated by spaces.
The types of rails are numbered according to the diagram provided in the problem statement.
When placing a station
If you are constructing a station at section 
(i,j), output 
0,i,j separated by spaces.
When waiting
Output -1.
show example

Input Generation
Details
Tools (Input generator and visualizer)
Web version: This is more powerful than the local version providing animations.
Local version: You need a compilation environment of Rust language.
Pre-compiled binary for Windows: If you are not familiar with the Rust language environment, please use this instead.
Please be aware that sharing visualization results or discussing solutions/ideas during the contest is prohibited.

Your program may output comment lines starting with #. The web version of the visualizer displays the comment lines with the corresponding output, which may be useful for debugging and analysis. Since the judge program ignores all comment lines, you can submit a program that outputs comment lines as is.

Sample Solution
Sample implementation in Python
The following processes are implemented:

Examine person 
0, 
1, 
… in order to find the first person for whom it is possible to place stations at their home and workplace locations and connect them with rails at the initial money.
Place stations at the identified person's home and workplace locations, and place rails to connect from home to workplace.
After that, wait until turn 
T.
The code includes a simulation of the changes in money. You may use it as a reference when creating your solution.