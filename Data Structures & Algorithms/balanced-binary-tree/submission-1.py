class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if self.height(root) is False:
            return False
        return True

    def height(self, root: Optional[TreeNode]):
        if not root:
            return 0
        left_height = self.height(root.left)
        if left_height is False:
            return False
        right_height = self.height(root.right)
        if right_height is False:
            return False
        if abs(left_height - right_height) > 1:
            return False
        return 1 + max(left_height, right_height)