# 330. Patching Array

[Original Page](https://leetcode.com/problems/patching-array/)

Given a sorted positive integer array _nums_ and an integer _n_, add/patch elements to the array such that any number in range `[1, n]` inclusive can be formed by the sum of some elements in the array. Return the minimum number of patches required.

**Example 1:**  
_nums_ = `[1, 3]`, _n_ = `6`  
Return `1`.

Combinations of _nums_ are `[1], [3], [1,3]`, which form possible sums of: `1, 3, 4`.  
Now if we add/patch `2` to _nums_, the combinations are: `[1], [2], [3], [1,3], [2,3], [1,2,3]`.  
Possible sums are `1, 2, 3, 4, 5, 6`, which now covers the range `[1, 6]`.  
So we only need `1` patch.

**Example 2:**  
_nums_ = `[1, 5, 10]`, _n_ = `20`  
Return `2`.  
The two patches can be `[2, 4]`.

**Example 3:**  
_nums_ = `[1, 2, 2]`, _n_ = `5`  
Return `0`.  

**Credits:**  
Special thanks to [@dietpepsi](https://leetcode.com/discuss/user/dietpepsi) for adding this problem and creating all test cases.

<div>

[Subscribe](/subscribe/) to see which companies asked this question

</div>

<div>

<div id="company_tags" class="btn btn-xs btn-warning">Hide Company Tags</div>

<span class="hidebutton" style="display: inline;">[Google](/company/google/)</span></div>

<div>

<div id="tags" class="btn btn-xs btn-warning">Hide Tags</div>

<span class="hidebutton" style="display: inline;">[Greedy](/tag/greedy/)</span></div>