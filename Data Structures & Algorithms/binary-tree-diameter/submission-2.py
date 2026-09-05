class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.best = 0

        def height(node):
            if not node:
                return 0
            lh = height(node.left)
            rh = height(node.right)
            self.best = max(self.best, lh + rh)   # path through this node, in edges
            return 1 + max(lh, rh)

        height(root)
        return self.best