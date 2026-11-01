# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        self.res = True

        def dfs(i, node):
            if not node:
                return i

            i += 1

            left = dfs(i, node.left)
            right = dfs(i, node.right)

            if abs(left-right) > 1:
                self.res = False
                return False

            return max(left, right)

        
        dfs(0, root)
        
        return self.res