# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        closest = root.val
        def helper(root, target):
            nonlocal closest       
            # Base case
            if root is None:
                return
            
            if abs(target - closest) > abs(root.val - target):
                closest = root.val
            
            # Traverse
            if target > root.val:
                helper(root.right, target)
            elif target < root.val:
                helper(root.left, target)
        
        helper(root, target)
        return closest