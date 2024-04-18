# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:        
        
        def dfs(node, max_in_path):
            if not node:
                return 0
            
            if node.val >= max_in_path:
                res = 1
            else:
                res = 0

            max_in_path = max(node.val, max_in_path)

            res += dfs(node.left, max_in_path)
            res += dfs(node.right, max_in_path)

            return res

        return dfs(root, root.val)

