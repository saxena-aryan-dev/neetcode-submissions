class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if self.height(root) is  False:
            return False
        return True    
        

    def height(self, root: Optional[TreeNode]):
        if not root:
            return 0
        lh=self.height(root.left)    
        rh=self.height(root.right)
        if lh is False:
            return False
        if rh is False:
            return False    
        if abs(lh-rh)>1:
            return False 
        return 1+ max(rh,lh)
       