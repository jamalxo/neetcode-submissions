
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        # in order traversal
        self.res = 0
        self.current = 0

        def dfs(node):
            
            if not node:
                return
            print(node.val, self.current)
            
            dfs(node.left)
            self.current += 1
            if self.current == k:
                self.res = node.val
            dfs(node.right)

        dfs(root)

        return self.res
