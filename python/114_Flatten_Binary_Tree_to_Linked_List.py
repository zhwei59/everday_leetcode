class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        前序遍历
        tmp=root.right
        root.right=root.left
        root.left=tmp
        left
        """
        stack=[]
        while root:
            if root.left:
                if root.right:
                    stack.append(root.right)
                root.left,root.right=root.left,None
            if not root.right and stack:
                root.right=stack.pop()
            root=root.right
