# coding: utf-8
"""15. 三数之和
给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有和为 0 且不重复的三元组。

注意：答案中不可以包含重复的三元组。



示例 1：

输入：nums = [-1,0,1,2,-1,-4]
输出：[[-1,-1,2],[-1,0,1]]
示例 2：

输入：nums = []
输出：[]
示例 3：

输入：nums = [0]
输出：[]


提示：

0 <= nums.length <= 3000
-105 <= nums[i] <= 105

"""
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''Hash + 数学

        思路: 问题可以降维成为多个2Sum的问题
        关键:
            - 需要考虑元素间的去重
            - 通过排序降低去重难度
            - 排序后的列表天然利于剪枝
        '''

        def two_sum(start, target):
            if nums[start] > target:
                return []
            l, r, ans_list = start, length - 1, []
            # 使用双指针夹逼求和
            while l < r:
                num_l, num_r = nums[l], nums[r]
                _sum = num_l + num_r
                if _sum > target:
                    r -= 1
                    while r > l and nums[r] == num_r:
                        r -= 1
                elif _sum < target:
                    l += 1
                    while r > l and nums[l] == num_l:
                        l += 1
                else:
                    ans_list.append([num_l, num_r])
                    r -= 1
                    while r > l and nums[r] == num_r:
                        r -= 1
                    l += 1
                    while r > l and nums[l] == num_l:
                        l += 1
            return ans_list

        if len(nums) < 3:
            return []

        nums.sort()  # 排序
        if nums[0] > 0 or nums[-1] < 0:
            return []

        ans_map, length = {}, len(nums)
        for index, num in enumerate(nums[:-2]):
            if num > 0:  # 剪枝
                break
            if num in ans_map:  # 去重
                continue
            ans_map[num] = two_sum(index + 1, 0 - num)

        ans = []
        # 组装结果
        for first, two_sums in ans_map.items():
            if two_sums:
                ans.extend([[first, two_sum[0], two_sum[1]]
                            for two_sum in two_sums])
        return ans
