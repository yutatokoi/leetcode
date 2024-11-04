# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        modes = []
        maxCount = 0
        curr = None
        currCount = 0
        
        def traverse(node):
            if not node:
                return
            
            traverse(node.left)

            nonlocal modes, maxCount, curr, currCount
            if node.val == curr:
                currCount += 1
            else:
                curr = node.val
                currCount = 1

            if currCount > maxCount:
                modes = [curr]
                maxCount = currCount
            elif currCount == maxCount:
                modes.append(node.val)
            
            traverse(node.right)

        traverse(root)

        return modes
