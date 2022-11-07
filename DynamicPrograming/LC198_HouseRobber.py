# coding: utf-8
"""198. 打家劫舍
你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。



示例 1：

输入：[1,2,3,1]
输出：4
解释：偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
     偷窃到的最高金额 = 1 + 3 = 4 。
示例 2：

输入：[2,7,9,3,1]
输出：12
解释：偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
     偷窃到的最高金额 = 2 + 9 + 1 = 12 。


提示：

1 <= nums.length <= 100
0 <= nums[i] <= 400
"""
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        '''动态规划

        - 思路: 多阶段决策最优解, 尝试dp
          1. 状态定义: dp[i], 偷盗第i间房能获得的最大收益
          2. 状态转移方程: dp[i] = max(dp[i - 1], dp[i - 2] + dp[i])
          3. 解: max(dp)
        - 实现:
          base case: dp[0], dp[1] = nums[0], max(nums[0], nums[1])
        '''
        if len(nums) < 3:
            return max(nums)

        dp = [nums[0], max(nums[0], nums[1])]
        for i in range(2, len(nums)):
            dp.append(max(dp[i - 1], nums[i] + dp[i - 2]))
        return dp[-1]


s = Solution()
print(s.rob([1, 2, 3, 1]))  # Exp: 4
print(s.rob([2, 7, 9, 3, 1]))  # Exp: 12
print(s.rob([2, 1, 1, 2]))  # Exp: 4
