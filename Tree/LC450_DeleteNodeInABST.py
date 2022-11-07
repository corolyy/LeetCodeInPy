# coding: utf-8
"""450. 删除二叉搜索树中的节点
给定一个二叉搜索树的根节点 root 和一个值 key，删除二叉搜索树中的 key 对应的节点，并保证二叉搜索树的性质不变。返回二叉搜索树（有可能被更新）的根节点的引用。

一般来说，删除节点可分为两个步骤：

首先找到需要删除的节点；
如果找到了，删除它。
说明： 要求算法时间复杂度为 O(h)，h 为树的高度。

示例:

root = [5,3,6,2,4,null,7]
key = 3

    5
   / \
  3   6
 / \   \
2   4   7

给定需要删除的节点值是 3，所以我们首先找到 3 这个节点，然后删除它。

一个正确的答案是 [5,4,6,2,null,null,7], 如下图所示。

    5
   / \
  4   6
 /     \
2       7

另一个正确答案是 [5,2,6,null,4,null,7]。

    5
   / \
  2   6
   \   \
    4   7
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        '''BST节点操作框架

        思路:
            1. 找到节点干嘛?删掉它
            2. 还要干点啥?WDNMD, 还得考虑左右子树的重新BST化
        实现:
            if node == target:
                整活
            if node > target:
                process(node.left)
            if node < target:
                process(node.right)
        '''
        if not root:
            return

        if root.val == key:
            return self._delete(root)

        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)
        return root

    def _delete(self, node):
        # 叶子节点直接删
        if not node.right and not node.left:
            return
        # 单边树直接向上挂载
        if not node.left:
            return node.right
        if not node.right:
            return node.left
        # 找到左子树最大的节点或者右子树最小的节点进行删除然后挂载到当前节点
        # 这里以右子树最小节点为例实现(一定是叶子节点或者单边树的根节点)
        right = node.right
        mid_list = []
        self._find_min(right, mid_list)
        r_min_node = mid_list[0]
        # 不要忘了构造树
        r_min_node.right = self.deleteNode(right, r_min_node.val)
        r_min_node.left = node.left
        return r_min_node

    def _find_min(self, root, mid_list):
        if mid_list or not root:
            return

        self._find_min(root.left, mid_list)
        mid_list.append(root)
        self._find_min(root.right, mid_list)
