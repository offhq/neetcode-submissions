# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue = deque([root])
        res = []
        
        while queue:
            n = len(queue)
            curr_level = []
            for _ in range(n):
                s = queue.popleft()
                if s:
                    curr_level.append(s.val)
                    if s.left:
                        queue.append(s.left)
                    if s.right:
                        queue.append(s.right)
            res.append(curr_level[-1])
        return res



        