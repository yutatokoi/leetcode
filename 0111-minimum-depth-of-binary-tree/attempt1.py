# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left_depth = self.minDepth(root.left)
        right_depth = self.minDepth(root.right)
        
        if not root.left and not root.right:
            return 1
        
        if not root.left:
            return 1 + right_depth

        if not root.right:
            return left_depth + 1

        return min(left_depth, right_depth) + 1
    
        
