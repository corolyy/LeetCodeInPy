# coding: utf-8
"""22. 括号生成
数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。



示例 1：

输入：n = 3
输出：["((()))","(()())","(())()","()(())","()()()"]
示例 2：

输入：n = 1
输出：["()"]


提示：

1 <= n <= 8
"""
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """DFS法

        思路: 问题可以抽象为一个n * n矩阵从入口(0， 0)到出口(n, n)的路径穷举,
            每一步都可以向下和向右走 约束为每一步都要x >= y
        实现:
            - 每一步向下、向右保证了路径趋势是单向的，不用记录重复状态
            - 本题不是最常见的找目标类型，而是寻找所有可能解
                _dfs函数的职责不是返回答案，而是在达到目标态时记录当时的解
        复杂度:
            time: O(N^2)
            space: O(1)
        """
        pt_list = []
        self._dfs(0, 0, "", n, pt_list)
        return pt_list

    def _dfs(self, x, y, parenthesis, n, pt_list):
        if x == n and y == n:
            pt_list.append(parenthesis)
            return
        elif x > n or y > n:
            return
        elif y > x:
            return

        self._dfs(x + 1, y, parenthesis + "(", n, pt_list)
        self._dfs(x, y + 1, parenthesis + ")", n, pt_list)
