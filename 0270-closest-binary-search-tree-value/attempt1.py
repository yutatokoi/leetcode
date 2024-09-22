# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        closest = float("infinity")

        while root:
            if root.val == target:
                return root.val
            if abs(root.val - target) < abs(closest - target):
                closest = root.val
            if abs(root.val - target) == abs(closest - target):
                closest = min(closest, root.val)

            if root.val > target:
                root = root.left
            else:
                root = root.right

        return closest


