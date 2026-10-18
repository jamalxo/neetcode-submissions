# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0
        
        def dfs(biggest, node):
            if not node:
                return
            
            if node.val >= biggest:
                self.count += 1                
            biggest = max(node.val, biggest)
            
            dfs(biggest, node.left)
            dfs(biggest, node.right)
        
        dfs(root.val, root)
        
        return self.count
