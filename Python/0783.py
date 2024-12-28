# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        answer = float("inf")
        prev_node = None

        def inorder_traversal(node):
            if not node:
                return

            inorder_traversal(node.left)

            nonlocal prev_node
            nonlocal answer
            if prev_node:
                answer = min(answer, node.val - prev_node.val)

            prev_node = node
            inorder_traversal(node.right)

        inorder_traversal(root)

        return answer
