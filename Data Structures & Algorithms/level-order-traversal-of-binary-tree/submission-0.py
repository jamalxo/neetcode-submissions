# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        level = {}

        def dfs(i, node):
            if not node:
                return

            level.setdefault(i, []).append(node.val)

            dfs(i+1, node.left)
            dfs(i+1, node.right)
        
        dfs(0, root)

        return list(level.values())
