# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        nodes = []

        def inorder(node):
            if not node:
                return

            inorder(node.left)
            nodes.append(node.val)
            inorder(node.right)

        inorder(root)
        ans = 1e6
        for i in range(1, len(nodes)):
            ans = min(ans, nodes[i] - nodes[i - 1])

        return ans
