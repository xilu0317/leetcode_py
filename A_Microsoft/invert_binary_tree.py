class Solution:
    def invert_tree(self, root):
        if not root:
            return None

        # record root.right since it would be modified
        right = root.right

        root.right = self.invertTree(root.left)
        root.left = self.invertTree(right)

        return root


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
