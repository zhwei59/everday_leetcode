class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        res = []
        if not root:
            return res
        stack = [root]
        while stack:
            stack, tmp = [], stack
            curr = []
            for n in tmp:
                curr.append(n.val)
                if n.left:
                    stack.append(n.left)
                if n.right:
                    stack.append(n.right)
            res.append(curr)
        return res