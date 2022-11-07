# coding: utf-8
"""199. 二叉树的右视图
给定一棵二叉树，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。

示例:

输入: [1,2,3,null,5,null,4]
输出: [1, 3, 4]
解释:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
"""
# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        '''层序遍历

        - 思路: 层序遍历, 记录每层尾节点即可
        - 复杂度:
            time: O(N)
            space: O(N)
        '''
        if not root:
            return []

        res, lv_q = [root.val], [root]
        while lv_q:
            cur_lv = []
            for node in lv_q:
                if node.left:
                    cur_lv.append(node.left)
                if node.right:
                    cur_lv.append(node.right)
            if cur_lv:
                res.append(cur_lv[-1].val)
            lv_q = cur_lv
        return res
