class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        best = 0

        def depth(node):
            nonlocal best
            if not node:
                return 0
            l = depth(node.left)
            r = depth(node.right)
            best = max(best, l + r)
            return 1 + max(l, r)

        depth(root)
        return best