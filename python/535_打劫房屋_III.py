class Solution:
    def visit(self,root):
        if not root:
            return 0,0
        left_rab,left_not_rab=self.visit(root.left)
        right_rab,right_not_rab=self.visit(root.right)
        rab=root.val+left_not_rab+right_not_rab
        not_rab=max(left_not_rab,left_rab)+max(right_not_rab,right_rab)
        return rab,not_rab
    def houseRobber3(self, root):
        rab,not_rab=self.visit(root)
        return max(rab,not_rab)

