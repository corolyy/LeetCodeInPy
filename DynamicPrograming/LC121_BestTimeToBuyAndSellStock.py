# coding: utf-8
"""121. 买卖股票的最佳时机
给定一个数组 prices ，它的第 i 个元素 prices[i] 表示一支给定股票第 i 天的价格。

你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。设计一个算法来计算你所能获取的最大利润。

返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0 。



示例 1：

输入：[7,1,5,3,6,4]
输出：5
解释：在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。
示例 2：

输入：prices = [7,6,4,3,1]
输出：0
解释：在这种情况下, 没有交易完成, 所以最大利润为 0。


提示：

1 <= prices.length <= 10^5
0 <= prices[i] <= 10^4
"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''动态规划

        思路: 多阶段决策最优解问题

        维度1: 天数
        维度2: 交易次数；注意买入不算交易，卖出才算
        维度3: 是否有股票, 无: 0, 有: 1
        状态: 当前维度下的最大利润

        状态转移方程:
        dp[i][j][0] = max(
                        dp[i - 1][j - 1][0],  -- 无法转移, 因为无法卖出;
                        dp[i - 1][j - 1][1] + price[i],  -- 卖出, j > 0, i >= 2
                        dp[i - 1][j][0],  -- 不动
                        dp[i - 1][j][1]  -- 无法转移, 因为已经买卖j次
                        )

        dp[i][j][1] = max(
                        dp[i - 1][j - 1][0] - price[i],  -- 无法转移, [j - 1][0]需要买入再卖出才能到[j][0]然后才能买入
                        dp[i - 1][j - 1][1],  -- 买过, 不动, j > 0, i > = 2
                        dp[i - 1][j][0] - price[i],  -- 买入
                        dp[i - 1][j][1] + price[i],  -- 无法转移, 因为已经交易j次
                        )
        解: max{dp[i][0][0], dp[i][1][0]}

        复杂度:
            time: O(N * 2 * 2) => O(N)
            space: O(N)
        '''
        dp = [
            [
                [0, -prices[0]],
                []
            ]
        ]
        for i, p in enumerate(prices[1:], start=1):
            dp[i].append([])
            for j in range(2):
                dp[j].append([])
                if j > 0 and i > 1:
                    dp[i][j].append(max(dp[i - 1][j - 1][1] + prices[i], dp[i - 1][j][0]))
                    dp[i][j].append(max(dp[i - 1][j - 1][1], dp[i - 1][j][0] - prices[i]))
                else:
                    dp[i][j].append(dp[i - 1][j][0])
                    dp[i][j].append(max(dp[i - 1][j][1], dp[i - 1][j][0] - prices[i]))

        return max(dp[-1][0][0], dp[-1][1][0])
