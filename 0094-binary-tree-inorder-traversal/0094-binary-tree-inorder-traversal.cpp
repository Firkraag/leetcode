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
    void inorderTraversalAux(TreeNode *root, vector<int> &ans) {
        if (root == nullptr) {
            return;
        }
        inorderTraversalAux(root->left, ans);
        ans.push_back(root->val);
        inorderTraversalAux(root->right, ans);
    }
public:
    vector<int> inorderTraversal(TreeNode* root) {
        stack<TreeNode *> nodeStack;
        vector<int> ans;
        for (TreeNode *node = root;node;node = node->left) {
            nodeStack.push(node);
        }
        while (!nodeStack.empty()) {
            auto *node = nodeStack.top();
            nodeStack.pop();
            ans.push_back(node->val);
            for (node = node->right;node;node = node->left) {
                nodeStack.push(node);
            }
        }
        return ans;
    }
};