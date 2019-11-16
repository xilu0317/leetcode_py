class Solution(object):
    def is_valid_BST(self, root, less_than=float('inf'), larger_than=float('-inf')):
        if not root:
            return True

        if root.val <= larger_than or root.val >= less_than:
            return False

        return self.is_valid_BST(root.left, min(less_than, root.val), larger_than) and \
               self.is_valid_BST(root.right, less_than, max(root.val, larger_than))
