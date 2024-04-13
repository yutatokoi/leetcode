# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        while root:
            if self.treeHeight(root.left) > 1 + self.treeHeight(root.right):
                return False
            if self.treeHeight(root.right) > 1 + self.treeheight(root.left):
                return False

            self.isBalanced(root.left)
            self.isBalanced(root.right)

        return True
        
    def treeHeight(self, root):
        if not root:
            return 0
        
        height = 1
        while root:
            height = 1 + max(self.treeHeight(root.left), self.treeHeight(root.right))

        return height

