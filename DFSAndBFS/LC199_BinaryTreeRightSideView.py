# coding: utf-8
""" 199. 二叉树的右视图

给定一个二叉树的 根节点 root，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。

示例1:
    1
  /   \
2      3
 \      \
  5      4
输入: [1,2,3,null,5,null,4]
输出: [1,3,4]

示例2:
输入: [1,null,3]
输出: [1,3]

示例3:
输入: []
输出: []
"""
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        '''BFS or DFSd都可

        思路: 层序遍历，但是总右到左, 每一层的第一个元素作为该层代表加入结果列表
        '''
        if not root:
            return []

        q, res = [root], []
        while q:
            # 记录本层最右值
            res.append(q[0].val)
            # 构建本层对列
            lv_q = []
            for node in q:
                if node.right:
                    lv_q.append(node.right)
                if node.left:
                    lv_q.append(node.left)
            # 下一层遍历
            q = lv_q
        return res
