# coding: utf-8
"""72. 编辑距离
给你两个单词 word1 和 word2，请你计算出将 word1 转换成 word2 所使用的最少操作数 。

你可以对一个单词进行如下三种操作：

插入一个字符
删除一个字符
替换一个字符


示例 1：

输入：word1 = "horse", word2 = "ros"
输出：3
解释：
horse -> rorse (将 'h' 替换为 'r')
rorse -> rose (删除 'r')
rose -> ros (删除 'e')
示例 2：

输入：word1 = "intention", word2 = "execution"
输出：5
解释：
intention -> inention (删除 't')
inention -> enention (将 'i' 替换为 'e')
enention -> exention (将 'n' 替换为 'x')
exention -> exection (将 'n' 替换为 'c')
exection -> execution (插入 'u')


提示：

0 <= word1.length, word2.length <= 500
word1 和 word2 由小写英文字母组成
"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        '''动态规划

        - 思路: 多阶段决策最优解 -> 动态规划
          1. 状态定义: dp[i][j] -- w1的前i位和w2的前j位的编辑距离
          2. 状态转移方程:
            - w1[i] == w2[j]时: min(dp[i - 1][j] + 1, dp[i][j - 1]+ 1, dp[i - 1][j - 1]);
            - w1[i] != w2[j]时: min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
          3. 解: dp[m][n]
          4. base case: 边缘编辑距离与本身长度相等
        '''
        m, n = len(word1), len(word2)

        # 空字符串场景:
        if not m or not n:
            return m + n

        # 初始化dp数组
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for cnt in range(m + 1):
            dp[cnt][0] = cnt
        for cnt in range(n + 1):
            dp[0][cnt] = cnt

        # 递推dp数组
        for r_idx in range(1, m + 1):
            for c_idx in range(1, n + 1):
                if word1[r_idx - 1] == word2[c_idx - 1]:
                    dp[r_idx][c_idx] = min(dp[r_idx - 1][c_idx] + 1,
                                           dp[r_idx][c_idx - 1] + 1,
                                           dp[r_idx - 1][c_idx - 1])
                else:
                    dp[r_idx][c_idx] = min(dp[r_idx - 1][c_idx],
                                           dp[r_idx][c_idx - 1],
                                           dp[r_idx - 1][c_idx - 1]) + 1
        return dp[m][n]
