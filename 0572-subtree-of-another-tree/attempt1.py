# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root.val != subRoot.val:
            if root.left:
                self.isSubtree(root.left, subRoot)
            if root.right:
                self.isSubtree(root.right, subRoot)
        
        return self.isSameTree(root.val, subRoot)

        return False

    def isSameTree(self, p, q):
        if not p and not q:
            return True
        if not p and q:
            return False
        if p and not q:
            return False
        if p and q:
            if p != q:
                return False
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        
