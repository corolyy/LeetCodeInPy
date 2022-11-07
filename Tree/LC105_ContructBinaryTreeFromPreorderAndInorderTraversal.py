# coding: utf-8
"""105. 从前序与中序遍历序列构造二叉树
根据一棵树的前序遍历与中序遍历构造二叉树。

注意:
你可以假设树中没有重复的元素。

例如，给出

前序遍历 preorder = [3,9,20,15,7]
中序遍历 inorder = [9,3,15,20,7]
返回如下的二叉树：

    3
   / \
  9  20
    /  \
   15   7
"""
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        '''递归+二叉树框架

        思路:
            1. 题目让我干啥?根据遍历结果反推树，我得先找到根节点呀
            2. 根节点该干啥?通过前序遍历确认根节点，通过中序遍历确认左右子树
            3. 该用什么遍历?先序
        实现: 递归 + 利用二叉树性质加速
            - 前序遍历性质: 根节点 + 左子树 + 右子树
            - 中序遍历性质: 左子树 + 根节点 + 右子树
            - 后续遍历性质: 左子树 + 右子树 + 根节点
            利用相关性质在实现过程中不再重新构造中间数据结构以提升时间/空间复杂度

        '''
        def build_tree(pre_left, pre_right, in_left, in_right):
            if pre_right < pre_left:
                return

            root = TreeNode(preorder[pre_left])
            in_idx = val_idx_mapping[root.val]
            left_size = in_idx - in_left
            root.left = build_tree(pre_left + 1, pre_left + left_size,
                                   in_left, in_idx - 1)
            root.right = build_tree(pre_left + left_size + 1, pre_right,
                                    in_idx + 1, in_right)
            return root

        val_idx_mapping = {val: idx for idx, val in enumerate(preorder)}
        return build_tree(0, len(preorder) - 1, 0, len(inorder) - 1)

    def buildTreeBruteForce(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        '''递归+二叉树框架

        思路:
            1. 题目让我干啥?根据遍历结果反推树，我得先找到根节点呀
            2. 根节点该干啥?通过前序遍历确认根节点，通过中序遍历确认左右子树
            3. 该用什么遍历?先序
        实现: 递归
        '''
        if not preorder or not inorder:
            return

        root = TreeNode(preorder[0])
        in_idx = inorder.index(root.val)
        l_in, r_in = inorder[0: in_idx], inorder[in_idx + 1:]
        l_pre, r_pre = [], []
        for node in preorder:
            if node in l_in:
                l_pre.append(node)
            if node in r_in:  # 因为没有重复元素，所以不用elif
                r_pre.append(node)
        root.left = self.buildTree(l_pre, l_in)
        root.right = self.buildTree(r_pre, r_in)
        return root
