# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.sum = root.val
        def dfs(root):
            if not root: return 0
            l = dfs(root.left)
            r = dfs(root.right)
            self.sum = max(self.sum, root.val + max(l, r), root.val, root.val + l + r)
            return max(root.val, root.val + max(l, r))
        return max(dfs(root), self.sum)

        
