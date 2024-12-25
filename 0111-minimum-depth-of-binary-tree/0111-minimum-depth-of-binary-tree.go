/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func minDepth(root *TreeNode) int {
    if root == nil {
        return 0
    }
    var depth int
    if root.Left == nil && root.Right == nil {
        depth = 1
    } else if root.Left == nil && root.Right != nil {
        depth = 1 + minDepth(root.Right)
    } else if root.Left != nil && root.Right == nil {
        depth = 1 + minDepth(root.Left)
    } else {
        depth = 1 + min(minDepth(root.Left), minDepth(root.Right))
    }
    return depth
}