# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        result = []
        node_queue = deque([root])
        while node_queue:
            n = len(node_queue)
            level = []
            for _ in range(n):
                node = node_queue.popleft()
                level.append(node.val)
                if node.left is not None:
                    node_queue.append(node.left)
                if node.right is not None:
                    node_queue.append(node.right)
            result.append(level)
        return result

        