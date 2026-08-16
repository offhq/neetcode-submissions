# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        minimum = min(p.val, q.val)
        maximum = max(p.val, q.val)
        while root:
            if minimum <= root.val <= maximum:
                return root
            elif minimum > root.val:
                root = root.right
            else:
                root = root.left
        


        
        