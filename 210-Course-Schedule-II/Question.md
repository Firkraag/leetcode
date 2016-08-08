# 210. Course Schedule II

[Original Page](https://leetcode.com/problems/course-schedule-ii/)

There are a total of _n_ courses you have to take, labeled from `0` to `n - 1`.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: `[0,1]`

Given the total number of courses and a list of prerequisite **pairs**, return the ordering of courses you should take to finish all courses.

There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.

For example:

<pre>2, [[1,0]]</pre>

There are a total of 2 courses to take. To take course 1 you should have finished course 0\. So the correct course order is `[0,1]`

<pre>4, [[1,0],[2,0],[3,1],[3,2]]</pre>

There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2\. Both courses 1 and 2 should be taken after you finished course 0\. So one correct course order is `[0,1,2,3]`. Another correct ordering is`[0,2,1,3]`.

**Note:**  
The input prerequisites is a graph represented by **a list of edges**, not adjacency matrices. Read more about [how a graph is represented](https://www.khanacademy.org/computing/computer-science/algorithms/graph-representation/a/representing-graphs).

[click to show more hints.](#)

<div class="spoilers" style="display: none;">**Hints:**

1.  This problem is equivalent to finding the topological order in a directed graph. If a cycle exists, no topological ordering exists and therefore it will be impossible to take all courses.
2.  [Topological Sort via DFS](https://class.coursera.org/algo-003/lecture/52) - A great video tutorial (21 minutes) on Coursera explaining the basic concepts of Topological Sort.
3.  Topological sort could also be done via [BFS](http://en.wikipedia.org/wiki/Topological_sorting#Algorithms).

</div>

<div>

[Subscribe](/subscribe/) to see which companies asked this question

</div>

<div>

<div id="company_tags" class="btn btn-xs btn-warning">Show Company Tags</div>

<span class="hidebutton">[Facebook](/company/facebook/) [Zenefits](/company/zenefits/)</span></div>

<div>

<div id="tags" class="btn btn-xs btn-warning">Show Tags</div>

<span class="hidebutton">[Depth-first Search](/tag/depth-first-search/) [Breadth-first Search](/tag/breadth-first-search/) [Graph](/tag/graph/) [Topological Sort](/tag/topological-sort/)</span></div>

<div>

<div id="similar" class="btn btn-xs btn-warning">Show Similar Problems</div>

<span class="hidebutton">[(M) Course Schedule](/problems/course-schedule/) [(H) Alien Dictionary](/problems/alien-dictionary/) [(M) Minimum Height Trees](/problems/minimum-height-trees/)</span></div>