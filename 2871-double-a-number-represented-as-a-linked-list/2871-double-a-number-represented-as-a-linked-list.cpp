/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
    pair<ListNode *, int> doubleItAux(ListNode *node) {
        if (node->next) {
            auto [newNextNode, promote] = doubleItAux(node->next);
            int value = (node->val * 2 + promote) % 10;
            promote = (node->val * 2 + promote) / 10;
            return {new ListNode(value, newNextNode), promote};
        }
        else {
            int value = (node->val * 2) % 10;
            int promote = (node->val * 2) / 10;
            return {new ListNode(value), promote};
        }
    }
public:
    ListNode* doubleIt(ListNode* head) {
        auto [newHead, promote] = doubleItAux(head);
        return promote == 1 ? new ListNode(1, newHead) : newHead;
    }
};