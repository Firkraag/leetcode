# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        return self.sumRootToLeafAux(root, 0)
    
    def sumRootToLeafAux(self, node, val):
        if node.left is None and node.right is None:
            return val * 2 + node.val
        elif node.left is None and node.right is not None:
            return self.sumRootToLeafAux(node.right, val * 2 + node.val)
        elif node.left is not None and node.right is None:
            return self.sumRootToLeafAux(node.left, val * 2 + node.val)
        else:
            return self.sumRootToLeafAux(node.left, val * 2 + node.val) + self.sumRootToLeafAux(node.right, val * 2 + node.val)