"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        ans = []
        
        if not root:
            return ans

        def dfs(node):
            for x in node.children:
                dfs(x)

            ans.append(node.val)

        dfs(root)

        return ans

        
