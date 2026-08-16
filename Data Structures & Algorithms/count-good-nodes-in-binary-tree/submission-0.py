# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        curr_max = [root.val]
        self.count = 0
        def dfs(node):
            if not node:
                return
            curr_max.append(max(curr_max[-1], node.val))
             
            dfs(node.left)
            if node.val >= curr_max[-1]:
                self.count += 1
            dfs(node.right)
            curr_max.pop(-1)



        dfs(root)
        return self.count
            

