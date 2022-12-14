"""114. 二叉树展开为链表
给你二叉树的根结点 root ，请你将它展开为一个单链表：

展开后的单链表应该同样使用 TreeNode ，其中 right 子指针指向链表中下一个结点，而左子指针始终为 null 。
展开后的单链表应该与二叉树 先序遍历 顺序相同。

示例 1：
输入：root = [1,2,5,3,4,null,6]
输出：[1,null,2,null,3,null,4,null,5,null,6]

示例 2：
输入：root = []
输出：[]

示例 3：
输入：root = [0]
输出：[0]

提示：
树中结点数在范围 [0, 2000] 内
-100 <= Node.val <= 100

进阶：你可以使用原地算法（O(1) 额外空间）展开这棵树吗？
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        '''递归 + 框架
        
        思路:
            1. 题目让我干嘛?把左子树干掉，展开成只有右子树的情况，顺序与先序遍历相同
            2. 根节点该干嘛?把左子节点挂到右子节点，把左子节点挂到右子树的尾节点的右子节点
            3. 我该怎么遍历?先序
        '''
        if not root or not (root.left or root.right):
            return

        if root.left:
            root.right, r, root.left = root.left, root.right, None
            self.flatten(root.right)
            self._get_last_node(root.right).right = r
            self.flatten(r)
        else:
            self.flatten(root.right)

    def _get_last_node(self, root: TreeNode) -> TreeNode:
        node = root
        while node.right:
            node = node.right
        return node
