/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* left;
    Node* right;
    Node* next;

    Node() : val(0), left(NULL), right(NULL), next(NULL) {}

    Node(int _val) : val(_val), left(NULL), right(NULL), next(NULL) {}

    Node(int _val, Node* _left, Node* _right, Node* _next)
        : val(_val), left(_left), right(_right), next(_next) {}
};
*/

class Solution {
public:
    Node* connect(Node* root) {
        if (!root) return nullptr;
        queue<Node *> nodeQueue;
        nodeQueue.push(root);
        while (!nodeQueue.empty()) {
            int levelSize = nodeQueue.size();
            Node *prev = nullptr;
            for (int i = 0; i < levelSize;i++) {
                Node *node = nodeQueue.front();
                nodeQueue.pop();
                if (node->left) {
                    nodeQueue.push(node->left);
                }
                if (node->right) {
                    nodeQueue.push(node->right);
                }
                if (prev) {
                    prev->next = node;
                }
                prev = node;
            }
        }
        return root;
    }
};