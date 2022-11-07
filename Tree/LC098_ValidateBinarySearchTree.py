# coding: utf-8
"""98. 验证二叉搜索树
给定一个二叉树，判断其是否是一个有效的二叉搜索树。

假设一个二叉搜索树具有如下特征：

节点的左子树只包含小于当前节点的数。
节点的右子树只包含大于当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。
示例 1:

输入:
    2
   / \
  1   3
输出: true
示例 2:

输入:
    5
   / \
  1   4
     / \
    3   6
输出: false
解释: 输入为: [5,1,4,null,null,3,6]。
     根节点的值为 5 ，但是其右子节点值为 4 。

"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        '''中序遍历

        思路: 二叉搜索树的性质决定了其中序遍历结果是单调递增的
        复杂度:
            time: 需要遍历数同时遍历新产生序列, O(N)
            space: 新开数组，O(N)
        '''
        val_list = []
        self._mid(root, val_list)
        for index, val in enumerate(val_list[:-1]):
            if val >= val_list[index + 1]:
                return False
        return True

    def _mid(self, node, val_list):
        if not node:
            return

        self._mid(node.left, val_list)
        val_list.append(node.val)
        self._mid(node.right, val_list)
