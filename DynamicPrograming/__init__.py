# coding: utf-8
"""
特征: 多阶段决策最优解问题 -> 最优子结构、重复子问题、无后效性

思路: 定义状态 -> 明确dp数组 -> 做好选择(让状态转移起来) -> 明确BaseCase

转移思路: 1. 必须是由已知向未知转移; 2. 转移方向为目标解.
"""
from typing import List


'''示例: 凑零钱'''


# 伪码框架
def coin_change(coins: List[int], amount: int):
    # 定义：要凑出金额 n，至少要 dp(n) 个硬币
    def dp(n):
        # base case
        if n == 0: return 0
        if n < 0: return  -1
        # 做选择，需要硬币最少的那个结果就是答案
        for coin in coins:
            if n - coin < 0:
                continue
            res = min(res, 1 + dp(n - coin))
        return res
    # 我们要求目标金额是 amount
    return dp(amount)
