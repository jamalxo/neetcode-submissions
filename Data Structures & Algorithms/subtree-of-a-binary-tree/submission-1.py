# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        self.res = False

        def dfs(node1, sub):
            if not node1:
                return
            if sameTree(node1, sub):
                self.res = True
            dfs(node1.left, sub)
            dfs(node1.right, sub)
        
        
        def sameTree(node1, node2):
            if not node1 and not node2:
                return True
            if not node1 or not node2:
                return False
            if node1.val != node2.val:
                return False

            left = sameTree(node1.left, node2.left)
            right = sameTree(node1.right, node2.right)

            return left and right

        dfs(root, subRoot)
        return self.res