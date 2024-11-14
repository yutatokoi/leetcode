"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        stack = []
        if root:
            stack.append((1, root))

        depth = 0
        while stack:
            currDepth, root = stack.pop()
            if root:
                depth = max(depth, currDepth)
                for c in root.children:
                    stack.append((currDepth + 1, c))

        return depth
