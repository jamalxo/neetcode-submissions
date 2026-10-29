class Codec:
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        self.res = ""

        def dfs(node):
            if not node:
                self.res += ', null'
                return
            
            if len(self.res) != 0:
                self.res += ', '
            self.res += str(node.val)
            left = dfs(node.left)
            right = dfs(node.right)
        
        dfs(root)

        return self.res
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        
        if data == ", null":
            return None

        tree = data.strip().split(',')

        self.i = 0

        def build():
            token = tree[self.i]
            token = token.strip()
            self.i += 1

            if token == 'null':
                return None

            node = TreeNode(int(token))
            node.left = build()
            node.right = build()
            return node


        return build()



