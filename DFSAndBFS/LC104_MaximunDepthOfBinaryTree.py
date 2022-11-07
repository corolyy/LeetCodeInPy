# coding: utf-8
"""104. 二叉树的最大深度
给定一个二叉树，找出其最大深度。

二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。

说明: 叶子节点是指没有子节点的节点。

示例：
给定二叉树 [3,9,20,null,null,15,7]，

    3
   / \
  9  20
    /  \
   15   7
返回它的最大深度 3 。
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        '''BFS法

        思路: 最长路径用BFS也比较合适
        实现:
            - BFS模板变式，单层内部取出所有节点，生成下一层队列，下一层队列为空时，返回最大层数
            - 需要独立记录层数: lv
        复杂度:
            time: O(N)
            space: O(N)
        '''
        if not root:
            return 0

        q, lv = [root], 0
        while q:
            lv += 1
            next_lv = []
            while q:
                node = q.pop()
                if node.left:
                    next_lv.append(node.left)
                if node.right:
                    next_lv.append(node.right)
            q = next_lv
        return lv
