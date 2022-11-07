# coding: utf-8
"""96. 不同的二叉搜索树
给你一个整数 n ，求恰由 n 个节点组成且节点值从 1 到 n 互不相同的 二叉搜索树 有多少种？返回满足题意的二叉搜索树的种数。

示例 1：
输入：n = 3
输出：5

示例 2：
输入：n = 1
输出：1

提示：
1 <= n <= 19
"""


class Solution:
    def numTrees(self, n: int) -> int:
        """动态规划

        思路: 这尼玛不是动态规划吗?
        状态定义:
            维度1: 天然维度, k的BST数量
        递推公式:
            dp[i] = sum(dp[j] * dp[i - j - 1] for i in range(i))
        解: dp[n]
        """
        # base case
        dp = [1, 1, 2]
        # 递推
        for i in range(3, n + 1):
            cnt_i = 0
            for j in range(i):
                cnt_i += dp[j] * dp[i - j - 1]
            dp.append(cnt_i)
        return dp[n]
