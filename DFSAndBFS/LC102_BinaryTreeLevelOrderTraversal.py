# coding: utf-8
"""102. 二叉树的层序遍历
给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。



示例：
二叉树：[3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其层序遍历结果：

[
  [3],
  [9,20],
  [15,7]
]
"""
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        '''BFS法

        思路: 二叉树层序遍历其实就是BFS
        实现:
            - 标准BFS的变式, 每次循环时把当层所有节点获取
            - 注意顺序从左往右， pop时需要用pop(0)
        复杂度:
            time: O(N)
            space: O(N), 要开临时列表
        '''
        if not root:
            return []

        q, l_o_list = [root], []
        while q:
            lv_q, lv_list = [], []
            while q:
                node = q.pop(0)
                lv_list.append(node.val)
                if node.left:
                    lv_q.append(node.left)
                if node.right:
                    lv_q.append(node.right)
            q = lv_q
            l_o_list.append(lv_list)
        return l_o_list
