#!/usr/bin/env python
# coding=utf-8
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root == None:
            return ""
        from collections import deque
        queue = deque([root])
        valList = [str(root.val)]
        while len(queue) != 0:
            node = queue.popleft()
            if node.left != None:
                valList.append(str(node.left.val))
                queue.append(node.left)
            else:
                valList.append(str(None))
            
            if node.right != None:
                valList.append(str(node.right.val))
                queue.append(node.right)
            else:
                valList.append(str(None))
        return ' '.join(valList)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if len(data) == 0:
            return None
        valList = data.split()
        n = len(valList)
        from collections import deque
        root = TreeNode(valList[0])
        queue = deque([root])
        i = 1
        while len(queue) != 0:
            node = queue.popleft()
            if valList[i] == 'None':
                node.left = None
            else:
                left = TreeNode(int(valList[i]))
                node.left = left
                queue.append(left)
            
            if valList[i + 1] == 'None':
                node.right = None
            else:
                right = TreeNode(int(valList[i + 1]))
                node.right = right
                queue.append(right)
            i += 2
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
