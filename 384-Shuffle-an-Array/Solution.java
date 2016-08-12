public class Solution {
    private int[] nums;
    public Solution(int[] nums) {
        this.nums = nums;
    }
    
    /** Resets the array to its original configuration and return it. */
    public int[] reset() {
        return nums;
    }
    
    /** Returns a random shuffling of the array. */
    public int[] shuffle() {
        int n = this.nums.length;
        int[] nums = new int[n];
        for (int i = 0; i < n; i++) {
            nums[i] = this.nums[i];
        }
        for (int i = 0; i < n; i++) {
            int j = randint(i, n);
            int tmp = nums[i];
            nums[i] = nums[j];
            nums[j] = tmp;
        }
        return nums;
    }
    /** return a random number k such that i <= k < j */
    private int randint(int i, int j) {
        return (int) (Math.random() * (j - i)) + i;
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(nums);
 * int[] param_1 = obj.reset();
 * int[] param_2 = obj.shuffle();
 */
 
