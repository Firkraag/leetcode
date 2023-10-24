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
    int isBalancedAux(TreeNode *root) {
        if (!root) return 0;
        int leftDepth = isBalancedAux(root->left);
        int rightDepth = isBalancedAux(root->right);
        if (leftDepth == -1 || rightDepth == -1) {
            return -1; // a depth of -1 means the subtee is not height-balanced
        }
        if (abs(leftDepth - rightDepth) > 1) {
            return -1;
        }
        return max(leftDepth, rightDepth) + 1;
    }
public:
    bool isBalanced(TreeNode* root) {
        return isBalancedAux(root) != -1;
    }
};