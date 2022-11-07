# coding: utf-8
"""111. 二叉树的最小深度
给定一个二叉树，找出其最小深度。

最小深度是从根节点到最近叶子节点的最短路径上的节点数量。

说明：叶子节点是指没有子节点的节点。

示例 1：
输入：root = [3,9,20,null,null,15,7]
输出：2

示例 2：
输入：root = [2,null,3,null,4,null,5,null,6]
输出：5

提示：
树中节点数的范围在 [0, 105] 内
-1000 <= Node.val <= 1000
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        '''BFS法

        思路: 最短路径用BFS比较合适，第一次遇到没有子节点的节点时返回当前层数即可
        实现:
            - 标准的BFS模板，且不需要缓存已访问节点
            - 需要独立记录层数: (node, lv)
        复杂度:
            time: O(N)
            space: O(N)
        '''
        if not root:
            return 0

        q = [(root, 1)]
        while q:
            node, lv = q.pop()
            if not node.left and not node.right:
                return lv

            next_lv = lv + 1
            if node.left:
                q.append((node.left, next_lv))
            if node.right:
                q.append((node.right, next_lv))

