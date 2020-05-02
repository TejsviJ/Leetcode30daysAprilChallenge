class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def helper(root):
            if not root:
                return (0 , 0)
            left = helper(root.left)
            right = helper(root.right)
            return (max(left[0], right[0]) + 1 , max(left[0] + right[0] + 1, max(left[1], right[1]))) 
        if not root:
            return 0


        return  helper(root)[1] - 1 
