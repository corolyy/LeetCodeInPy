# coding: utf-8
"""322. 零钱兑换
给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。

你可以认为每种硬币的数量是无限的。



示例 1：

输入：coins = [1, 2, 5], amount = 11
输出：3
解释：11 = 5 + 5 + 1
示例 2：

输入：coins = [2], amount = 3
输出：-1
示例 3：

输入：coins = [1], amount = 0
输出：0
示例 4：

输入：coins = [1], amount = 1
输出：1
示例 5：

输入：coins = [1], amount = 2
输出：2


提示：

1 <= coins.length <= 12
1 <= coins[i] <= 2^31 - 1
0 <= amount <= 10^4
"""
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        '''动态规划

        思路: 攒到amount的最少个数 = min(amount - 各个面值的最少个数) + 1
        状态定义:
            dp[i]  -- 凑到i的最少币数
        转移方程:
            dp[i] = min(dp(i - coins[0]), ..., dp(i - coins[n - 1])) + 1, i - coin[j] >= 0 且 dp[i - coin[j]] != -1
        解:
            dp[n]
        复杂度:
            time: O(M * N), M - coins长度, N - amount
            space: O(N)
        '''
        coins.sort()
        dp = [0]
        for i in range(1, amount + 1):
            cnt_list = []
            for coin in coins:
                _amount = i - coin
                if _amount < 0 or dp[_amount] == -1:
                    continue
                cnt_list.append(dp[i - coin] + 1)
            dp.append(min(cnt_list) if cnt_list else -1)
        return dp[-1]
