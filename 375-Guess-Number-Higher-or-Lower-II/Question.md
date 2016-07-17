# 375. Guess Number Higher or Lower II

[Original Page](https://leetcode.com/problems/guess-number-higher-or-lower-ii/)

We are playing the Guess Game. The game is as follows:

I pick a number from **1** to **n**. You have to guess which number I picked.

Every time you guess wrong, I'll tell you whether the number I picked is higher or lower.

However, when you guess a particular number x, and you guess wrong, you pay **$x**. You win the game when you guess the number I picked.

**Example:**

<pre>n = 10, I pick 8.

First round:  You guess 5, I tell you that it's higher. You pay $5.
Second round: You guess 7, I tell you that it's higher. You pay $7.
Third round:  You guess 9, I tell you that it's lower. You pay $9.

Game over. 8 is the number I picked.

You end up paying $5 + $7 + $9 = $21.
</pre>

Given a particular **n ≥ 1**, find out how much money you need to have to guarantee a **win**.

**Hint:**

[Show Hint](#)

1.  The best strategy to play the game is to minimize the maximum loss you could possibly face. Another strategy is to minimize the expected loss. Here, we are interested in the **first** scenario.[Show More Hint](#)
2.  Take a small example (n = 3). What do you end up paying in the worst case?[Show More Hint](#)
3.  Check out [this article](https://en.wikipedia.org/wiki/Minimax) if you're still stuck.[Show More Hint](#)
4.  The purely recursive implementation of minimax would be worthless for even a small n. You MUST use dynamic programming. [Show More Hint](#)
5.  As a follow-up, how would you modify your code to solve the problem of minimizing the expected loss, instead of the worst-case loss?

**Credits:**  
Special thanks to [@agave](https://leetcode.com/agave/) and [@StefanPochmann](https://leetcode.com/stefanpochmann/) for adding this problem and creating all test cases.

<div>

[Subscribe](/subscribe/) to see which companies asked this question

</div>

<div>

<div id="company_tags" class="btn btn-xs btn-warning">Show Company Tags</div>

<span class="hidebutton">[Google](/company/google/)</span></div>

<div>

<div id="tags" class="btn btn-xs btn-warning">Show Tags</div>

<span class="hidebutton">[Dynamic Programming](/tag/dynamic-programming/)</span></div>

<div>

<div id="similar" class="btn btn-xs btn-warning">Show Similar Problems</div>

<span class="hidebutton">[(M) Flip Game II](/problems/flip-game-ii/) [(E) Guess Number Higher or Lower](/problems/guess-number-higher-or-lower/)</span></div>