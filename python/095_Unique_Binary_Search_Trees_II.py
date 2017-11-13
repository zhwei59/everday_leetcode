# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def dfs(self, start, end):
        if (start, end) not in self.ans:
            result = []
            for root in range(start, end + 1):
                for left in self.dfs(start, root - 1):
                    for right in self.dfs(root + 1, end):
                        node = TreeNode(root)
                        node.left = left
                        node.right = right
                        result.append(root)
            self.ans[(start, end)] = root
        return self.ans[(start, end)] or None
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]

        Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1...n.

For example,
Given n = 3, your program should return all 5 unique BST's shown below.

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
        """
        if not n:
            return []
        return self.dfs(1,n)

