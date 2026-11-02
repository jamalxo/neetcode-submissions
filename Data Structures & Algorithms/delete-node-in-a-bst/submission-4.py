# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def dfs(node):
            if not node:
                return None

            if node.val == key:
                if node.left:
                    cur = node.left
                    while cur.right: cur = cur.right
                    cur.right = node.right
                    return node.left
                elif node.right:
                    #print(node.right.val)
                    node.right.left = node.left
                    return node.right
                else:
                    return None

            if key < node.val:
                node.left = dfs(node.left)
            if key > node.val:
                node.right = dfs(node.right)
            #print(node.left)
            #print(node.right)
            return node

        return dfs(root)
        
        #return root