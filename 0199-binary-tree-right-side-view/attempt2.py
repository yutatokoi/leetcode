# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        node = root

        while node:
            result.append(node.val)
            if not node.right:
                node = node.left
            else:
                node = node.right

        return result

