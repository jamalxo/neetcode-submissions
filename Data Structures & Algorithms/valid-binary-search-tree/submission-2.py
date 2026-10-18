# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import sys

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.res = True

        def dfs(allowed_range, node):
            if not node:
                return
            
            
            # the main problem is right bigger node and left lower, but we have to keep the roo in mind
            if node.val <= allowed_range[0] or allowed_range[1] <= node.val:
                self.res = False

            left = [allowed_range[0], node.val]
            right = [node.val, allowed_range[1]]

            dfs(left, node.left)
            dfs(right, node.right)

        
        dfs([-sys.maxsize-1, sys.maxsize], root)

        return self.res