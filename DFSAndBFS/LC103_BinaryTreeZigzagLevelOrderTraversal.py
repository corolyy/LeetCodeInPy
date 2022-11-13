# coding: utf-8
"""103. 二叉树的锯齿形层序遍历
给你二叉树的根节点 root ，返回其节点值的 锯齿形层序遍历 。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。

示例 1：
    3
  /  \
9    20
    /  \
  15    7
输入：root = [3,9,20,null,null,15,7]
输出：[[3],[20,9],[15,7]]

示例 2:
输入：root = [1]
输出：[[1]]

示例 3:
输入：root = []
输出：[]
"""
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ''' BFS小变式

        思路: 标准的BFS，增加一个标志位用来判定正序逆序
        实现: 使用bool表示正序/逆序，每轮not一次即可
        '''
        if not root:
            return []

        q, res, flag = [root], [], True
        while q:
            lv_val, temp_q = [], []
            for node in q:
                # 根据flag判断正序逆序
                if flag:
                    lv_val.append(node.val)
                else:
                    lv_val.insert(0, node.val)
                # 构造下一层遍历对列
                if node.left:
                    temp_q.append(node.left)
                if node.right:
                    temp_q.append(node.right)
            # 构造下一层遍历对列
            q = temp_q
            # 填充响应
            res.append(lv_val)
            # 反转flag
            flag = not flag
        return res
