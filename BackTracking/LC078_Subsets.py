# coding: utf-8
"""78. 子集
给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。

解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。



示例 1：

输入：nums = [1,2,3]
输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
示例 2：

输入：nums = [0]
输出：[[],[0]]


提示：

1 <= nums.length <= 10
-10 <= nums[i] <= 10
nums 中的所有元素 互不相同
"""
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        '''回溯

        思路: 按位置回溯，选择仅限于本坐标向后
        '''
        self.result = []
        for i in range(len(nums)):
            self._backtrack(i, nums[i:])
            pass

        self.result = [[]]

        for idx, num in enumerate(nums):
            self.result.append([num])
            self._backtrack(set([num]), nums[idx:])

    def _backtrack(self, num_set, nums):
        if not nums:
            return

        for idx, num in enumerate(nums):
            num_set.add(num)
            num_set.copy()
        pass
