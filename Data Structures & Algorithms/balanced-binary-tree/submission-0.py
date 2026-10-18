# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.res = True

        def dfs(node):
            if not node:
                return 0

            height_l = dfs(node.left)
            height_r = dfs(node.right)

            if abs(height_l - height_r) > 1:
                self.res = False
            
            return 1 + max(height_l, height_r)
        
        dfs(root)

        return self.res