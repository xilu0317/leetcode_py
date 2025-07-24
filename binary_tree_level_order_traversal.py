class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        if not root:
            return res
        queue = [root]
        while queue:
            res.append([node.val for node in queue])
            queue = [child for node in queue for child in (node.left, node.right) if child]
        return res