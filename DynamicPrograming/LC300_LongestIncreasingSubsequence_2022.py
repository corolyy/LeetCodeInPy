# coding: utf-8
"""300. 最长递增子序列
给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。

子序列是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子序列。


示例 1：

输入：nums = [10,9,2,5,3,7,101,18]
输出：4
解释：最长递增子序列是 [2,3,7,101]，因此长度为 4 。
示例 2：

输入：nums = [0,1,0,3,2,3]
输出：4
示例 3：

输入：nums = [7,7,7,7,7,7,7]
输出：1


提示：

1 <= nums.length <= 2500
-10^4 <= nums[i] <= 10^4


进阶：

你可以设计时间复杂度为 O(n2) 的解决方案吗？
你能将算法的时间复杂度降低到 O(n log(n)) 吗?
"""
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        '''动态规划

        思路: 动态规划, nums[i]为终点的最长子序列长度，等于0 -> i - 1位中所有<(严格递增)nums[i]的最小子序列长度 + 1
        DP拆解:
          - base case: dp[0] = 1
          - 状态: dp[i] -- 以第i位为终点的最长子序列长度
          - 选择: nums[m] < nums[i]
          - 转移: dp[i] = max(dp[m])
        '''
        # base case
        dp = [1]
        for idx, num in enumerate(nums[1:], start=1):
            dp.append(1)
            for j in range(idx):
                # 选择
                if nums[j] < num:
                    # 转移
                    dp[idx] = max(dp[j] + 1, dp[idx])
        return max(dp)
