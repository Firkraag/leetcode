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
        if (root == nullptr) {
            return nullptr;
        }
        queue<Node *> nodeQueue;
        nodeQueue.push(root);
        for (int levelSize = 1; levelSize > 0;) {
            int newLevelSize = 0;
            Node *prev = nodeQueue.front();
            nodeQueue.pop();
            if (prev->left) {
                nodeQueue.push(prev->left);
                newLevelSize++;
            }
            if (prev->right) {
                nodeQueue.push(prev->right);
                newLevelSize++;
            }
            for (int i = 1; i < levelSize;i++) {
                Node *node = nodeQueue.front();
                nodeQueue.pop();
                if (node->left) {
                    nodeQueue.push(node->left);
                    newLevelSize++;
                }
                if (node->right) {
                    nodeQueue.push(node->right);
                    newLevelSize++;
                }
                prev->next = node;
                prev = node;
            }
            levelSize = newLevelSize;
        }
        return root;
    }
};