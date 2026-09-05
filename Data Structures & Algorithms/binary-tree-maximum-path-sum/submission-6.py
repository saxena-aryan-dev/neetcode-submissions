# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxi=float('-inf')
        def tra(root: Optional[TreeNode])-> int:
            if not  root:
                return 0
            curr=root.val    
                  
                
                
            lh=max(0, tra(root.left))

            rh=max(0, tra(root.right))
    
            self.maxi=max(self.maxi,lh+rh+curr)
            return curr+max(lh,rh)
        tra(root)
        return self.maxi