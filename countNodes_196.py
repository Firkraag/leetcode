# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        global number, height
        height = -1
        node = root
        while node != None:
            height += 1
            node = node.left
        if height == -1:
            return 0
        elif height == 0:
            return 1
        else:
            number = 2 ** height - 1
            self.countNodesAux(root, 0)
            return number
        
    def countNodesAux(self, root, h):
        global height, number
        if root == None:
            return
        elif root.left == None:
            if h == height:
                number += 1
            return
        else:
            node = root.left
            nodeHeight = h + 1
            while node.right != None:
                nodeHeight += 1
                node = node.right
            if nodeHeight == height:
                number += 2 ** (height - h - 1)
                self.countNodesAux(root.right, h + 1)
            elif node.left != None:
                number += 2 ** (height - h - 1) - 1
            else:
                self.countNodesAux(root.left, h + 1)
        
