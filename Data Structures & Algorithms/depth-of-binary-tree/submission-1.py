# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depth = 0
        res = 0
        def traverse(node):
            nonlocal depth, res
            depth += 1
            
            if not node:
                depth -= 1
                return
            traverse(node.left)
            res = max(res, depth)
            traverse(node.right)
            depth -= 1
        traverse(root)
        return res
                

        