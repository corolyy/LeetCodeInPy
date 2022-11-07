# coding: utf-8
"""235. 二叉搜索树的最近公共祖先
给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。

百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”

例如，给定如下二叉搜索树:  root = [6,2,8,0,4,7,9,null,null,3,5]


示例 1:

输入: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
输出: 6
解释: 节点 2 和节点 8 的最近公共祖先是 6。
示例 2:

输入: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
输出: 2
解释: 节点 2 和节点 4 的最近公共祖先是 2, 因为根据定义最近公共祖先节点可以为节点本身。


说明:

所有节点的值都是唯一的。
p、q 为不同节点且均存在于给定的二叉搜索树中。

"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        '''从性质出发

        原理: 由根节点开始搜索p、q，p、q同时被找到前不停止，同时记录共同路径，第一次分道扬镳时返回
        约束: 一定有公共祖先
        实现:
            - 剪枝: 搜索途中遇到对方直接返回
        复杂度:
            time: O(lgN) - O(N)
            space: O(lgN) - O(N)
        '''
        def next_node(current_node, target_node):
            if not current_node or current_node == target_node:
                return None
            if current_node.val < target_node.val:
                return current_node.right
            if current_node.val > target_node.val:
                return current_node.left

        if root == p or root == q:
            return root

        common_path = []
        p_head, q_head = root, root
        while True:
            common_path.append(p_head)
            p_head = next_node(p_head, p)
            q_head = next_node(q_head, q)

            if p_head != q_head:
                return common_path[-1]
        return None

    def lowestCommonAncestorModify(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        '''从性质出发

        原理: 由根节点开始搜索p、q，p、q同时被找到前不停止，同时记录共同路径，第一次分道扬镳时返回
        实现:
            - 路径用数组记录
            - 剪枝: 搜索途中遇到对方直接返回
        复杂度:
            time: O(lgN) - O(N)
            space: O(lgN) - O(N)
        '''
        def next_node(current_node, target_node):
            if current_node == target_node:
                return None
            if current_node.val < target_node.val:
                return current_node.right
            if current_node.val > target_node.val:
                return current_node.left

        if root == p or root == q:
            return root

        p_found, q_found, common_path = False, False, []
        p_head, q_head = root, root
        while not (p_found and q_found):
            if p_head == q_head:
                common_path.append(p_head)

            if not p_found:
                p_head = next_node(p_head, p)
                p_found = p_head is None

            if not q_found:
                q_head = next_node(q_head, q)
                q_found = q_head is None

            if not p_found and p_head == q:
                return q
            if not q_found and q_head == p:
                return p
            if p_head != q_head:
                return common_path[-1]
        return None

    def lowestCommonAncestorBruteForce(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        '''从性质出发

        原理: 由根节点开始搜索p、q，路径记在数组中，数组下标即可代表深度增长趋势，取下标最大的共同节点即可
        实现:
            - 路径用数组记录
            - 剪枝: 搜索途中遇到对方直接返回
        复杂度:
            time: O(lgN) - O(N)
            space: O(lgN) - O(N)
        '''
        if root == p or root == q:
            return root

        p_path, q_path = [], []
        head = root
        while head.val != p.val:
            if head == q:
                return q
            p_path.append(head)
            if head.val > p.val:
                head = head.left
            else:
                head = head.right
        p_path.append(head)

        head = root
        while head.val != q.val:
            if head == p:
                return p
            q_path.append(head)
            if head.val > q.val:
                head = head.left
            else:
                head = head.right
        q_path.append(head)

        common_ancestor_list = []
        for i in range(min(len(p_path), len(q_path))):
            if p_path[i] == q_path[i]:
                common_ancestor_list.append(p_path[i])
        return common_ancestor_list[-1] if common_ancestor_list else None
