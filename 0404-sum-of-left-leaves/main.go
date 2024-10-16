// # attempt1 (iterative solution)
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

// #attempt2 (dfs solution)
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func sumOfLeftLeaves(root *TreeNode) int {
    sum := 0
    var dfs func(node *TreeNode)
    dfs = func(node *TreeNode) {
        if node == nil {
            return
        }

        if node.Left != nil && isLeaf(node.Left) {
            sum += node.Left.Val
        }
        dfs(node.Left)
        dfs(node.Right)
    }

    dfs(root)
    return sum
}

func isLeaf(node *TreeNode) bool {
    return node != nil && node.Left == nil && node.Right == nil
}
