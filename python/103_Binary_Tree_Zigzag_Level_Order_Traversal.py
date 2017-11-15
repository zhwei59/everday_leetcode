class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        nodes=[root]
        res=[]
        odd=False
        while nodes:
            curr=[]
            tmp,nodes=nodes,[]

            for n in tmp:
                if not odd:
                    if n.left:
                        nodes.append(n.left)
                    if n.right:
                        nodes.append(n.right)
                else :
                    if n.right:
                        nodes.append(n.right)
                    if n.left:
                        nodes.append(n.left)
                curr.append(n.val)
            res.append(curr)
            odd=False if odd else True
            nodes.reverse()
        return res