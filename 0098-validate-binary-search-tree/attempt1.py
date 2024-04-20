# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        l = root.left
        r = root.right

        if not l and not r:
            return True
        elif l and not r:
            if l.val >= root.val:
                return False
            else:
                return True
        elif not l and r:
            if r.val <= root.val:
                return False
            else:
                return True
        elif l and r:
            if l.val < root.val and r.val > root.val:
                return True
            else:
                return False
        else:
            return self.isValidBST(l) and self.isValidBST(r)
        

