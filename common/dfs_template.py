def dfs_binary_tree(root: Optional[TreeNode]) -> List[int]:
    res = []

    def dfs(node: Optional[TreeNode]):
        if not node:
            return
            
        # Pre-order: process current, then children
        res.append(node.val)
        dfs(node.left)
        dfs(node.right)
    dfs(root)

    return res
