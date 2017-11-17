# -*- coding: UTF-8 -*-
# 给定n个不同的正整数，整数k（k < = n）以及一个目标数字。　

# 在这n个数里面找出K个数，使得这K个数的和等于目标数字，求问有多少种方案？
# 暴力搜索
# def isEqual(self, A, k, target, curr):
#     if k == 0:
#         t = sum(curr)
#         if t == target:
#             self.count += 1
#     else:
#         for i, n in enumerate(A):
#             self.isEqual(A[i + 1:], k - 1, target, curr + [n])
#
#
# def kSum(self, A, k, target):
#     # write your code here
#     self.count = 0
#     self.isEqual(A, k, target, [])
#     return self.count
class Solution:
    def kSum(self, A, k, target):
