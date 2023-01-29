# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def dfs(root,sum):
            if not root: return False
            if root.left == None and root.right == None:
                if sum == root.val:return True
            left = dfs(root.left,sum - root.val)
            right = dfs(root.right,sum - root.val)

            return left or right

        
        return dfs(root,targetSum)
            