# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        def build_subtree(preorder_start: int, inorder_start: int, subtree_size: int):
            if subtree_size <= 0:
                return None
            root_value = preorder[preorder_start]
            root_inorder_index = inorder_index_map[root_value]
            left_subtree_size = root_inorder_index - inorder_start
            left_child = build_subtree(
                preorder_start + 1, 
                inorder_start, 
                left_subtree_size
            )
            right_child = build_subtree(
                preorder_start + 1 + left_subtree_size,
                root_inorder_index + 1,
                subtree_size - left_subtree_size - 1
            )
            return TreeNode(root_value, left_child, right_child)
        inorder_index_map = {value: index for index, value in enumerate(inorder)}
        return build_subtree(0, 0, len(preorder))

        

        