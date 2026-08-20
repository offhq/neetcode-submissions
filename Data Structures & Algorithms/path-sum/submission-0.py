# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, curr_sum):

            if not node:
                
                return False
            curr_sum = curr_sum + node.val
            if curr_sum == targetSum and not node.left and not node.right:
                return True
            return any([dfs(node.left, curr_sum), dfs(node.right, curr_sum)])
        return dfs(root, 0)
        