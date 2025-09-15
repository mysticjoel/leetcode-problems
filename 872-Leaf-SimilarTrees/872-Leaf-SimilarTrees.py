# Last updated: 9/15/2025, 12:12:49 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def collect_leaves(self,node):
        if not node:
            return []
        
        if not node.left and not node.right:
            return [node.val]

        return self.collect_leaves(node.left) + self.collect_leaves(node.right)
            
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leaves1 = self.collect_leaves(root1)
        leaves2 = self.collect_leaves(root2)
        return leaves1==leaves2
