# 380. Insert Delete GetRandom O(1)

[Original Page](https://leetcode.com/problems/insert-delete-getrandom-o1/)

Design a data structure that supports all following operations in **O(1)** time.

1.  `insert(val)`: Inserts an item val to the set if not already present.
2.  `remove(val)`: Removes an item val from the set if present.
3.  `getRandom`: Returns a random element from current set of elements. Each element must have the **same probability** of being returned.

**Example:**

<pre>// Init an empty set.
RandomizedSet randomSet = new RandomizedSet();

// Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomSet.insert(1);

// Returns false as 2 does not exist in the set.
randomSet.remove(2);

// Inserts 2 to the set, returns true. Set now contains [1,2].
randomSet.insert(2);

// getRandom should return either 1 or 2 randomly.
randomSet.getRandom();

// Removes 1 from the set, returns true. Set now contains [2].
randomSet.remove(1);

// 2 was already in the set, so return false.
randomSet.insert(2);

// Since 1 is the only number in the set, getRandom always return 1.
randomSet.getRandom();
</pre>

<div>

[Subscribe](/subscribe/) to see which companies asked this question

</div>

<div>

<div id="tags" class="btn btn-xs btn-warning">Show Tags</div>

<span class="hidebutton" style="display: none;">[Array](/tag/array/) [Hash Table](/tag/hash-table/) [Design](/tag/design/)</span></div>