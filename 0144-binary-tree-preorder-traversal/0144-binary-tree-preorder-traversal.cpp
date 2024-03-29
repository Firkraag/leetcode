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
    void preorderTraversalAux(TreeNode *root, vector<int> &ans) {
        if (!root) return;
        ans.push_back(root->val);
        preorderTraversalAux(root->left, ans);
        preorderTraversalAux(root->right, ans);
    }
public:
    vector<int> preorderTraversal(TreeNode* root) {
        vector<int> ans;
        stack<TreeNode *> nodeStack;
        for (auto *node = root; node; node = node->left) {
            nodeStack.push(node);
            ans.push_back(node->val);
        }
        while (!nodeStack.empty()) {
            auto *node = nodeStack.top();
            nodeStack.pop();
            for(node = node->right;node;node = node->left) {
                nodeStack.push(node);
                ans.push_back(node->val);
            }
        }
        return ans;  
    }
};