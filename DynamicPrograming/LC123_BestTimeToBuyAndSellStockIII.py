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

        维度1: 天数i, 即prices里的i, 自然维度, 这类题目主要就靠这个维度向下推
        维度2: 是否持有股票, 不持有为0，持有记为1
        维度3: 交易次数k
            注意: 交易次数k和天数i之间有约束关系，(i + 1) // 2 >= k，i从0计数，
                只有实际经过2*k天才可能产生k次交易，这里会影响状态矩阵边缘的生成

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
        '''
        dp = [
            [
                [0, float('-inf'), float('-inf')],
                [-prices[0], float('-inf'), float('-inf')]
            ]
        ]
        for i, p in enumerate(prices[1:], start=1):
            dp.append([[], []])
            for k in (0, 1, 2):
                if k == 0:
                    dp[i][0].append(0)
                else:
                    dp[i][0].append(max(dp[i - 1][1][k - 1] + prices[i], dp[i - 1][0][k]))
                dp[i][1].append(max(dp[i - 1][0][k] - prices[i], dp[i - 1][1][k]))
        return max(dp[-1][0])

    def maxProfitUsingNone(self, prices: List[int]) -> int:
        dp = [
            [
                [0, None, None],
                [-prices[0], None, None]
            ]
        ]
        for i, p in enumerate(prices[1:], start=1):
            dp.append([[], []])
            for k in (0, 1, 2):
                if k == 0:
                    dp[i][0].append(0)
                elif dp[i - 1][1][k - 1] is not None and dp[i - 1][0][k] is not None:
                    dp[i][0].append(max(dp[i - 1][1][k - 1] + prices[i], dp[i - 1][0][k]))
                elif dp[i - 1][1][k - 1] is None and dp[i - 1][0][k] is None:
                    dp[i][0].append(None)
                else:
                    dp[i][0].append(dp[i - 1][1][k - 1] + prices[i])

                if dp[i - 1][0][k] is not None and dp[i - 1][1][k] is not None:
                    dp[i][1].append(
                        max(dp[i - 1][0][k] - prices[i], dp[i - 1][1][k]))
                elif dp[i - 1][0][k] is None and dp[i - 1][1][k] is None:
                    dp[i][1].append(None)
                else:
                    dp[i][1].append(dp[i - 1][0][k] - prices[i])
        return max([p for p in dp[-1][0] if p is not None])
