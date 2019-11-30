class Solution(object):
    def is_valid_BST(self, root, MIN=float('inf'), MAX=float('-inf')):
        if not root:
            return True

        if root.val <= MAX or root.val >= MIN:
            return False

        return self.is_valid_BST(root.left, min(MIN, root.val), MAX) and \
            self.is_valid_BST(root.right, MIN, max(root.val, MAX))
