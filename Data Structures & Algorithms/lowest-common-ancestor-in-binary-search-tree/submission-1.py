# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # current value is bigger and samller at the same time?
        self.res = None
        def dfs(node):
            if not node:
                return

            if (node.val >= p.val and node.val <= q.val) or (node.val >= q.val and node.val <= p.val):
                self.res = node
                return
            
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)

        return self.res