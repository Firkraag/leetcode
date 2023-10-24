/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
    TreeNode* sortedArrayTOBSTAux(vector<int>& nums, int begin, int end) {
        if (begin == end) {
            return new TreeNode(nums[begin]);
        }
        if (begin > end) {
            return nullptr;
        }
        int mid = (begin + end) / 2;
        return new TreeNode(nums[mid], sortedArrayTOBSTAux(nums, begin, mid - 1), sortedArrayTOBSTAux(nums, mid + 1, end));
    }
public:
    TreeNode* sortedArrayToBST(vector<int>& nums) {
        return sortedArrayTOBSTAux(nums, 0, nums.size() - 1);
    }
};