# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def backtrack(l, r):
            if l > r:
                return None
            
            m = (l + r) // 2
            node = TreeNode(nums[m])
            node.left = backtrack(l, m - 1)
            node.right = backtrack(m + 1, r)
            return node

        return backtrack(0, len(nums) - 1)
            

        
