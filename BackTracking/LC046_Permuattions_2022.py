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
        实现关键:
            1. 按元素数目: 0 -> 1 -> 2 -> 3...向下决策
            2. 维护两个结构:
                - 上一层决策完传下来的列表
                - 当前层可供决策的元素列表
            3. 终止条件: 可决策元素为空
            4. 记住1、2、3按照back_track模版实现即可
        '''
        def _back_track(pre_result: List[int], cur_elems: List[int]):
            # 终止条件
            if not cur_elems:
                results.append(pre_result.copy())
                return
            # 开始回溯
            for idx, elem in enumerate(cur_elems):
                # 决策: 全排列直接挨个选择即可
                pre_result.append(elem)
                cur_elems.pop(idx)
                # 向下回溯
                _back_track(pre_result, cur_elems)
                # 撤销: 标准模版
                pre_result.pop(-1)
                cur_elems.insert(idx, elem)

        results = []
        _back_track([], nums)
        return results
