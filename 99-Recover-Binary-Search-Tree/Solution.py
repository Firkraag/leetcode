# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if root == None:
            return
        nodeList = []
        self.traverse(root, nodeList)
        sortedNodeList = sorted(nodeList, key = lambda node: node.val)
        #print [node.val for node in nodeList], [node.val for node in sortedNodeList]
        for i in range(len(nodeList)):
            if nodeList[i] != sortedNodeList[i]:
                node1 = nodeList[i]
                node2 = sortedNodeList[i]
                #print node1.val, node2.val
                node1.val, node2.val = node2.val, node1.val
                #print node1.val, node2.val
                return
      
    def traverse(self, root, nodeList):
        if root.left != None:
            self.traverse(root.left, nodeList)
        nodeList.append(root)
        if root.right != None:
            self.traverse(root.right, nodeList)
              