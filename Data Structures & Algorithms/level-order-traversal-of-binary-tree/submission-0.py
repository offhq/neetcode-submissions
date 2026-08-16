# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque([root])
        res = []

        while queue:
            size = len(queue)
            curr_level  = []
            for _ in range(size):
                s = queue.popleft()
                if s:
                    curr_level.append(s.val)
                    if s.left:
                        queue.append(s.left)
                    if s.right:
                        queue.append(s.right)
            res.append(curr_level)
        return res

                        
                    
                
        
        print(res)







        