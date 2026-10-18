# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
       # every value's position in inorder, worked out once
        position = {val: i for i, val in enumerate(inorder)}

        # which preorder value is the next root to create
        self.pre_i = 0

        # build the subtree made of inorder[left..right] (inclusive)
        def dfs(left, right):
            if left > right:
                return None

            val = preorder[self.pre_i]
            self.pre_i += 1
            root = TreeNode(val)

            mid = position[val]
            root.left = dfs(left, mid - 1)     # build the left side first: preorder lists it first
            root.right = dfs(mid + 1, right)
            return root

        return dfs(0, len(inorder) - 1)