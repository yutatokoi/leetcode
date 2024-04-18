# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good_nodes = [root]

        node = root
        max_in_path = node.val

        while node:
            if node.left:
                if node.left.val >= max_in_path:
                    good_nodes.append(node.left)
                    max_in_path = max(max_in_path, node.left.val)
                    
            if node.right:

        return len(good_nodes)


