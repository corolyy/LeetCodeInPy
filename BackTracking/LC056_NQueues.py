# coding: utf-8
"""51. N 皇后
n 皇后问题 研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
给你一个整数 n ，返回所有不同的 n 皇后问题 的解决方案。
每一种解法包含一个不同的 n 皇后问题 的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。


示例 1：
输入：n = 4
输出：[[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
解释：如上图所示，4 皇后问题存在两个不同的解法。

示例 2：
输入：n = 1
输出：[["Q"]]

提示：
1 <= n <= 9
皇后彼此不能相互攻击，也就是说：任何两个皇后都不能处于同一条横行、纵行或斜线上。
"""
from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def gen_q(idx):
            q_list = ['.' for _ in range(n)]
            q_list[idx] = 'Q'
            return ''.join(q_list)
        """DFS + 数学 + 回溯

        思路:
            - 需要穷举: DFS, 逐层向下
            - Q的约束:
                1. 横向: 字典缓存判重
                2. 斜向: 若Q放在位置(i, j), 则x + y = i + j, x - y = i - j两个方向都不能放
                        即以(i + j, i - j)作为判重依据
        """
        pre_list, n_q_list = [], []
        pre_y_cache, pre_slash_cache = set(), [set(), set()]
        self._dfs(0, n, pre_y_cache, pre_slash_cache, pre_list, n_q_list)
        return [[gen_q(index) for index in q_list] for q_list in n_q_list]

    def _dfs(self, lv, n, pre_y_cache, pre_slash_cache, pre_list, n_q_list):
        if lv == n:
            n_q_list.append(pre_list)
            return

        for j in range(n):
            # 判重
            if j in pre_y_cache:
                continue
            slash_idx = (j + lv, j - lv)
            if slash_idx[0] in pre_slash_cache[0] or slash_idx[1] in pre_slash_cache[1]:
                continue

            # 进入下一层之前生成新的判重缓存
            pre_y_cache.add(j)
            pre_slash_cache[0].add(slash_idx[0])
            pre_slash_cache[1].add(slash_idx[1])
            cur_list = pre_list.copy()
            cur_list.append(j)
            self._dfs(lv + 1, n, pre_y_cache, pre_slash_cache, cur_list, n_q_list)
            # 递归结束后恢复老的判重缓存
            pre_slash_cache[0].remove(slash_idx[0])
            pre_slash_cache[1].remove(slash_idx[1])
            pre_y_cache.remove(j)
