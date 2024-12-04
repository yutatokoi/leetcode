# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        stack = []
        minval = root.val
        secondmin = float("inf")
        node = root
        flag = False

        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            if minval < node.val < secondmin:
                secondmin = node.val
                flag = True
            node = node.right

        if flag:
            return secondmin

        return -1
