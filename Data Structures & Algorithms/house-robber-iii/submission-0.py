# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        memo = {}
        def dfs(node, robbing):
        
            #print(total)
            if not node:
                return 0

            if (node, robbing) in memo:
                return memo[(node, robbing)]

            # skip this node: the children are free to be robbed or not
            skip = dfs(node.left, False) + dfs(node.right, False)
            res = 0
            take = 0
            if robbing:
                res = skip
            else:
                take = node.val + dfs(node.left, True) + dfs(node.right, True)
                res = max(skip, take)

            memo[(node, robbing)] = res
            return res
        
        return dfs(root, False)

