# 68. Text Justification

[Original Page](https://leetcode.com/problems/text-justification/)

Given an array of words and a length _L_, format the text such that each line has exactly _L_ characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces `' '` when necessary so that each line has exactly _L_ characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left justified and no extra space is inserted between words.

For example,  
**words**: `["This", "is", "an", "example", "of", "text", "justification."]`  
**L**: `16`.

Return the formatted lines as:  

<pre>[
   "This    is    an",
   "example  of text",
   "justification.  "
]
</pre>

**Note:** Each word is guaranteed not to exceed _L_ in length.

[click to show corner cases.](#)

<div class="spoilers" style="display: none;">**Corner Cases:**

*   A line other than the last line might contain only one word. What should you do in this case?  
    In this case, that line should be left-justified.

</div>

<div>

[Subscribe](/subscribe/) to see which companies asked this question

</div>

<div>

<div id="company_tags" class="btn btn-xs btn-warning">Show Company Tags</div>

<span class="hidebutton">[Airbnb](/company/airbnb/) [LinkedIn](/company/linkedin/)</span></div>

<div>

<div id="tags" class="btn btn-xs btn-warning">Show Tags</div>

<span class="hidebutton">[String](/tag/string/)</span></div>