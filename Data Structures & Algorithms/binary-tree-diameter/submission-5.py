# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def diameterOfBinaryTree(self,root:[TreeNode]) -> int:
        self.nums=[]
        
        
        def height(root):
            if not root:
                return 0
            lh=height(root.left) 
            rh=height(root.right)
            self.nums.append(rh+lh)
            
            
            return 1+ max(lh,rh)  
        
        height(root)
        return max(self.nums)   
        