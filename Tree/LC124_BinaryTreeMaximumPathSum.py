# coding: utf-8
"""124. 二叉树中的最大路径和
路径 被定义为一条从树中任意节点出发，沿父节点-子节点连接，达到任意节点的序列。同一个节点在一条路径序列中 至多出现一次 。该路径 至少包含一个 节点，且不一定经过根节点。

路径和 是路径中各节点值的总和。

给你一个二叉树的根节点 root ，返回其 最大路径和 。



示例 1：


输入：root = [1,2,3]
输出：6
解释：最优路径是 2 -> 1 -> 3 ，路径和为 2 + 1 + 3 = 6
示例 2：


输入：root = [-10,9,20,null,null,15,7]
输出：42
解释：最优路径是 15 -> 20 -> 7 ，路径和为 15 + 20 + 7 = 42


提示：

树中节点数目范围是 [1, 3 * 104]
-1000 <= Node.val <= 1000
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.max_sum = float('-inf')

    def maxPathSum(self, root: TreeNode) -> int:
        '''递归

        思路:
        1. 每个节点的最大路径和为: 其左右子树最大贡献值之和(< 0时记为0) + 本身值;
        2. 每个节点的最大贡献值为: max(左/右最大贡献值) + 本身值;
            因为父节点联通子节点时只能向下联通其一颗子树，否则该子节点将被重复访问
        实现:

        '''
        def max_gain(node):
            if not node:
                return 0

            # 后续遍历
            # 最大贡献值小于0时实际不会采纳，按0算
            l_gain = max(max_gain(node.left), 0)
            r_gain = max(max_gain(node.right), 0)

            # 本节点最大路径和
            max_price = node.val + l_gain + r_gain
            self.max_sum = max(self.max_sum, max_price)

            # 返回最大贡献值
            return node.val + max(l_gain, r_gain)

        max_gain(root)
        return self.max_sum
