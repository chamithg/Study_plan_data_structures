# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        numMap =set()

        def treverse(root):
            #  return false when there is no more roots.
            if not root:return False
            
            # if k- val is in the set, it means there is a sum.
            if k-root.val in numMap:
                return True
            else: numMap.add(root.val)
            
            # if either left or right returns true, which means there is a sum.
            left = treverse(root.left)
            right = treverse(root.right)

            return left or right
        
        return treverse(root)