# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        levels = {}

        def dfs(i, node):
            if not node:
                return
            levels[i] = max(levels.get(i, 0), node.val)
            dfs(i+1, node.left)
            dfs(i+1, node.right)

        dfs(0, root)
        print(levels)
        return list(levels.values())