# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        res = 0

        if root:
            res = 1

            if root.left:
                l = self.maxDepth(root.left) + res
            else:
                l = res

            if root.right:
                r = self.maxDepth(root.right) + res
            else:
                r = res

            res = max(l, r)
        else:
            res = 0

        return res

