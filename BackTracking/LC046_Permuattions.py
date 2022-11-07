# coding: utf-8
"""46. 全排列
给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。



示例 1：

输入：nums = [1,2,3]
输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
示例 2：

输入：nums = [0,1]
输出：[[0,1],[1,0]]
示例 3：

输入：nums = [1]
输出：[[1]]


提示：

1 <= nums.length <= 6
-10 <= nums[i] <= 10
nums 中的所有整数 互不相同
"""
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        '''回溯算法

        思路: 全排列，不看顺序，直接每个元素作为起点向下回溯

        '''
        self.result = []

        self._backtrack([], nums)
        return self.result

    def _backtrack(self, sub_list, sub_nums):
        if not sub_nums:
            self.result.append(sub_list.copy())
            return

        for idx, num in enumerate(sub_nums):
            sub_list.append(num)
            sub_nums.pop(idx)
            self._backtrack(sub_list, sub_nums)
            sub_nums.insert(idx, num)
            sub_list.pop(-1)
