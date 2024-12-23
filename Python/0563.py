# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        total = 0

        def calculate(node):
            if not node:
                return 0

            leftSum = calculate(node.left) 
            rightSum = calculate(node.right)

            nonlocal total
            total += abs(leftSum - rightSum)

            return leftSum + rightSum + node.val

        calculate(root)
        return total
