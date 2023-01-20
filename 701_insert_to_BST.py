# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)

        def treverse(root):
            if not root: return
            if root.left and val < root.val:
                return treverse(root.left)
            if root.right and val > root.val:
                return treverse(root.right)
            if val > root.val:
                root.right = TreeNode(val)
            else:
                root.left = TreeNode(val)

        treverse(root)

        return root