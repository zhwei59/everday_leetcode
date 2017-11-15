# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def travel(self, left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        if left.val == right.val:
            return self.travel(left.left, right.right) and self.travel(left.right, right.left)
        else:
            return False


def isSymmetric(self, root):
    """
    :type root: TreeNode
    :rtype: bool
    """
    if not root:
        return True
    return self.travel(root.left, root.right)