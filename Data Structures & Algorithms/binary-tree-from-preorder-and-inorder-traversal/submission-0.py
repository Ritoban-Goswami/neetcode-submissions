# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        pre_idx = 0
        inorder_map = { val: idx for idx, val in enumerate(inorder)}
        def find_root(l_idx: int, r_idx: int) -> TreeNode:
            nonlocal pre_idx

            if l_idx > r_idx:
                return None

            root = TreeNode(preorder[pre_idx])
            pre_idx += 1
            in_idx = inorder_map[root.val]
            root.left = find_root(l_idx, in_idx - 1)
            root.right = find_root(in_idx + 1, r_idx)
            return root

        return find_root(0, len(inorder) - 1)