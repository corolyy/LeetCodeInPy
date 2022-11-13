# coding: utf-8
"""236. 二叉树的最近公共祖先
给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。

百度百科中最近公共祖先的定义为：“对于有根树 T 的两个节点 p、q，最近公共祖先表示为一个节点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”

示例1:
     3
   /   \
  5     1
 / \   / \
6   2 0   8
   / \
  7   4
输入：root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
输出：3
解释：节点 5 和节点 1 的最近公共祖先是节点 3 。

示例2:
     3
   /   \
  5     1
 / \   / \
6   2 0   8
   / \
  7   4
输入：root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
输出：5
解释：节点 5 和节点 4 的最近公共祖先是节点 5 。因为根据定义最近公共祖先节点可以为节点本身。

示例3:
输入：root = [1,2], p = 1, q = 2
输出：1

提示：
  - 树中节点数目在范围 [2, 105] 内。
  - -109 <= Node.val <= 109
  - 所有 Node.val 互不相同 。
  - p != q
  - p 和 q 均存在于给定的二叉树中。
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.ancestor = None

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ''' DFS

        思路: DFS, 当前节点为起点的DFS同时找到了两个目标值时, 该节点即可返回
        实现关键:
          1. 每次DFS时都需要有一个数据结构记录是否命中所有target;
          2. 找到公共祖先时如何直接返回;
          3. 如果开始搜索右子树，则最近祖先一定是root
        复杂度:
          - 时间: O(N)
          - 空间: O(N) or O(1)
        '''
        target_set, match_set = {p.val, q.val}, set()
        # 根据提示, 所有节点均不同，那么如果root在目标中，最近公共祖先肯定是它自己
        if root in target_set:
            return root

        match_set = self._dfs(root.left, target_set)
        # 左边可能找到了
        if self.ancestor:
            return self.ancestor
        # print("not find in left")
        # 遍历完半边，只找到一个，不用往下遍历了
        if root.left and match_set:
            # print("must in right")
            return root
        self._dfs(root.right, target_set)
        if self.ancestor:
            return self.ancestor
        return root

    def _dfs(self, root, target_set):
        # 非法或者已经找到，不用遍历
        if not root or self.ancestor:
            return set()
        # print("====>>>", root.val)
        l_macth = self._dfs(root.left, target_set)
        # print("\t left:", l_macth)
        # 已经找到，不用遍历
        if self.ancestor:
            return target_set
        cur_match = l_macth
        # 判断自己
        if root.val in target_set:
            cur_match.add(root.val)
        if cur_match == target_set:
            self.ancestor = root
            return target_set
        # 还没找到，继续遍历
        r_macth = self._dfs(root.right, target_set)
        # print("\t right:", r_macth)
        if self.ancestor:
            return target_set
        cur_match = cur_match.union(r_macth)
        # print(cur_match.union(r_macth))
        if cur_match == target_set:
            self.ancestor = root
            # print(self.ancestor)
        return cur_match
