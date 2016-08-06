# 241. Different Ways to Add Parentheses

[Original Page](https://leetcode.com/problems/different-ways-to-add-parentheses/)

Given a string of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. The valid operators are `+`, `-` and `*`.

**Example 1**

Input: `"2-1-1"`.

<pre>((2-1)-1) = 0
(2-(1-1)) = 2</pre>

Output: `[0, 2]`

**Example 2**

Input: `"2*3-4*5"`

<pre>(2*(3-(4*5))) = -34
((2*3)-(4*5)) = -14
((2*(3-4))*5) = -10
(2*((3-4)*5)) = -10
(((2*3)-4)*5) = 10</pre>

Output: `[-34, -14, -10, -10, 10]`

**Credits:**  
Special thanks to [@mithmatt](https://leetcode.com/discuss/user/mithmatt) for adding this problem and creating all test cases.

<div>

[Subscribe](/subscribe/) to see which companies asked this question

</div>

<div>

<div id="company_tags" class="btn btn-xs btn-warning">Show Company Tags</div>

<span class="hidebutton">[Cryptic Studios](/company/cryptic-studios/)</span></div>

<div>

<div id="tags" class="btn btn-xs btn-warning">Show Tags</div>

<span class="hidebutton">[Divide and Conquer](/tag/divide-and-conquer/)</span></div>

<div>

<div id="similar" class="btn btn-xs btn-warning">Show Similar Problems</div>

<span class="hidebutton">[(M) Unique Binary Search Trees II](/problems/unique-binary-search-trees-ii/) [(H) Basic Calculator](/problems/basic-calculator/) [(H) Expression Add Operators](/problems/expression-add-operators/)</span></div>