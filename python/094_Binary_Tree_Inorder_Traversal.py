#Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution(object):
    def inorderTraversal(self, root):
        res=[]
        stack=[]
        p=root
        while p or stack:
            while p:
                stack.append(p.left)
                p=p.left
            if stack:
                p=stack.pop()
                res.append(p.val)
                p=p.right
        return res
