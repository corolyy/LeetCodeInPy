# coding: utf-8
"""188. 买卖股票的最佳时机 IV
给定一个整数数组 prices ，它的第 i 个元素 prices[i] 是一支给定的股票在第 i 天的价格。

设计一个算法来计算你所能获取的最大利润。你最多可以完成 k 笔交易。

注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。



示例 1：

输入：k = 2, prices = [2,4,1]
输出：2
解释：在第 1 天 (股票价格 = 2) 的时候买入，在第 2 天 (股票价格 = 4) 的时候卖出，这笔交易所能获得利润 = 4-2 = 2 。
示例 2：

输入：k = 2, prices = [3,2,6,5,0,3]
输出：7
解释：在第 2 天 (股票价格 = 2) 的时候买入，在第 3 天 (股票价格 = 6) 的时候卖出, 这笔交易所能获得利润 = 6-2 = 4 。
     随后，在第 5 天 (股票价格 = 0) 的时候买入，在第 6 天 (股票价格 = 3) 的时候卖出, 这笔交易所能获得利润 = 3-0 = 3 。


提示：

0 <= k <= 100
0 <= prices.length <= 1000
0 <= prices[i] <= 1000
"""
from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        '''动态规划

        思路: 多阶段决策最优解问题

        维度1: 天数i, 即prices里的i, 自然维度, 这类题目主要就靠这个维度向下推
        维度2: 是否持有股票, 不持有为0，持有记为1
        维度3: 交易次数k

        初始状态:
            dp = [[[0, -prices[0]]]]
        状态方程:
            dp[i][0][k] = max{
                            dp[i - 1][1][k - 1] + prices[i],  -- 卖出
                            dp[i - 1][0][k]                   -- 不操作
                        }
            dp[i][1][k] = max{
                            dp[i - 1][0][k] - prices[i],  -- 买入
                            dp[i - 1][1][k]               -- 不操作
                        }

        实现关键:
            1. dp[i][0][0] = dp[0][0][0]
            2. 为避免边界判断，对于前期无法进行买卖的天数使用float('-inf')进行填充, 方便代码实现

        优化: 当len(prices) // 2 <= k时, 实际上相当于可以无限次买卖，此时使用贪心法可以大大降低复杂度
        '''
        if not k or len(prices) < 2:
            return 0

        if len(prices) // 2 <= k:
            return self._max_profit_in_greedy(prices)

        return self._max_profit_in_dp(k, prices)

    def _max_profit_in_greedy(self, prices):
        idx, sum, length = 0, 0, len(prices)
        while idx < length:
            while idx + 1 < length and prices[idx] >= prices[idx + 1]:
                idx += 1
            min = prices[idx]
            while idx + 1 < length and prices[idx] < prices[idx + 1]:
                idx += 1
            sum += prices[idx] - min
            idx += 1
        return sum

    def _max_profit_in_dp(self, k, prices):
        dp = [
            [
                [float('-inf') for _ in range(k + 1)],
                [float('-inf') for _ in range(k + 1)]
            ]
        ]
        dp[0][0][0], dp[0][1][0] = 0, -prices[0]

        for i, p in enumerate(prices[1:], start=1):
            dp.append([[], []])
            for k in range(k + 1):
                if k == 0:
                    dp[i][0].append(0)
                else:
                    dp[i][0].append(max(dp[i - 1][1][k - 1] + prices[i], dp[i - 1][0][k]))
                dp[i][1].append(max(dp[i - 1][0][k] - prices[i], dp[i - 1][1][k]))
        return max(dp[-1][0])
