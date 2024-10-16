/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func sumOfLeftLeaves(root *TreeNode) int {
    if root == nil {
        return 0
    }

    stack := []*TreeNode{root}
    total := 0
    for len(stack) > 0 {
        node := stack[len(stack) - 1]
        stack = stack[:len(stack) - 1]

        if node.Left != nil && node.Left.Left == nil && node.Left.Right == nil {
            total += node.Left.Val
        }

        if node.Left != nil {
            stack = append(stack, node.Left)
        }

        if node.Right != nil {
            stack = append(stack, node.Right)
        }
    }

    return total
}
