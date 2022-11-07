# coding: utf-8
"""95. 不同的二叉搜索树 II
给定一个整数 n，生成所有由 1 ... n 为节点所组成的 二叉搜索树 。

示例：
输入：3
输出：
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]
解释：
以上的输出对应以下 5 种不同结构的二叉搜索树：
   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

提示：
0 <= n <= 8
"""
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        '''回溯: 递归 + 分治 + 缓存

        思路: WDNMD, 内存爆炸的解法
            记录(起点数值, 终点数值)对应的各种树
            如(1, 1): 1
              (1, 2): 1       2
                       \     /
                        2， 1
        复杂度:
            时间: n!
            空间: n!
        '''
        def gen_trees(start, end):
            # 边界保护
            if end < start:
                return []
            # 记忆化加速
            key = (start, end)
            if key in tree_dict:
                return tree_dict[key]
            # base case, 递归退出条件
            if start == end:
                tree_dict[key] = [TreeNode(start)]
                return tree_dict[key]
            # 用左右子区间生成左右子树列表
            tree_list = []
            for val in range(start, end + 1):
                left_trees = gen_trees(start, val - 1)
                right_trees = gen_trees(val + 1, end)
                # 分治: 分类讨论
                if left_trees and right_trees:
                    for l_node in left_trees:
                        for r_node in right_trees:
                            tree_list.append(TreeNode(val, l_node, r_node))
                elif left_trees:
                    for l_node in left_trees:
                        tree_list.append(TreeNode(val, l_node, None))
                elif right_trees:
                    for r_node in right_trees:
                        tree_list.append(TreeNode(val, None, r_node))
                else:
                    tree_list.append(TreeNode(val))
            tree_dict[key] = tree_list
            return tree_dict[key]

        if not n:
            return []

        tree_dict = {}
        gen_trees(1, n)
        return tree_dict[(1, n)]
