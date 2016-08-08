# 207. Course Schedule

[Original Page](https://leetcode.com/problems/course-schedule/)

There are a total of _n_ courses you have to take, labeled from `0` to `n - 1`.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: `[0,1]`

Given the total number of courses and a list of prerequisite **pairs**, is it possible for you to finish all courses?

For example:

<pre>2, [[1,0]]</pre>

There are a total of 2 courses to take. To take course 1 you should have finished course 0\. So it is possible.

<pre>2, [[1,0],[0,1]]</pre>

There are a total of 2 courses to take. To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1\. So it is impossible.

**Note:**  
The input prerequisites is a graph represented by **a list of edges**, not adjacency matrices. Read more about [how a graph is represented](https://www.khanacademy.org/computing/computer-science/algorithms/graph-representation/a/representing-graphs).

[click to show more hints.](#)

<div class="spoilers" style="display: none;">**Hints:**

1.  This problem is equivalent to finding if a cycle exists in a directed graph. If a cycle exists, no topological ordering exists and therefore it will be impossible to take all courses.
2.  [Topological Sort via DFS](https://class.coursera.org/algo-003/lecture/52) - A great video tutorial (21 minutes) on Coursera explaining the basic concepts of Topological Sort.
3.  Topological sort could also be done via [BFS](http://en.wikipedia.org/wiki/Topological_sorting#Algorithms).

</div>

<div>

[Subscribe](/subscribe/) to see which companies asked this question

</div>

<div>

<div id="company_tags" class="btn btn-xs btn-warning">Show Company Tags</div>

<span class="hidebutton">[Apple](/company/apple/) [Yelp](/company/yelp/) [Zenefits](/company/zenefits/)</span></div>

<div>

<div id="tags" class="btn btn-xs btn-warning">Show Tags</div>

<span class="hidebutton">[Depth-first Search](/tag/depth-first-search/) [Breadth-first Search](/tag/breadth-first-search/) [Graph](/tag/graph/) [Topological Sort](/tag/topological-sort/)</span></div>

<div>

<div id="similar" class="btn btn-xs btn-warning">Show Similar Problems</div>

<span class="hidebutton">[(M) Course Schedule II](/problems/course-schedule-ii/) [(M) Graph Valid Tree](/problems/graph-valid-tree/) [(M) Minimum Height Trees](/problems/minimum-height-trees/)</span></div>